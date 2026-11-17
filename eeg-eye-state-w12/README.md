# 🧠 EEG Eye-State Intelligent Monitoring — Progres Minggu 12

Repository ini berisi progres **Minggu 12** Tugas Besar Mata Kuliah Kecerdasan Buatan (TE2514031) oleh **Kelompok 14**, yang berfokus pada eksplorasi data (EDA), pembagian data kronologis (*anti-data leakage*), model *baseline* LSTM, serta kerangka awal aplikasi Streamlit.

> **Catatan:** Sistem ini merupakan prototipe pemantauan berbasis sinyal EEG dan **bukan alat diagnosis medis**.

---

## 👥 Anggota Kelompok 14
* **Alwan Akmal Larik** (04231009)
* **Nur Hayati S.** (04231069)
* **Tiara Alyssa** (04231087)
* **Wahyu Ianatul Mubasirin** (04231090)

---

## 📌 Ruang Lingkup Progres Minggu 12
Sesuai rencana kerja proyek, fokus pada tahap ini meliputi:
1. **Akuisisi & Pemahaman Dataset:** Mengunduh dataset UCI EEG Eye State (ID 264) dengan 14 channel (`AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4`) dan target `eyeDetection` (`0 = terbuka`, `1 = tertutup`).
2. **Preprocessing Anti-Data Leakage:**
   * Split kronologis **70% Train, 15% Validation, 15% Test** tanpa pengacakan (*shuffle*).
   * *Outlier clipping* menggunakan batas $Q1 - 3\cdot\text{IQR}$ dan $Q3 + 3\cdot\text{IQR}$ serta standardisasi (*mean* dan *std*) yang dihitung **hanya dari data train**.
   * Pembentukan *sliding window* berukuran `seq_len = 16` secara terpisah di tiap split.
3. **Exploratory Data Analysis (EDA):** Analisis statistik deskriptif, pengecekan *missing value*, distribusi kelas per split, *boxplot* sebelum & sesudah *clipping*, serta *heatmap* korelasi antar channel.
4. **Model A (Baseline LSTM):** Pelatihan arsitektur awal `LSTM(32) → Dropout(0.2) → Dense(16, ReLU) → Dense(1, Sigmoid)` pada seluruh 14 channel dengan 5 *random seed* berbeda.
5. **Kerangka Awal Streamlit:** Penyiapan struktur aplikasi web untuk integrasi model pada tahap berikutnya.

---

## 📁 Struktur Repository (Minggu 12)
```text
eeg-eye-state-w12/
├── README.md                  # Dokumentasi progres Minggu 12
├── requirements.txt           # Daftar library yang dibutuhkan
├── .gitignore                 # File pengecualian Git
├── notebooks/                 # Tempat file notebook (.ipynb) EDA & Baseline
├── artifacts/                 # Tempat hasil EDA (eda_summary.json, grafik PNG, baseline)
└── app/
    └── app.py                 # Kerangka awal (skeleton) dashboard Streamlit
```

---

## 🚀 Cara Menjalankan Kerangka Streamlit
```bash
# 1. Instal dependensi
pip install -r requirements.txt

# 2. Jalankan kerangka aplikasi
streamlit run app/app.py
```

---

## 🗓️ Rencana Tahap Selanjutnya
* **Minggu 13:** Implementasi *Genetic Algorithm* (GA) untuk seleksi channel EEG dan perbandingan Baseline vs GA+LSTM.
* **Minggu 14:** Implementasi *Particle Swarm Optimization* (PSO) untuk *tuning hyperparameter* dan perbandingan 4 konfigurasi model.
* **Minggu 15–16:** Integrasi *Fuzzy Inference System* (Mamdani), *deployment* online penuh, dan laporan akhir.
