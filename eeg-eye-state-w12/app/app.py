import streamlit as st

st.set_page_config(page_title="EEG Eye-State Monitoring (W12 Skeleton)", page_icon="🧠", layout="wide")

st.title("🧠 EEG Eye-State Intelligent Monitoring")
st.subheader("Kerangka Awal Dashboard (Progres Minggu 12 — Kelompok 14)")
st.info("Status: Tahap EDA, Preprocessing Anti-Leakage, dan Baseline LSTM (Model A).")

tab1, tab2, tab3 = st.tabs(["📊 Dataset Explorer (EDA)", "🤖 Baseline Model (Model A)", "🔮 Simulasi & Fuzzy (Tahap Lanjut)"])

with tab1:
    st.write("### Ringkasan Dataset & EDA")
    st.write("- **Sumber Data:** UCI EEG Eye State (ID 264) — 14 Channel EEG")
    st.write("- **Skema Split:** Kronologis 70% Train / 15% Validation / 15% Test")
    st.caption("Grafik boxplot, korelasi, dan distribusi target dari folder `artifacts/` akan ditampilkan di sini.")

with tab2:
    st.write("### Evaluasi Baseline LSTM (Model A)")
    st.write("- **Arsitektur:** `LSTM(32) -> Dropout(0.2) -> Dense(16, ReLU) -> Dense(1, Sigmoid)`")
    st.caption("Tabel hasil metrik Accuracy, Precision, Recall, dan F1-Score (mean ± std) akan ditampilkan di sini.")

with tab3:
    st.warning("Modul optimasi GA, PSO, dan Fuzzy Inference System akan diintegrasikan pada Minggu 13–15.")
