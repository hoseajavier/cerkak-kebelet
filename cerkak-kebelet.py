import streamlit as st
import time
from SPARQLWrapper import SPARQLWrapper, JSON

# --- Fungsi untuk query Fuseki ---
def query_fuseki(kata: str):
    sparql = SPARQLWrapper("http://localhost:3030/cerkak-kebelet/sparql")
    sparql.setReturnFormat(JSON)

    filter_clauses = []
    if kata:
        filter_clauses.append(f'CONTAINS(LCASE(STR(?aksara)), "{kata.lower()}")')
        filter_clauses.append(f'CONTAINS(LCASE(STR(?transliterasi)), "{kata.lower()}")')
        filter_clauses.append(f'CONTAINS(LCASE(STR(?translasi)), "{kata.lower()}")')
    
    filter_str = " || ".join(filter_clauses)
    
    query = f"""
    PREFIX : <http://contoh.org/cerkak#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX dcterms: <http://purl.org/dc/terms/>

    SELECT ?barisID ?aksara ?transliterasi ?translasi
    WHERE {{
      ?baris a :BarisCerkak ;
             dcterms:identifier ?barisID ;
             :mengandungAksara ?aksaraNode ;
             :hasTransliteration ?translitNode ;
             :hasTranslation ?transNode .

      ?aksaraNode rdf:value ?aksara .
      ?translitNode rdf:value ?transliterasi .
      ?transNode rdf:value ?translasi .

      FILTER ({filter_str})
    }}
    ORDER BY ?barisID
    """
    sparql.setQuery(query)
    try:
        results = sparql.query().convert()
        return results["results"]["bindings"]
    except Exception as e:
        st.error(f"Koneksi ke Fuseki gagal atau query bermasalah: {e}. Pastikan Apache Jena Fuseki sedang berjalan di http://localhost:3030/cerkak-kebelet/sparql.")
        return []

# --- Fungsi metadata cerkak ---
def get_cerkak_metadata():
    sparql = SPARQLWrapper("http://localhost:3030/cerkak-kebelet/sparql")
    sparql.setReturnFormat(JSON)

    query = """
    PREFIX : <http://contoh.org/cerkak#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?title ?language ?creator ?scriptLabel ?scriptRegion
    WHERE {
      :cerkak dcterms:title ?title ;
              dcterms:language ?language ;
              dcterms:creator ?creator ;
              :ditulisMenggunakan ?scriptSystem .
      ?scriptSystem rdfs:label ?scriptLabel ;
                    :berasalDariWilayah ?scriptRegion .
    }
    """
    sparql.setQuery(query)
    try:
        results = sparql.query().convert()
        if results["results"]["bindings"]:
            return results["results"]["bindings"][0]
        return None
    except Exception as e:
        st.error(f"Gagal mengambil metadata cerkak dari Fuseki: {e}")
        return None

# --- Konfigurasi Streamlit ---
st.set_page_config(
    page_title="Kamus Jawa Kuno",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Tentang Cerkak</h2>", unsafe_allow_html=True)
    metadata = get_cerkak_metadata()
    if metadata:
        st.write(f"*Judul:* {metadata['title']['value']}")
        st.write(f"*Penulis:* {metadata['creator']['value']}")
        st.write(f"*Bahasa:* {metadata['language']['value']}")
        st.write(f"*Sistem Tulisan:* {metadata['scriptLabel']['value']}")
        st.write(f"*Asal Wilayah Tulisan:* {metadata['scriptRegion']['value']}")
    else:
        st.info("Metadata cerkak tidak dapat dimuat.")
    st.markdown("---")
    st.markdown("Aplikasi ini dibuat untuk membantu Anda mencari dan memahami teks cerkak Jawa Kuno.")
    st.markdown("Pastikan Fuseki Anda berjalan pada http://localhost:3030/cerkak-kebelet/sparql")

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📖 Kamus Jawa Kuno</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em;'>Cari kata dalam <em>aksara Jawa</em>, <strong>transliterasi Latin</strong>, atau <strong>terjemahan Bahasa Indonesia</strong>.</p>", unsafe_allow_html=True)

kata_kunci = st.text_input("🔎 Masukkan Kata Kunci", placeholder='Contoh: "ꦧꦸꦩꦶ", "bhumi", atau "tanah"').strip()

if kata_kunci:
    with st.spinner("🔍 Sedang mencari..."):
        time.sleep(0.5)
        hasil_fuseki = query_fuseki(kata_kunci)

        if hasil_fuseki:
            st.success(f"✅ Ditemukan {len(hasil_fuseki)} hasil dari Cerkak Kebelet:")
            for item in hasil_fuseki:
                baris_id = item["barisID"]["value"]
                aksara = item["aksara"]["value"]
                translit = item["transliterasi"]["value"]
                translasi = item["translasi"]["value"]

                with st.expander(f"📝 *Baris ID: {baris_id}*"):
                    st.markdown(f"🔤 *Aksara Jawa:* <span style='font-size: 1.2em;'>{aksara}</span>", unsafe_allow_html=True)
                    st.markdown(f"📖 *Transliterasi (Jawa):* <span style='font-family: monospace;'>{translit}</span>", unsafe_allow_html=True)
                    st.markdown(f"🇮🇩 *Terjemahan (Indonesia):* {translasi}", unsafe_allow_html=True)

                    # Tombol 3 kolom
                    col1, col2, col3 = st.columns(3)
                    copied_text = None
                    with col1:
                        if st.button("Salin Aksara", key=f"copy_aksara_{baris_id}"):
                            copied_text = aksara
                    with col2:
                        if st.button("Salin Transliterasi", key=f"copy_translit_{baris_id}"):
                            copied_text = translit
                    with col3:
                        if st.button("Salin Terjemahan", key=f"copy_translasi_{baris_id}"):
                            copied_text = translasi

                    if copied_text:
                        st.code(copied_text, language='text')
                        st.success("Teks berhasil disalin!")

            st.markdown("---")
            st.info("Hasil diurutkan berdasarkan ID Baris.")
        else:
            st.warning("❌ Kata tidak ditemukan di database Fuseki.")
            st.info("Pastikan Anda telah menjalankan Apache Jena Fuseki dan memuat data cerkak.")

# --- Jelajahi Semua Data ---
st.markdown("---")
st.markdown("#### Lihat Semua Baris Data")
st.info("Fitur ini akan menampilkan semua baris cerkak.")
if st.button("Tampilkan Semua Baris"):
    with st.spinner("Mengambil semua baris..."):
        time.sleep(1)
        sparql_all = SPARQLWrapper("http://localhost:3030/cerkak-kebelet/sparql")
        sparql_all.setReturnFormat(JSON)
        query_all = """
        PREFIX : <http://contoh.org/cerkak#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX dcterms: <http://purl.org/dc/terms/>

        SELECT ?barisID ?aksara ?transliterasi ?translasi
        WHERE {
          ?baris a :BarisCerkak ;
                 dcterms:identifier ?barisID ;
                 :mengandungAksara ?aksaraNode ;
                 :hasTransliteration ?translitNode ;
                 :hasTranslation ?transNode .

          ?aksaraNode rdf:value ?aksara .
          ?translitNode rdf:value ?transliterasi .
          ?transNode rdf:value ?translasi .
        }
        ORDER BY ?barisID
        """
        sparql_all.setQuery(query_all)
        try:
            all_results = sparql_all.query().convert()
            all_lines = all_results["results"]["bindings"]
            if all_lines:
                st.write(f"Menampilkan {len(all_lines)} baris cerkak:")
                for item in all_lines:
                    baris_id = item["barisID"]["value"]
                    aksara = item["aksara"]["value"]
                    translit = item["transliterasi"]["value"]
                    translasi = item["translasi"]["value"]
                    with st.expander(f"📝 *Baris ID: {baris_id}*"):
                        st.markdown(f"🔤 *Aksara Jawa:* <span style='font-size: 1.2em;'>{aksara}</span>", unsafe_allow_html=True)
                        st.markdown(f"📖 *Transliterasi (Jawa):* <span style='font-family: monospace;'>{translit}</span>", unsafe_allow_html=True)
                        st.markdown(f"🇮🇩 *Terjemahan (Indonesia):* {translasi}", unsafe_allow_html=True)
            else:
                st.warning("Tidak ada baris cerkak yang ditemukan dalam database.")
        except Exception as e:
            st.error(f"Gagal mengambil semua baris cerkak: {e}")
