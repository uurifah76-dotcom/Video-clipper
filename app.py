import streamlit as st

# Konfigurasi Halaman (Tata letak vertikal profesional & ringkas)
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

# 1. Halaman Beranda & Studio (Landing Page Ringkas & Bersih)
if menu == "Beranda & Studio":
    
    # --- SLOGAN PROMOSI UTAMA ---
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-size: 30px; margin-bottom: 8px;">⚡ Paidi.ai Video Studio</h1>
            <h3 style="color: #4da6ff; margin-top: 0; font-size: 18px;">Ekstraksi Konten Sinematik: Dari Video Panjang Menjadi Reels Daya Tinggi 🔗</h3>
            <p style="font-size: 14px; opacity: 0.9; max-width: 600px; margin: 0 auto;">
                Sistem kecerdasan buatan otonom kami memindai durasi penuh, mengidentifikasi segmen paling bernilai tinggi, serta meraciknya dalam format vertikal siap edar secara instan.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # --- PANEL STUDIO UTAMA ---
    st.markdown("### 🛠️ Studio Pemrosesan Konten")
    
    # Banner Promo Pengguna Baru (Tetap Tampil di Atas Form)
    st.markdown("""
    <div class="promo-banner">
        <span style="font-size: 14px; font-weight: bold; color: #4da6ff;">🎁 PROMO SPESIAL PENGGUNA BARU:</span>
        <p style="font-size: 13px; margin: 4px 0 0 0; opacity: 0.95;">Nikmati <strong>Ekstra 5 Sesi Gratis Tambahan</strong> + Diskon 50% untuk peningkatan paket pertama Anda hari ini!</p>
    </div>
    """, unsafe_allow_html=True)

    # Form Studio (Kotak kosong di bawah banner promo sudah dibersihkan total)
    with st.container():
        st.markdown('<div class="card" style="margin-top: 0px;">', unsafe_allow_html=True)
        
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

    # --- LANGKAH-LANGKAH PENGGUNAAN (HOW IT WORKS) ---
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

    # --- PROFIL FOUNDER (Posisi di Tengah, "Founder of" Usman Shidiq) ---
    st.markdown("""
    <div class="profile-card">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&h=150&fit=crop&crop=faces" style="width: 90px; height: 90px; border-radius: 50%; object-fit: cover; border: 2px solid #007bff; margin-bottom: 12px; display: block; margin-left: auto; margin-right: auto;" alt="Founder">
        <h3 style="margin: 0; font-size: 18px; text-align: center;">Usman Shidiq</h3>
        <p style="color: #4da6ff; font-size: 13px; margin-top: 2px; margin-bottom: 12px; text-align: center;">Founder of Paidi.ai</p>
        <p style="font-size: 14px; opacity: 0.9; line-height: 1.6; text-align: center; margin-bottom: 8px;">
            "Paidi.ai lahir dari sebuah keresahan pribadi melihat betapa melelahkannya proses manual memotong video podcast atau rekaman panjang menjadi klip-klip pendek vertikal yang siap viral. Waktu kreatif kreator seringkali habis di ruang edit yang repetitif.<br><br>
            Saat ini, <strong>Paidi.ai masih berada di tahap rintisan awal (early-stage startup)</strong>, di mana kami terus merintis, belajar, dan berinovasi bersama komunitas kreator di Indonesia untuk menghadirkan solusi teknologi otomasi video yang efisien, mudah digunakan, dan terjangkau."
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- INFORMASI PERUSAHAAN & KORPORAT ---
    st.markdown("### 🏢 Informasi Korporat & Kontak Resmi")
    st.markdown("""
    <div class="card" style="border-left: 4px solid #007bff;">
        <p style="font-size: 13px; line-height: 1.6; margin-bottom: 10px;">
            <strong>PT Paidi.ai Group</strong> didirikan pada tahun <strong>2026</strong> di Kota Malang, Jawa Timur. Kami berkomitmen membangun fondasi perangkat lunak rintisan berbasis kecerdasan buatan untuk revolusi konten digital Indonesia.
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 12px 0;">
        <p style="font-size: 13px; margin: 0; opacity: 0.9;">
            📍 <strong>Alamat Kantor:</strong> Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139<br>
            📞 <strong>WhatsApp Korporat:</strong> 083853413171<br>
            ✉️ <strong>Layanan Gmail Resmi:</strong> support@paidi.ai / usmancipanky@gmail.com<br>
            📱 <strong>Media Sosial:</strong> TikTok & Instagram (@Paidi.ai.idn)
        </p>
    </div>
    """, unsafe_allow_html=True)

# Halaman Kredit & Paket
elif menu == "Kredit & Paket":
    st.markdown("# 💳 Kredit & Paket Berlangganan")
    st.markdown("---")
    st.write("Sisa sesi pemrosesan AI Anda saat ini adalah **5 / 10 Sesi** (Status Rintisan Awal).")
    st.button("Top Up Sesi Tambahan")

# Halaman Program Affiliate
elif menu == "Program Affiliate":
    st.markdown("# 🤝 Program Affiliate Paidi.ai")
    st.markdown("---")
    st.write("Dapatkan komisi menarik dengan membagikan tautan referral eksklusif Anda ke sesama kreator.")
    st.code("https://paidi.ai/ref/usman_shidiq")

# Halaman Akun & Profil
elif menu == "Akun & Profil":
    st.markdown("# 👤 Akun & Profil Founder")
    st.markdown("---")
    st.markdown("### Halo, saya Usman Shidiq")
    st.write('"Sebagai pengembang yang merintis Paidi.ai dari Malang, visi kami adalah mem
