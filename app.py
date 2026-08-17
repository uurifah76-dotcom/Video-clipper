import streamlit as st

# Konfigurasi Halaman (Lebar agar layout dua kolom tertata pas)
st.set_page_config(
    page_title="Paidi.ai - AI Video Studio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Kustom agar kartu transparan dan elegan sesuai desain asli
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigasi Asli
st.sidebar.markdown("### ⚡ Paidi.ai Menu")
menu = st.sidebar.radio(
    "Navigasi Utama", 
    ["Beranda & Studio", "Kredit & Paket", "Program Affiliate", "Akun & Profil"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Status Sistem:** Rintisan Awal")
st.sidebar.markdown("**Kredit Anda:** 5 / 10 Sesi")
st.sidebar.markdown("📍 Malang, Indonesia")

# Konten Beranda & Studio (Struktur Dua Kolom Persis Seperti Asli)
if menu == "Beranda & Studio":
    col_kiri, col_kanan = st.columns([1.1, 0.9], gap="large")
    
    with col_kiri:
        st.markdown("### ⚡ Paidi.ai")
        st.markdown("---")
        
        # Kartu Sambutan & Profil Founder di Kiri Atas
        st.markdown("""
        <div class="card">
            <h4>Halo, saya Usman cip4nky</h4>
            <p style="font-size: 14px; opacity: 0.9;">"Saya merintis pengembangan Paidi.ai untuk membantu kreator menyederhanakan alur kerja produksi media. Sebagai platform baru, kami terus belajar dan bertumbuh bersama komunitas untuk memberikan solusi terbaik."</p>
            <p><strong>Usman cip4nky</strong> · <span style="font-size: 13px; opacity: 0.8;">Founder of Usman cip4nky</span></p>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <p style="font-size: 12px; opacity: 0.8; margin-bottom:0;">
                📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Form Input YouTube URL
        st.markdown("#### 🔗 Tautan Sumber Media (YouTube URL)")
        link = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...", label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Pengaturan Studio
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
            else:
                st.warning("⚠️ Silakan masukkan tautan YouTube terlebih dahulu!")

    with col_kanan:
        # Sisi Kanan: Kartu Informasi Fitur Unggulan (Persis Seperti Gambar Asli)
        st.markdown("""
        <div class="card" style="text-align: center; background: rgba(0, 123, 255, 0.1);">
            <h2 style="margin-bottom: 10px;">Ekstraksi Konten Sinematik</h2>
            <h3 style="color: #4da6ff; margin-top: 0;">Dari Video Panjang Menjadi Reels Daya Tarik Tinggi 🔗</h3>
            <p style="font-size: 14px; opacity: 0.9;">Sistem kecerdasan buatan otonom kami memindai durasi penuh, mengidentifikasi segmen paling bernilai tinggi, serta meraciknya dalam format vertikal siap edar.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h4>1. Ingest Data</h4>
            <p style="font-size: 13px; opacity: 0.8; margin-bottom: 0;">Kirimkan tautan arsip video berdurasi panjang ke dalam sistem komputasi cloud kami.</p>
        </div>
        
        <div class="card">
            <h4>2. Deep Scanning</h4>
            <p style="font-size: 13px; opacity: 0.8; margin-bottom: 0;">Algoritma machine learning menyeleksi puncak impresi, emosi, dan inti narasi terbaik.</p>
        </div>
        
        <div class="card" style="border-left: 4px solid #007bff;">
            <p style="font-size: 12px; margin: 0; opacity: 0.8;">Infrastruktur perangkatan lunak rintisan berbasis kecerdasan buatan untuk otomatisasi repurposing video di Indonesia.</p>
            <p style="font-size: 12px; margin-top: 8px; opacity: 0.8; margin-bottom: 0;">
                🏢 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139<br>
                📞 WhatsApp: 083853413171 | ✉️ support@paidi.ai<br>
                📱 TikTok & Instagram: @Paidi.ai.idn
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
    
    st.markdown("**Usman cip4nky** · *Founder of Usman cip4nky*")
    st.markdown("📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139")
    st.markdown("📞 Hotline: 083853413171 | ✉️ Email: support@paidi.ai")

# Footer Perusahaan
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 12px;'>
    <strong>Paidi.ai</strong> — Infrastruktur perangkat lunak rintisan berbasis kecerdasan buatan untuk otomatisasi repurposing video di Indonesia.<br>
    © 2026 PT Paidi.ai Group. Didirikan 2026. Hak Cipta Dilindungi Undang-Undang. Engineered in Malang, Indonesia.
</div>
""", unsafe_allow_html=True)
