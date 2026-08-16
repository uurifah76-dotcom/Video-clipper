import streamlit as st
import os
import yt_dlp

# 1. PENGATURAN HALAMAN
st.set_page_config(
    page_title="Paidi.ai | Next-Gen AI Video Studio", 
    page_icon="⚡", 
    layout="centered"
)

# 2. CSS KUSTOM - TEMA BIRU KHAS MALANG & INPUT GELAP MENYATU
st.markdown("""
    <style>
    /* Tema Biru Khas Malang (Navy Gelap & Biru Arema Clean) */
    .stApp {
        background-color: #0b132b;
        color: #e0f2fe;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header Navbar */
    header[data-testid="stHeader"] {
        background-color: #0b132b !important;
        border-bottom: 1px solid #1d3557;
    }
    
    /* Kartu Konten Kustom */
    .card-box {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.4);
    }
    
    /* Styling Input Teks agar Menyatu dengan Tema Gelap */
    div[data-baseweb="input"] {
        background-color: #1c2541 !important;
        border: 1px solid #3a506b !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="input"] input {
        color: #e0f2fe !important;
        background-color: transparent !important;
    }
    
    /* Styling Selectbox agar Menyatu dengan Tema Gelap */
    div[data-baseweb="select"] > div {
        background-color: #1c2541 !important;
        color: #e0f2fe !important;
        border-radius: 12px !important;
        border: 1px solid #3a506b !important;
    }
    
    /* Label warna teks input/select agar kontras & jelas */
    .stTextInput label, .stSelectbox label {
        color: #93c5fd !important;
        font-weight: 500;
    }
    
    /* Tombol Interaktif */
    div.stButton > button {
        background: linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 14px 24px;
        font-weight: 600;
        width: 100%;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(29, 78, 216, 0.4);
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 100%, #60a5fa 0%);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
    }

    /* Footer Korporat */
    .footer-box {
        background-color: #060913;
        border-top: 1px solid #1d3557;
        padding: 2.5rem 1.5rem 2rem 1.5rem;
        margin-top: 4rem;
        border-radius: 20px 20px 0 0;
    }
    </style>
""", unsafe_allow_html=True)


# ================= 3. SIDEBAR NAVIGASI & AKUN =================
with st.sidebar:
    st.markdown("### ⚡ Paidi.ai Menu")
    menu_pilihan = st.radio(
        "Navigasi Utama", 
        ["Beranda & Studio", "Kredit & Paket", "Program Affiliate", "Akun & Profil"]
    )
    
    st.markdown("---")
    st.markdown("**Status Sistem:** Rintisan Awal")
    st.markdown("**Kredit Anda:** 5 / 10 Sesi")
    st.markdown("📍 Malang, Indonesia")


# ================= 4. KONTEN UTAMA BERDASARKAN NAVIGASI =================

if menu_pilihan == "Beranda & Studio":
    # Navigasi Atas Sederhana
    st.markdown(
        "<div style='display: flex; align-items: center; justify-content: space-between; padding: 1rem 0; border-bottom: 1px solid #1d3557; margin-bottom: 2rem;'>"
        "<div style='font-size: 1.3rem; font-weight: 900; color: #ffffff; letter-spacing: -0.5px;'>⚡ Paidi<span style='color: #60a5fa;'>.ai</span></div>"
        "<div style='background: linear-gradient(135deg, #1d4ed8, #3b82f6); color: white; border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.1rem;'>U</div>"
        "</div>",
        unsafe_allow_html=True
    )

    # Hero Section
    st.markdown(
        "<h1 style='text-align: center; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px; color: #ffffff; line-height: 1.3;'>"
        "Ekstraksi Konten Sinematik<br>Dari Video Panjang Menjadi <span style='color: #60a5fa; font-style: italic;'>Reels Daya Tarik Tinggi</span>"
        "</h1>", 
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center; color: #93c5fd; font-size: 1rem; margin-top: 1rem; margin-bottom: 2.5rem;'>"
        "Sistem kecerdasan buatan otonom kami memindai durasi penuh, mengidentifikasi segmen paling bernilai tinggi, "
        "serta meraciknya dalam format vertikal siap edar."
        "</p>", 
        unsafe_allow_html=True
    )

    # Area Input Tautan YouTube
    url_input = st.text_input("Tautan Sumber Media (YouTube URL)", placeholder="https://www.youtube.com/watch?v=...")
    st.markdown("<br>", unsafe_allow_html=True)

    # Panel Kustomisasi Template & Ekstraksi
    with st.expander("⚙️ Pengaturan Template & Kustomisasi Ekstraksi", expanded=True):
        col_opt1, col_opt2 = st.columns(2)
        with col_opt1:
            target_durasi = st.selectbox("Durasi Target Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)", "Mendalam (60-90 detik)"])
            gaya_subtitle = st.selectbox("Gaya Subtitle / Headline", ["Dinamis Alex Hormozi Style", "Minimalis Clean", "Bold Cinematic"])
            aspek_rasio = st.selectbox("Rasio Aspek Video", ["9:16 (Vertical Reels/TikTok)", "1:1 (Square Feed)", "16:9 (Landscape)"])
        with col_opt2:
            resolusi_video = st.selectbox("Resolusi Ekspor", ["1080p (Full HD)", "720p (Standard HD)"])
            estimasi_waktu = st.selectbox("Estimasi Durasi Proses", ["⚡ Kilat (~3-5 Menit)", "🛡️ Standar Teliti (~5-10 Menit)"])
            filter_fokus = st.selectbox(
                "Fokus Ekstraksi Konten", 
                [
                    "🔥 Deteksi Menyeluruh (AI Multi-Analisis Semua Kategori)", 
                    "🚀 Potensi Viral Tertinggi (Algoritma Hook & Retensi)", 
                    "⭐ Golden Moment / Puncak Emosi Terbaik", 
                    "💡 Argumen Kuat / Edukasi Mendalam", 
                    "😄 Humor & Segmen Menghibur"
                ]
            )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✨ Eksekusi Analisis Otonom"):
        if url_input:
            st.info(f"🔄 Menghubungkan ke server YouTube untuk membaca metadata video...")
            
            # Menggunakan yt-dlp untuk mendeteksi informasi video secara nyata
            ydl_opts = {'quiet': True, 'skip_download': True}
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url_input, download=False)
                    video_title = info_dict.get('title', 'Tidak diketahui')
                    video_duration = info_dict.get('duration', 0)
                    channel_name = info_dict.get('uploader', 'Tidak diketahui')
                
                st.success(f"✅ Video Berhasil Dideteksi!")
                st.markdown(f"""
                <div class="card-box" style="margin-top: 1rem;">
                    <h4 style="color: #60a5fa; margin-bottom: 0.5rem;">📌 Informasi Metadata Video:</h4>
                    <p style="color: #e0f2fe; margin: 0.2rem 0;"><strong>Judul:</strong> {video_title}</p>
                    <p style="color: #e0f2fe; margin: 0.2rem 0;"><strong>Kanal:</strong> {channel_name}</p>
                    <p style="color: #e0f2fe; margin: 0.2rem 0;"><strong>Durasi Asli:</strong> {video_duration // 60} menit {video_duration % 60} detik</p>
                    <p style="color: #93c5fd; margin-top: 0.5rem; font-size: 0.9rem;">🤖 AI sedang memproses mode <strong>[{filter_fokus}]</strong> untuk memotong klip dengan format {aspek_rasio}...</p>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Gagal membaca tautan YouTube. Pastikan link yang dimasukkan benar dan publik. (Detail: {e})")
        else:
            st.error("Harap masukkan tautan video YouTube yang valid terlebih dahulu.")

    st.markdown(
        "<p style='text-align: center; color: #60a5fa; font-size: 0.85rem; margin-top: 1rem; margin-bottom: 3rem;'>"
        "Pratinjau sistem rintisan awal • Dikembangkan di Malang, Indonesia"
        "</p>", 
        unsafe_allow_html=True
    )

    # Bagian Alur Kerja (3 Pilar Sistem)
    st.markdown("<h2 style='text-align: center; font-weight: 800; color: #ffffff; font-size: 1.5rem; margin-bottom: 1.5rem;'>Arsitektur 3 Langkah Kerja</h2>", unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(
            '<div class="card-box">'
            '<h4 style="color: #ffffff; margin-bottom: 0.5rem;">📥 1. Ingest Data</h4>'
            '<p style="color: #93c5fd; font-size: 0.9rem; margin: 0;">Kirimkan tautan arsip video berdurasi panjang ke dalam sistem komputasi cloud kami.</p>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col_b:
        st.markdown(
            '<div class="card-box">'
            '<h4 style="color: #ffffff; margin-bottom: 0.5rem;">🧠 2. Deep Scanning</h4>'
            '<p style="color: #93c5fd; font-size: 0.9rem; margin: 0;">Algoritma machine learning menyeleksi puncak impresi, emosi, dan inti narasi terbaik.</p>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col_c:
        st.markdown(
            '<div class="card-box">'
            '<h4 style="color: #ffffff; margin-bottom: 0.5rem;">🚀 3. Instant Export</h4>'
            '<p style="color: #93c5fd; font-size: 0.9rem; margin: 0;">Unduh kompilasi video vertikal beresolusi tinggi dengan sinkronisasi teks dinamis.</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    # Profil Founder & Identitas Wilayah
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<div class="card-box" style="text-align: center;">'
        "<div style='display: flex; justify-content: center; margin-bottom: 1rem;'>"
        "<img src='https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80' "
        "style='width: 90px; height: 90px; border-radius: 50%; object-fit: cover; border: 3px solid #3b82f6;'>"
        "</div>"
        "<h3 style='color: #ffffff; margin-bottom: 0.5rem;'>Halo, saya Usman cip4nky</h3>"
        "<p style='color: #e0f2fe; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;'>"
        "“Saya merintis pengembangan Paidi.ai untuk membantu kreator menyederhanakan alur kerja produksi media. "
        "Sebagai platform baru, kami terus belajar dan bertumbuh bersama komunitas untuk memberikan solusi terbaik.”"
        "</p>"
        "<strong style='color: #ffffff;'>Usman cip4nky</strong> · <em style='color: #60a5fa;'>Founder of Usman cip4nky</em>"
        "<p style='color: #60a5fa; font-size: 0.85rem; margin-top: 0.8rem;'>📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139</p>"
        "<p style='color: #93c5fd; font-size: 0.85rem; margin-top: 0.3rem;'>📞 Hotline: 083853413171 | ✉️ Email: support@paidi.ai</p>"
        '</div>',
        unsafe_allow_html=True
    )

elif menu_pilihan == "Kredit & Paket":
    st.markdown("<h2 style='color: white;'>💎 Pilihan Paket & Kredit Paidi.ai</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #93c5fd;'>Pilih skema fleksibel yang sesuai dengan kebutuhan produksi konten Anda.</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="card-box">'
            '<h3 style="color: #ffffff;">Paket Rintisan (Gratis)</h3>'
            '<p style="color: #93c5fd;">Cocok untuk uji coba fitur dasar.</p>'
            '<h4 style="color: #60a5fa;">Rp 0 / bulan</h4>'
            '<p style="color: #e0f2fe; font-size: 0.9rem;">• 10 Sesi Ekstraksi per Bulan<br>• Resolusi 720p<br>• Watermark Paidi.ai</p>'
            '</div>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<div class="card-box">'
            '<h3 style="color: #ffffff;">Paket Kreator Pro</h3>'
            '<p style="color: #93c5fd;">Untuk kreator aktif & agensi media.</p>'
            '<h4 style="color: #60a5fa;">Rp 99.000 / bulan</h4>'
            '<p style="color: #e0f2fe; font-size: 0.9rem;">• Ekstraksi Tanpa Batas<br>• Resolusi 1080p Full HD<br>• Tanpa Watermark<br>• Prioritas Antrian Server</p>'
            '</div>',
            unsafe_allow_html=True
        )

elif menu_pilihan == "Program Affiliate":
    st.markdown("<h2 style='color: white;'>🤝 Program Affiliate Paidi.ai</h2>", unsafe_allow_html=True)
    st.markdown(
        '<div class="card-box">'
        '<h3 style="color: #ffffff;">Dapatkan Komisi 30%</h3>'
        '<p style="color: #93c5fd; line-height: 1.6;">'
        'Ajak rekan kreator, editor, atau pebisnis digital menggunakan Paidi.ai. '
        'Dapatkan komisi pasif setiap kali referral Anda bergabung dengan paket berbayar kami.'
        '</p>'
        '<p style="color: #60a5fa; font-weight: bold;">Link Affiliate Anda: https://paidi.ai/ref/usman-malang</p>'
        '</div>',
        unsafe_allow_html=True
    )

elif menu_pilihan == "Akun & Profil":
    st.markdown("<h2 style='color: white;'>👤 Akun & Pengaturan Pengguna</h2>", unsafe_allow_html=True)
    st.markdown(
        '<div class="card-box">'
        '<h3 style="color: #ffffff;">Informasi Pengguna</h3>'
        '<p style="color: #e0f2fe;"><strong>Nama:</strong> Usman cip4nky</p>'
        '<p style="color: #e0f2fe;"><strong>Email:</strong> support@paidi.ai</p>'
        '<p style="color: #e0f2fe;"><strong>Lokasi Utama:</strong> Ruko WOW Sawojajar, Kota Malang</p>'
        '<p style="color: #e0f2fe;"><strong>Status Langganan:</strong> Akun Uji Coba (Free Tier)</p>'
        '</div>',
        unsafe_allow_html=True
    )


# ================= 5. FOOTER KORPORAT BERSIH & AMAN =================
st.markdown(
    """
    <div class="footer-box">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <div style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin-bottom: 0.5rem;">⚡ Paidi.ai</div>
            <p style="color: #93c5fd; font-size: 0.9rem; line-height: 1.6; margin-bottom: 1rem;">
                Infrastruktur perangkat lunak rintisan berbasis kecerdasan buatan untuk otomatisasi repurposing video di Indonesia.
            </p>
            <p style="color: #60a5fa; font-size: 0.85rem; margin-bottom: 1.5rem;">
                🏢 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139<br>
                📞 WhatsApp/Telp: 083853413171 | ✉️ support@paidi.ai<br>
                📱 TikTok & Instagram: @Paidi.ai.idn
            </p>
            <hr style="border: none; border-top: 1px solid #1d3557; margin: 1.5rem 0;">
            <p style="color: #60a5fa; font-size: 0.85rem; margin: 0;">
                © 2026 PT Paidi.ai Group. Didirikan 2026. Hak Cipta Dilindungi Undang-Undang.<br>
                Engineered with excellence from Malang, Indonesia.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )
