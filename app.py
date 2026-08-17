import streamlit as st

# Konfigurasi Halaman (Membuka mode lebar agar tidak terlihat kosong)
st.set_page_config(page_title="Paidi.ai - AI Video Studio", layout="wide", initial_sidebar_state="expanded")

# CSS Kustom untuk nuansa biru Malang yang elegan
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .card { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title("Paidi.ai Navigation")
menu = st.sidebar.radio("Menu", ["Beranda", "Kredit", "Affiliate", "Profil"])

# Konten Halaman
if menu == "Beranda":
    st.title("🚀 Paidi.ai Video Studio")
    st.subheader("Ubah video panjang menjadi klip viral otomatis.")
    
    with st.container():
        link = st.text_input("🔗 Masukkan Tautan YouTube:")
        
        # Layout Kolom agar rapat dan rapi
        col1, col2 = st.columns(2)
        with col1:
            durasi = st.slider("⏱️ Durasi Klip (detik)", 15, 60, 30)
            subtitle = st.checkbox("✅ Aktifkan Subtitle Otomatis")
        with col2:
            rasio = st.selectbox("📱 Rasio Aspek", ["9:16 (Vertikal)", "1:1 (Kotak)"])
            fokus = st.selectbox("🎯 Fokus Ekstraksi", ["AI Cerdas", "Transkrip Penuh"])
            
        if st.button("Mulai Proses AI"):
            st.info("Sistem sedang memproses video Anda di cloud...")
            # Panggil fungsi integrasi ke backend Google Colab di sini

elif menu == "Profil":
    st.header("👤 Profil Founder")
    st.write("Founder: **Usman (cip4nky)**")
    st.write("Alamat: Malang, Jawa Timur, Indonesia")
    st.write("Paidi.ai adalah solusi AI efisien untuk konten kreator masa kini.")

# Footer Korporat
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>© 2026 Paidi.ai - All Rights Reserved</div>", unsafe_allow_html=True)
