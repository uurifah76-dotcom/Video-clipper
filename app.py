import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Paidi.ai - AI Video Studio",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS Kustom untuk Tampilan Elegan & Rata Tengah
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .promo-banner {
        background: linear-gradient(135deg, rgba(0, 123, 255, 0.25), rgba(40, 167, 69, 0.25));
        border: 1px solid rgba(0, 123, 255, 0.5);
        padding: 14px 18px;
        border-radius: 10px;
        margin-bottom: 15px;
        text-align: center;
    }
    .profile-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(0, 123, 255, 0.4);
        padding: 25px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.2em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.markdown("### ⚡ Paidi.ai Menu")
menu = st.sidebar.radio(
    "Navigasi Utama", 
    ["Beranda & Studio", "Kredit & Paket", "Program Affiliate", "Akun & Profil"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Status Sistem:** 🚀 Rintisan Awal (Early Stage)")
st.sidebar.markdown("**Kredit Anda:** 5 / 10 Sesi")
st.sidebar.markdown("📍 Malang, Indonesia")

# 1. Halaman Beranda & Studio
if menu == "Beranda & Studio":
    
    # --- JUDUL UTAMA STUDIO ---
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-size: 30px; margin-bottom: 8px;">⚡ Paidi.ai Video Studio</h1>
            <h3 style="color: #4da6ff; margin-top: 0; font-size: 18px;">Ekstraksi Konten Sinematik: Dari Video Panjang Menjadi Reels Daya Tinggi 🔗</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # --- PANEL STUDIO UTAMA ---
    st.markdown("### 🛠️ Studio Pemrosesan Konten")
    
    # Banner Promo Pengguna Baru
    st.markdown("""
    <div class="promo-banner">
        <span style="font-size: 14px; font-weight: bold; color: #4da6ff;">🎁 PROMO SPESIAL PENGGUNA BARU:</span>
        <p style="font-size: 13px; margin: 4px 0 0 0; opacity: 0.95;">Nikmati <strong>Ekstra 5 Sesi Gratis Tambahan</strong> + Diskon 50% untuk peningkatan paket pertama Anda hari ini!</p>
    </div>
    """, unsafe_allow_html=True)

    # Form Studio Input (Menggunakan struktur native Streamlit agar aman dari error sintaks HTML)
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 🔗 Tautan Sumber Media (YouTube URL)")
        link = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...", label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            durasi = st.selectbox("Durasi Target Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"])
            subtitle = st.selectbox("Gaya Subtitle / Headline", ["Dinamis Alex Hormozi Style", "Minimalis Clean", "Tanpa Subtitle"])
            rasio = st.selectbox("Rasio Aspek Video", ["9:16 (Vertical Reels/TikTok)", "1:1 (Square)", "16:9 (Horizontal)"])
        with col2:
            resolusi = st.selectbox("Resolusi Ekspor", ["1080p (Full HD)", "720p (HD)"])
            estimasi = st.selectbox("Estimasi Durasi Proses", ["⚡ Kilat (~3-5 Menit)", "Standard"])
            fokus = st.selectbox("Fokus Ekstraksi Konten", ["🔥 Deteksi Menyeluruh (AI Multi-Analisis)", "Fokus Hook Utama"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button
