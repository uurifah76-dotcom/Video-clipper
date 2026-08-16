import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="AI Video Clipper Pro", layout="wide")

# CSS Kustom untuk Tampilan Profesional
st.markdown("""
    <style>
    /* Mengubah warna latar belakang dan font */
    .stApp { background-color: #f8f9fa; }
    
    /* Styling Tombol agar terlihat lebih Modern */
    div.stButton > button:first-child {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    
    /* Mengatur Judul agar lebih elegan */
    h1 { color: #1e1e2e; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Menghilangkan Menu Bawaan Streamlit agar terlihat seperti Web Perusahaan */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Header Website
st.markdown("<h1 style='text-align: center;'>🎬 AI Video Clipper Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6c757d;'>Ubah video panjang Anda menjadi viral dengan kekuatan AI</p>", unsafe_allow_html=True)

# Membuat Navigasi Menu
menu_beranda, menu_kredit, menu_affiliate, menu_akun = st.tabs([
    "🏠 Beranda", "💳 Kredit & Paket", "🤝 Affiliate", "👤 Akun"
])

with menu_beranda:
    st.subheader("Buat Klip Anda Sekarang")
    url = st.text_input("Tempel Link YouTube Anda di sini:")
    
    # Sidebar dipindah ke kolom agar lebih menyatu dengan desain
    col_main, col_sidebar = st.columns([2, 1])
    
    with col_sidebar:
        st.markdown("### ⚙️ Pengaturan Video")
        durasi = st.selectbox("Durasi Klip", ["15-30s", "30-90s", "90s+"])
        sub = st.selectbox("Template Subtitle", ["Basic", "Neon Pop", "Minimalist"])
        rasio = st.selectbox("Rasio", ["9:16 (TikTok/Reels)", "16:9 (YouTube)"])
        resolusi = st.selectbox("Resolusi", ["720p", "1080p", "4K"])
        
    with col_main:
        st.write("---")
        if st.button("🚀 Mulai Clipping Otomatis"):
            st.success("Analisis AI sedang berjalan...")

# Tambahkan Footer Profesional
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #adb5bd; font-size: 12px;'>
    © 2026 AI Video Clipper Studio. All Rights Reserved.
    </div>
""", unsafe_allow_html=True)
