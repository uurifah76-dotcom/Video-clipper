import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Paidi.ai - AI Video Studio", layout="wide", initial_sidebar_state="expanded")

# CSS Kustom untuk Tampilan Elegan
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigasi Lengkap
st.sidebar.title("Paidi.ai Navigation")
menu = st.sidebar.radio("Menu", ["Beranda", "Kredit", "Affiliate", "Profil", "Tentang Perusahaan"])

# Halaman Beranda
if menu == "Beranda":
    st.title("🚀 Paidi.ai Video Studio")
    st.subheader("Ubah video panjang menjadi klip viral otomatis.")
    
    link = st.text_input("🔗 Masukkan Tautan YouTube:", placeholder="https://www.youtube.com/watch?v=...")
    
    durasi = st.slider("⏱️ Durasi Klip (detik)", 15, 60, 30)
    subtitle = st.checkbox("✅ Aktifkan Subtitle Otomatis", value=True)
    rasio = st.selectbox("📱 Rasio Aspek", ["9:16 (Vertikal)", "1:1 (Kotak)", "16:9 (Horizontal)"])
    fokus = st.selectbox("🎯 Fokus Ekstraksi", ["AI Cerdas", "Transkrip Penuh"])
    
    if st.button("Mulai Proses AI"):
        if link:
            st.info("Sistem sedang memproses video Anda di cloud...")
        else:
            st.warning("⚠️ Silakan masukkan tautan YouTube terlebih dahulu!")

# Halaman Kredit
elif menu == "Kredit":
    st.header("💳 Saldo Kredit Anda")
    st.write("Sisa Kredit Anda: **150 Kredit Tersedia**")
    st.button("Top Up Kredit")

# Halaman Affiliate
elif menu == "Affiliate":
    st.header("🤝 Program Affiliate Paidi.ai")
    st.write("Bagikan tautan referral Anda dan dapatkan komisi dari setiap pengguna baru.")
    st.code("https://paidi.ai/ref/usman_cip4nky")

# Halaman Profil
elif menu == "Profil":
    st.header("👤 Profil Pengguna & Founder")
    st.write(f"**Founder:** Usman (cip4nky)")
    st.write(f"**Lokasi Kantor:** Malang, Jawa Timur, Indonesia")
    st.write("Platform AI video studio untuk kreator konten profesional.")

# Halaman Tentang Perusahaan
elif menu == "Tentang Perusahaan":
    st.header("🏢 Tentang Paidi.ai")
    st.write("Paidi.ai adalah perusahaan teknologi berbasis kecerdasan buatan yang berfokus pada otomatisasi konten video pendek (Reels, TikTok, Shorts).")
    st.write("Kami berkomitmen menghadirkan solusi pengeditan tercepat dan efisien bagi kreator di seluruh Indonesia.")

# Footer Korporat
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>© 2026 Paidi.ai - All Rights Reserved</div>", unsafe_allow_html=True)
