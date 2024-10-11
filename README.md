# Implementasi Hill Cipher untuk File Gambar

Repositori ini berisi sebuah proyek tugas akhir pada mata kuliah kriptografi untuk menerapkan algoritma Hill Cipher pada enkripsi dan dekripsi file gambar. Implementasi dilakukan dengan menggunakan bahasa pemrograman Python dan framework Flask untuk pengembangan web serta melakukan prompting dengan ChatGPT untuk membantu proses perhitungan algoritma dengan piksel gambar pada ketiga channel-nya.

## Daftar Isi
- [Instalasi](#instalasi)
  - [1. Membuat Virtual Environment](#1-membuat-virtual-environment)
  - [2. Menginstal Library yang Dibutuhkan](#2-menginstal-library-yang-dibutuhkan)
  - [3. Menjalankan Aplikasi](#3-menjalankan-aplikasi)

## Instalasi

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah di bawah ini:

### 1. Membuat Virtual Environment

Pastikan Anda sudah memiliki Python 3.7+ terinstal. Buatlah virtual environment untuk proyek ini agar dependensi terisolasi:

```bash
# Di macOS/Linux
python3 -m venv env

# Di Windows
python -m venv env
```

Aktifkan virtual environment:

```bash
# Di macOS/Linux
source env/bin/activate

# Di Windows
env\Scripts\activate
```

### 2. Menginstal Library yang Dibutuhkan

Setelah virtual environment aktif, instal library yang dibutuhkan dengan menggunakan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi

Untuk menjalankan dashboard, gunakan perintah berikut:

```bash
python app.py
```

Perintah ini akan menjalankan web dari enkripsi dan dekripsi file gambar pada lokal server. Buka URL yang diberikan di browser Anda untuk mengakses web tersebut dan diakhir server tersebut tambahkan "/enc" maupun "/dec" untuk mengakses aplikasi enkripsi dan dekripsi file gambar pada web tersebut.
