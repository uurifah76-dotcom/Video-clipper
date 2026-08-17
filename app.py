import streamlit as st

# Konfigurasi Halaman (Mode standard vertikal agar rapi seperti website korporat besar)
st.set_page_config(
    page_title="Paidi.ai - AI Video Studio",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS Kustom untuk Tampilan Profesional Ala Perusahaan SaaS Besar
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    .hero-box {
        background: rgba(0, 123, 255, 0.15);
        border: 1px solid rgba(0, 123, 255, 0.3);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
    }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 24px;
        border-radius: 12px;
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
st.sidebar.markdown("**Status Sistem:** Versi 1.0 Live")
st.sidebar.markdown("**Kredit Anda:** 5 / 10 Sesi")
st.sidebar.markdown("📍 Malang, Indonesia")

# 1. Halaman Beranda & Studio (Struktur Vertikal Profesional)
if menu == "Beranda & Studio":
    
    # --- BAGIAN 1: HERO SECTION / PROMOSI UTAMA DI PALING ATAS ---
    st.markdown("""
    <div class="hero-box">
        <h1 style="font-size: 32px; margin-bottom: 10px;">⚡ Paidi.ai Video Studio</h1>
        <h3 style="color: #4da6ff; margin-top: 0; font-size: 20px;">Ekstraksi Konten Sinematik: Dari Video Panjang Menjadi Reels Daya Tarik Tinggi 🔗</h3>
        <p style="font-size: 15px; opacity: 0.9; max-width: 600px; margin: 0 auto;">
            Sistem kecerdasan buatan otonom kami memindai durasi penuh, mengidentifikasi segmen paling bernilai tinggi, serta meraciknya dalam format vertikal siap edar secara instan.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # --- BAGIAN 2: KOLOM MENU / PANEL STUDIO UTAMA ---
    st.markdown("### 🛠️ Studio Pemrosesan Konten")
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
        if st.button("✨ Eksekusi Analisis Otonom", type="primary"):
            if link:
                st.info("Menghubungkan ke server YouTube untuk membaca metadata video...")
                st.success("Video Berhasil Dideteksi!")
            else:
                st.warning("⚠️ Silakan masukkan tautan YouTube terlebih dahulu!")
                
        st.markdown('</div>', unsafe_allow_html=True)

    # --- BAGIAN 3: LANGKAH-LANGKAH PENGGUNAAN (HOW IT WORKS) ---
    st.markdown("### 📋 Cara Kerja Sistem Otonom Kami")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("""
        <div class="card">
            <h4>1. Ingest Data</h4>
            <p style="font-size: 14px; opacity: 0.8; margin-bottom: 0;">Kirimkan tautan arsip video berdurasi panjang ke dalam sistem komputasi cloud kami secara aman dan cepat.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_f2:
        st.markdown("""
        <div class="card">
            <h4>2. Deep Scanning</h4>
            <p style="font-size: 14px; opacity: 0.8; margin-bottom: 0;">Algoritma machine learning menyeleksi puncak impresi, emosi, dan inti narasi terbaik secara presisi.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- BAGIAN 4: PROFIL FOUNDER & ALASAN BERDIRINYA PAIDI.AI (PROMOSI HALUS) ---
    st.markdown("### 💡 Cerita Di Balik Paidi.ai")
    st.markdown("""
    <div class="card">
        <h4 style="color: #4da6ff;">Mengapa Paidi.ai Hadir untuk Kreator Indonesia?</h4>
        <p style="font-size: 14px; opacity: 0.9; line-height: 1.6;">
            "Saya merintis pengembangan <strong>Paidi.ai</strong> berawal dari keresahan melihat betapa melelahkannya proses manual memotong video panjang menjadi klip pendek yang menarik perhatian penonton. Banyak kreator potensial kehabisan waktu di ruang edit alih-alih fokus memikirkan ide konten.<br><br>
            Oleh karena itu, Paidi.ai didirikan untuk merevolusi alur kerja produksi media—menghadirkan solusi otomatisasi cerdas yang efisien, cepat, dan terjangkau bagi siapa saja yang ingin bersaing di era video vertikal."
        </p>
        <p style="margin-top: 15px; margin-bottom: 0;"><strong>Usman cip4nky</strong> · <span style="font-size: 13px; opacity: 0.8;">Founder & CEO of Paidi.ai</span></p>
    </div>
    """, unsafe_allow_html=True)

    # --- BAGIAN 5: INFORMASI PERUSAHAAN & KORPORAT BESAR ---
    st.markdown("### 🏢 Informasi Korporat & Kontak Resmi")
    st.markdown("""
    <div class="card" style="border-left: 4px solid #007bff;">
        <p style="font-size: 13px; line-height: 1.6; margin-bottom: 10px;">
            <strong>PT Paidi.ai Group</strong> didirikan pada tahun <strong>2026</strong> di Kota Malang, Jawa Timur. Kami berkomitmen menjadi pelopor infrastruktur perangkat lunak rintisan berbasis kecerdasan buatan untuk otomatisasi <em>repurposing</em> video di Indonesia.
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 12px 0;">
        <p style="font-size: 13px; margin: 0; opacity: 0.9;">
            📍 <strong>Alamat Kantor Pusat:</strong> Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139<br>
            📞 <strong>Telepon / WhatsApp Korporat:</strong> 083853413171<br>
            ✉️ <strong>Layanan Pelanggan (Gmail):</strong> support@paidi.ai / usmancipanky@gmail.com<br>
            📱 <strong>Media Sosial Resmi:</strong> TikTok & Instagram (@Paidi.ai.idn)
        </p>
    </div>
    """, unsafe_allow_html=True)

# Halaman Kredit & Paket
elif menu == "Kredit & Paket":
    st.markdown("# 💳 Kredit & Paket Berlangganan")
    st.markdown("---")
    st.write("Sisa sesi pemrosesan AI Anda saat ini adalah **5 / 10 Sesi**.")
    st.button("Top Up Sesi Tambahan")

# Halaman Program Affiliate
elif menu == "Program Affiliate":
    st.markdown("# 🤝 Program Affiliate Paidi.ai")
    st.markdown("---")
    st.write("Dapatkan komisi menarik dengan membagikan tautan referral eksklusif Anda ke sesama kreator.")
    st.code("https://paidi.ai/ref/usman_cip4nky")

# Halaman Akun & Profil
elif menu == "Akun & Profil":
    st.markdown("# 👤 Akun & Profil")
    st.markdown("---")
    st.markdown("### Halo, saya Usman cip4nky")
    st.write('"Saya merintis pengembangan Paidi.ai untuk membantu kreator menyederhanakan alur kerja produksi media. Sebagai platform baru, kami terus belajar dan bertumbuh bersama komunitas untuk memberikan solusi terbaik."')
    
    st.markdown("**Usman cip4nky** · *Founder of Paidi.ai*")
    st.markdown("📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139")
    st.markdown("📞 Hotline: 083853413171 | ✉️ Email: support@paidi.ai")

# Footer Korporat Standar Internasional
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 12px; line-height: 1.5;'>
    <strong>Paidi.ai</strong> — Infrastruktur perangkat lunak rintisan berbasis kecerdasan buatan untuk otomatisasi repurposing video di Indonesia.<br>
    🏢 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139 | 📞 083853413171 | ✉️ support@paidi.ai<br>
    © 2026 PT Paidi.ai Group. Didirikan 2026. Hak Cipta Dilindungi Undang-Undang. Engineered in Malang, Indonesia.
</div>
""", unsafe_allow_html=True)
