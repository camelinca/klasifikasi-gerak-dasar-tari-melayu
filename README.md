# Klasifikasi Gerak Dasar Tari Melayu menggunakan I3D

Aplikasi web untuk mengklasifikasikan gerak dasar tari Melayu secara real-time atau melalui unggahan video. Proyek ini menggunakan model deep learning I3D (Inflated 3D ConvNet).

## 📜 Deskripsi Proyek
Proyek ini bertujuan untuk melestarikan budaya tari Melayu dengan memanfaatkan teknologi Artificial Intelligence. Model I3D dilatih untuk mengenali beberapa gerak dasar tari dan menampilkannya melalui antarmuka web yang interaktif.

## ✨ Fitur
- Klasifikasi video dari unggahan file.

## 💻 Teknologi yang Digunakan
- **Model:** I3D (Inflated 3D ConvNet) dengan TensorFlow/Keras.
- **Backend:** Flask (Python)
- **Frontend:** Next.js (React)
- **Deployment (jika ada):** Vercel, Heroku, dll.

## 📂 Struktur Proyek
Tentu, ini adalah panduan langkah demi langkah untuk mempublikasikan proyek klasifikasi gerak tari Melayu Anda di GitHub, dengan memperhatikan bahwa dataset Anda bersifat privat.

Ringkasan Proses
Prosesnya akan dibagi menjadi beberapa tahap utama:

Persiapan Lokal: Membersihkan proyek dan menyiapkan file .gitignore.

Membuat Repositori GitHub: Menyiapkan "rumah" untuk proyek Anda di GitHub.

Menangani File Model Besar (Git LFS): Menggunakan alat khusus agar file model Anda yang besar bisa diunggah.

Upload Proyek: Menggunakan perintah Git untuk mengunggah semua file Anda.

Membuat Dokumentasi (README.md): Menjelaskan proyek Anda kepada dunia.

Langkah 1: Persiapan di Komputer Lokal
Sebelum mengunggah, pastikan proyek Anda bersih dan terstruktur dengan baik.

Struktur Folder yang Direkomendasikan:
Buat satu folder utama untuk proyek Anda, lalu atur semua komponen di dalamnya seperti ini. Struktur ini sangat umum dan mudah dipahami oleh orang lain.

📂 klasifikasi-tari-melayu/
├── 📁 backend/         # Semua file Flask (app.py, requirements.txt, dll)
├── 📁 frontend/        # Semua file Next.js (pages/, components/, package.json, dll)
├── 📁 model/           # Tempat menyimpan file model Anda (misal: model_i3d.h5)
├── 📄 notebook.ipynb    # File Jupyter Notebook Anda
└── 📄 .gitignore       # File untuk mengabaikan file/folder yang tidak perlu di-upload
Bersihkan Jupyter Notebook (.ipynb):

Hapus Output: Buka notebook Anda, lalu klik Kernel > Restart & Clear Output. Ini akan menghapus semua hasil eksekusi sel, termasuk visualisasi atau path file dari dataset privat Anda.

Hapus Path Dataset: Pastikan tidak ada hardcoded path (misal: C:/Users/Anda/Documents/DatasetTari) di dalam kode. Ganti dengan placeholder seperti DATASET_PATH = 'path/to/your/private/dataset'. Beri komentar bahwa dataset tidak disertakan.

Buat File .gitignore:
Ini adalah file teks yang berisi daftar file atau folder yang akan diabaikan oleh Git dan tidak akan diunggah ke GitHub. Ini sangat penting. Buat file bernama .gitignore di dalam folder utama proyek (klasifikasi-tari-melayu/) dan isi dengan:

Cuplikan kode

# Python & Jupyter
__pycache__/
*.pyc
.ipynb_checkpoints
venv/
*.env

# Node.js / Next.js
node_modules/
.next/
npm-debug.log

# Dataset (PENTING!)
# Ganti 'nama_folder_dataset/' dengan nama folder dataset Anda yang sebenarnya
nama_folder_dataset/ 
*.csv
*.zip

# Lainnya
.DS_Store
Langkah 2: Buat Repositori Baru di GitHub
Buka GitHub dan login.

Klik ikon + di pojok kanan atas, lalu pilih New repository.

Repository name: Beri nama yang deskriptif, contoh: klasifikasi-gerak-tari-melayu-i3d.

Description: Beri deskripsi singkat, contoh: "Aplikasi web untuk klasifikasi gerak dasar tari Melayu menggunakan model I3D, dengan backend Flask dan frontend Next.js."

Pilih Public agar semua orang bisa melihatnya.

Centang kotak "Add a README file". Ini akan membuat file README.md awal untuk Anda.

Klik Create repository.

Langkah 3: Menangani File Model Besar dengan Git LFS (Large File Storage)
GitHub memiliki batas ukuran file sekitar 100MB. File model machine learning seringkali lebih besar dari itu. Solusinya adalah menggunakan Git LFS.

Install Git LFS: Unduh dan install dari situs resminya.

Aktifkan Git LFS di Proyek Anda:

Buka terminal atau Command Prompt.

Masuk ke folder utama proyek Anda (cd path/to/klasifikasi-tari-melayu).

Jalankan perintah ini hanya sekali:

Bash

git lfs install
Lacak File Model: Beri tahu Git LFS untuk menangani file model Anda. Jika model Anda berekstensi .h5, jalankan:

Bash

git lfs track "model/*.h5" 
Perintah ini akan membuat file bernama .gitattributes. Jangan hapus file ini, karena file inilah yang memberitahu Git untuk menggunakan LFS pada file model Anda.

Langkah 4: Upload Proyek ke GitHub 🚀
Sekarang saatnya menghubungkan folder lokal Anda dengan repositori di GitHub.

Clone Repositori:
Di halaman repositori GitHub Anda, klik tombol hijau < > Code, salin URL HTTPS.

Buka terminal (di luar folder proyek Anda), dan jalankan:

Bash

git clone <URL_YANG_ANDA_SALIN>
Ini akan membuat folder baru dengan nama repositori Anda (misal: klasifikasi-gerak-tari-melayu-i3d).

Pindahkan File:
Salin semua file dan folder proyek Anda (backend/, frontend/, model/, notebook.ipynb, .gitignore, .gitattributes) ke dalam folder yang baru saja di-clone.

Upload dengan Perintah Git:
Buka terminal di dalam folder hasil clone tersebut, lalu jalankan perintah-perintah berikut secara berurutan:

Cek status file:

Bash

git status 
(Anda akan melihat semua file baru berwarna merah).

Tambahkan semua file untuk di-commit:

Bash

git add .
Simpan perubahan (commit):

Bash

git commit -m "Initial commit: Menambahkan struktur proyek klasifikasi tari"
Kirim ke GitHub:

Bash

git push origin main
(Mungkin Anda perlu memasukkan username dan password/token GitHub Anda).

Setelah selesai, refresh halaman repositori GitHub Anda. Semua file seharusnya sudah muncul!

Langkah 5: Buat Dokumentasi README.md yang Baik
File README.md adalah wajah dari proyek Anda. Edit file ini langsung di GitHub atau di komputer Anda lalu push lagi.

Berikut adalah template yang bisa Anda gunakan. Salin dan tempelkan ke README.md Anda, lalu sesuaikan isinya.

Markdown

# Klasifikasi Gerak Dasar Tari Melayu menggunakan I3D

Aplikasi web untuk mengklasifikasikan gerak dasar tari Melayu secara real-time atau melalui unggahan video. Proyek ini menggunakan model deep learning I3D (Inflated 3D ConvNet).

![Demo GIF atau Screenshot Aplikasi Anda](link_ke_gambar_demo.gif)

## 📜 Deskripsi Proyek
Proyek ini bertujuan untuk melestarikan budaya tari Melayu dengan memanfaatkan teknologi Artificial Intelligence. Model I3D dilatih untuk mengenali beberapa gerak dasar tari dan menampilkannya melalui antarmuka web yang interaktif.

## ✨ Fitur
- Klasifikasi video dari unggahan file.
- (Opsional) Klasifikasi real-time menggunakan webcam.
- Antarmuka pengguna yang responsif dan modern.

## 💻 Teknologi yang Digunakan
- **Model:** I3D (Inflated 3D ConvNet) dengan TensorFlow/Keras.
- **Backend:** Flask (Python)
- **Frontend:** Next.js (React)
- **Deployment (jika ada):** Vercel, Heroku, dll.

## 📂 Struktur Proyek
.
├── dance-motion-detector-api/ # Server Flask & API
├── dance-motion-detector/     # Aplikasi Klien Next.js
├── model/                     # File model .h5 
├── notebook.ipynb             # Notebook untuk development model
└── README.md

## 🚀 Instalasi & Cara Menjalankan
### **1. Backend (Flask)**
```bash
# Masuk ke folder backend
cd dance-motion-detector-api

python -m venv venv
source venv/bin/activate 

# Install dependensi
pip install -r requirements.txt

# Jalankan server
flask run 
atau 
phyton app.py
```
### **2. Frontend (Next.js)**
```bash
# Buka terminal baru, masuk ke folder frontend
cd frontend

# Install dependensi
npm install

# Jalankan aplikasi dev
npm run dev
```

Dataset bersifat privat dan tidak disertakan dalam repositori ini untuk melindungi hak cipta dan privasi.