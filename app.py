import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Paidi.ai - AI Video Studio",
    layout="centered",
    initial_sidebar_state="auto"
)

# Sidebar Navigasi Asli
st.sidebar.markdown("### ⚡ Paidi.ai Menu")
st.sidebar.markdown("**Navigasi Utama**")
menu = st.sidebar.radio(
    "Pilih Menu", 
    ["Beranda & Studio", "Kredit & Paket", "Program Affiliate", "Akun & Profil"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Status Sistem:** Rintisan Awal")
st.sidebar.markdown("**Kredit Anda:** 5 / 10 Sesi")
st.sidebar.markdown("📍 Malang, Indonesia")

# Konten Beranda & Studio
if menu == "Beranda & Studio":
    st.markdown("# ⚡ Paidi.ai")
    st.markdown("---")
    
    st.markdown("## Ekstraksi Konten Sinematik\nDari Video Panjang Menjadi *Reels* Daya Tarik Tinggi 🔗")
    st.markdown("Sistem kecerdasan buatan otonom kami memindai durasi penuh, mengidentifikasi segmen paling bernilai tinggi, serta meraciknya dalam format vertikal siap edar.")
    
    st.markdown("### Tautan Sumber Media (YouTube URL)")
    link = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...", label_visibility="collapsed")
    
    st.markdown("---")
    
    durasi = st.selectbox("Durasi Target Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"])
    subtitle = st.selectbox("Gaya Subtitle / Headline", ["Dinamis Alex Hormozi Style", "Minimalis Clean", "Tanpa Subtitle"])
    rasio = st.selectbox("Rasio Aspek Video", ["9:16 (Vertical Reels/TikTok)", "1:1 (Square)", "16:9 (Horizontal)"])
    resolusi = st.selectbox("Resolusi Ekspor", ["1080p (Full HD)", "720p (HD)"])
    estimasi = st.selectbox("Estimasi Durasi Proses", ["⚡ Kilat (~3-5 Menit)", "Standard"])
    fokus = st.selectbox("Fokus Ekstraksi Konten", ["🔥 Deteksi Menyeluruh (AI Multi-Analisis Semua Kategori)", "Fokus Hook Utama"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ Eksekusi Analisis Otonom", type="primary"):
        if link:
            st.info("Menghubungkan ke server YouTube untuk membaca metadata video...")
            st.success("Video Berhasil Dideteksi!")
            st.markdown("""
            ### 📌 Informasi Metadata Video:
            * **Judul:** Contoh Judul Video Panjang YouTube
            * **Kanal:** Nama Kreator
            * **Durasi Asli:** 46 menit 8 detik
            """)
        else:
            st.warning("⚠️ Silakan masukkan tautan YouTube terlebih dahulu!")

# Konten Kredit & Paket
elif menu == "Kredit & Paket":
    st.markdown("# 💳 Kredit & Paket Berlangganan")
    st.markdown("---")
    st.write("Sisa sesi pemrosesan AI Anda saat ini adalah **5 / 10 Sesi**.")
    st.button("Top Up Sesi Tambahan")

# Konten Program Affiliate
elif menu == "Program Affiliate":
    st.markdown("# 🤝 Program Affiliate Paidi.ai")
    st.markdown("---")
    st.write("Dapatkan komisi menarik dengan membagikan tautan referral eksklusif Anda ke sesama kreator.")
    st.code("https://paidi.ai/ref/usman_cip4nky")

# Konten Akun & Profil
elif menu == "Akun & Profil":
    st.markdown("# 👤 Akun & Profil")
    st.markdown("---")
    st.markdown("### Halo, saya Usman cip4nky")
    st.write('"Saya merintis pengembangan Paidi.ai untuk membantu kreator menyederhanakan alur kerja produksi media. Sebagai platform baru, kami terus belajar dan bertumbuh bersama komunitas untuk memberikan solusi terbaik."')
    
    st.markdown("**Usman cip4nky** · *Founder of Usman cip4nky*")
    st.markdown("📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139")
    st.markdown("📞 Hotline: 083853413171 | ✉️ Email: support@paidi.ai")

# Footer Perusahaan
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 13px;'>
    <strong>Paidi.ai</strong><br>
    Infrastruktur perangkat lunak rintisan berbasis kecerdasan buatan untuk otomatisasi repurposing video di Indonesia.<br><br>
    🏢 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139<br>
    📞 WhatsApp/Telp: 083853413171 | ✉️ support@paidi.ai<br>
    📱 TikTok & Instagram: @Paidi.ai.idn<br><br>
    © 2026 PT Paidi.ai Group. Didirikan 2026. Hak Cipta Dilindungi Undang-Undang.<br>
    Engineered with excellence from Malang, Indonesia.
</div>
""", unsafe_allow_html=True)
