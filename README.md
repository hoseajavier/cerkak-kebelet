# cerkak-kebelet
## 📘 Panduan Instalasi dan Penggunaan Aplikasi Pencarian Naskah RDF
### 🔗 Link Download
Apache Jena Fuseki: **https://jena.apache.org/download/**

### ⚙️ Panduan Instalasi Apache Jena Fuseki
1. Unduh Apache Jena Fuseki
- Buka tautan download di atas.
- Temukan dan unduh file Apache Jena Fuseki dengan format ZIP atau TAR.GZ.
2. Salin dan Ekstrak File
- Setelah diunduh, salin file (misalnya apache-jena-fuseki-x.x.x.zip) ke lokasi yang mudah diakses, seperti direktori C:\ untuk pengguna Windows.
- Ekstrak isi file tersebut. Hasilnya adalah folder baru dengan nama apache-jena-fuseki-x.x.x.
3. Akses Folder Fuseki
- Masuk ke dalam folder hasil ekstraksi tersebut.
4. Verifikasi Java dan Masuk ke Direktori
- Buka Command Prompt atau Terminal.
- Ketik java **-version** untuk memastikan Java sudah terinstal dengan benar.
- Arahkan direktori aktif ke folder Fuseki yang sudah diekstrak.
5. Jalankan Server Fuseki
- Jalankan perintah **fuseki-server --update --mem /ds**.
- **--update** berarti operasi pembaruan pada dataset diizinkan.
- **--mem** berarti dataset disimpan di memori sementara.
- **/ds** adalah nama dataset.
- Jika berhasil, server akan aktif di alamat **http://localhost:3030**.
6. Akses Web Interface
- Buka browser dan masukkan alamat http://localhost:3030.
- Jika berhasil, halaman antarmuka Fuseki akan tampil dengan indikator status berwarna hijau.
  
### 📥 Memuat Data RDF ke Apache Jena Fuseki
1. Buat dataset baru melalui antarmuka web Apache Jena Fuseki.
2. Masukkan file RDF ke dalam dataset yang telah dibuat.
3. Jalankan query SPARQL untuk melakukan pencarian data.

### 💻 Panduan Penggunaan Aplikasi Streamlit
1. Menjalankan Aplikasi
- Jalankan aplikasi dengan mengetikkan perintah streamlit run **nama_projek.py**.
2. Mengakses Aplikasi
- Setelah server berjalan, buka browser dan masuk ke **http://localhost:8501**.
3. Cara Menggunakan Aplikasi
- Masukkan kata kunci pencarian yang ingin dicari (misalnya dalam Aksara Jawa, Bahasa Jawa, atau Bahasa Indonesia).
- Aplikasi akan menampilkan baris-baris yang mengandung kata kunci tersebut beserta hasil translasi, transliterasi, dan aksara Jawa-nya.
- Jika ingin melihat seluruh baris dari teks cerkak, scroll ke bagian bawah dan klik tombol "Tampilkan semua baris".

### 🔍 Contoh Hasil
1. Tampilan Utama
![image](https://github.com/user-attachments/assets/818d1a66-340b-46aa-8f25-0653b6e419ad)

2. Hasil Pencarian
- Jika yang dicari kata kuncinya Bahasa Indonesia
![Gambar WhatsApp 2025-06-17 pukul 20 38 20_4396e378](https://github.com/user-attachments/assets/798acee9-049c-4b3a-8c98-be85867aaecf)

- Jika yang dicari kata kuncinya Bahasa Jawa
![Gambar WhatsApp 2025-06-17 pukul 20 39 19_82f1fa07](https://github.com/user-attachments/assets/000188c4-40e6-4a7d-9923-6d2eda0605b9)

- Jika yang dicari kata kuncinya Aksara Jawa
![Gambar WhatsApp 2025-06-17 pukul 20 39 54_526a53c4](https://github.com/user-attachments/assets/fa19c498-c1c6-4aca-a7d7-946e73a89def)

- Menampilkan semua baris data cerkak
![Gambar WhatsApp 2025-06-17 pukul 20 37 38_718e68b9](https://github.com/user-attachments/assets/af563bcb-b89f-47e9-aecf-31ac18557376)

- Error jika tidak ada kata kunci yang dicari
![Gambar WhatsApp 2025-06-17 pukul 20 40 15_4d749c18](https://github.com/user-attachments/assets/db372db7-b1e0-49a4-890b-66f4489dec22)

### 👤 Tim Pengembang
- Vernandika Stanley Hansen (140810220031)
- Hosea Javier (140810220033)
- Adrian Jeremia Kurniawan (140810220047)

**Universitas Padjadjaran**  
**Fakultas MIPA - Program Studi Teknik Informatika**  
**2025**

---

*Dikembangkan untuk pelestarian warisan budaya dan aksara Jawa*
