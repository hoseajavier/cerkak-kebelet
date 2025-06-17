# cerkak-kebelet
📘 Panduan Instalasi dan Penggunaan Aplikasi Pencarian Naskah RDF
🔗 Link Download
Apache Jena Fuseki: https://jena.apache.org/download/

⚙️ Panduan Instalasi Apache Jena Fuseki
1. Unduh Apache Jena Fuseki
Buka tautan download di atas.

Temukan dan unduh file Apache Jena Fuseki dengan format ZIP atau TAR.GZ.

2. Salin dan Ekstrak File
Setelah diunduh, salin file (misalnya apache-jena-fuseki-x.x.x.zip) ke lokasi yang mudah diakses, seperti direktori C:\ untuk pengguna Windows.

Ekstrak isi file tersebut. Hasilnya adalah folder baru dengan nama apache-jena-fuseki-x.x.x.

3. Akses Folder Fuseki
Masuk ke dalam folder hasil ekstraksi tersebut.

4. Verifikasi Java dan Masuk ke Direktori
Buka Command Prompt atau Terminal.

Ketik java -version untuk memastikan Java sudah terinstal dengan benar.

Arahkan direktori aktif ke folder Fuseki yang sudah diekstrak.

5. Jalankan Server Fuseki
Jalankan perintah fuseki-server --update --mem /ds.

--update berarti operasi pembaruan pada dataset diizinkan.

--mem berarti dataset disimpan di memori sementara.

/ds adalah nama dataset.

Jika berhasil, server akan aktif di alamat http://localhost:3030.

6. Akses Web Interface
Buka browser dan masukkan alamat http://localhost:3030.

Jika berhasil, halaman antarmuka Fuseki akan tampil dengan indikator status berwarna hijau.

📥 Memuat Data RDF ke Apache Jena Fuseki
Buat dataset baru melalui antarmuka web Apache Jena Fuseki.

Masukkan file RDF ke dalam dataset yang telah dibuat.

Jalankan query SPARQL untuk melakukan pencarian data.

💻 Panduan Penggunaan Aplikasi Streamlit
Menjalankan Aplikasi
Jalankan aplikasi dengan mengetikkan perintah streamlit run nama_projek.py.

Mengakses Aplikasi
Setelah server berjalan, buka browser dan masuk ke http://localhost:8501.

Cara Menggunakan Aplikasi
Masukkan kata kunci pencarian yang ingin dicari (misalnya dalam Aksara Jawa, Bahasa Jawa, atau Bahasa Indonesia).

Aplikasi akan menampilkan baris-baris yang mengandung kata kunci tersebut beserta hasil translasi, transliterasi, dan aksara Jawa-nya.

Jika ingin melihat seluruh baris dari teks cerkak, scroll ke bagian bawah dan klik tombol "Tampilkan semua baris".

