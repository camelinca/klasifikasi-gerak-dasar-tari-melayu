# Klasifikasi Gerak Dasar Tari Melayu menggunakan I3D
Aplikasi web untuk mengklasifikasikan gerak dasar tari Melayu secara real-time atau melalui unggahan video. Proyek ini menggunakan model deep learning I3D (Inflated 3D ConvNet).

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