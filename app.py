import streamlit as st

# 1. PENGATURAN HALAMAN
st.set_page_config(
    page_title="Paidi.ai | Next-Gen AI Video Studio", 
    page_icon="⚡", 
    layout="centered"
)

# 2. CSS KUSTOM - TEMA BIRU KHAS MALANG & UI BERSIH
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
    
    /* Kartu Konten Kustom yang Bersih & Rapi */
    .card-box {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.4);
    }
    
    /* Badge Slogan Atas Input */
    .slogan-badge {
        background: rgba(59, 130, 246, 0.15);
        border: 1px solid #3b82f6;
        color: #93c5fd;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        text-align: center;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 1rem;
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

    /* Footer Korporat Aman Tanpa HTML Bocor */
    .footer-container {
        background-color: #060913;
        border-top: 1px solid #1d3557;
        padding: 2.5rem 1.5rem 2rem 1.5rem;
        margin-top: 4rem;
        border-radius: 20px 20px 0 0;
    }
    </style>
""", unsafe_allow_html=True)


# ================= 3. STRUKTUR UTAMA HALAMAN =================

# Navigasi Atas / Brand Identitas
st.markdown(
    "<div style='display: flex; align-items: center; justify-content: space-between; padding: 1rem 0; border-bottom: 1px solid #1d3557; margin-bottom: 2rem;'>"
    "<div style='font-size: 1.3rem; font-weight: 900; color: #ffffff; letter-spacing: -0.5px;'>⚡ Paidi<span style='color: #60a5fa;'>.ai</span></div>"
    "<div style='background: linear-gradient(135deg, #1d4ed8, #3b82f6); color: white; border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.1rem;'>U</div>"
    "</div>",
    unsafe_allow_html=True
)

# Hero Section (Judul & Tagline Orisinal)
st.markdown(
    "<h1 style='text-align: center; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px; color: #ffffff; line-height: 1.3;'>"
    "Ekstraksi Konten Sinematik<br>Dari Video Panjang Menjadi <span style='color: #60a5fa; font-style: italic;'>Reels Daya Tarik Tinggi</span>"
    "</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #93c5fd; font-size: 1rem; margin-top: 1rem; margin-bottom: 2rem;'>"
    "Sistem kecerdasan buatan otonom kami memindai durasi penuh, mengidentifikasi segmen paling bernilai tinggi, "
    "serta meraciknya dalam format vertikal siap edar."
    "</p>", 
    unsafe_allow_html=True
)

# Area Input Tautan dengan Panel & Slogan Pengisi (Menghilangkan Kolom Kosong)
with st.container():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    
    # Bagian atas sebelum input link diisi badge/slogan informatif agar tidak kosong
    st.markdown(
        '<div class="slogan-badge">'
        '🚀 <strong>Teknologi Neural V3.2 Aktif:</strong> Pemrosesan Lebih Cepat & Akurasi Klip 99.8%'
        '</div>', 
        unsafe_allow_html=True
    )
    
    url_input = st.text_input("Tautan Sumber Media (YouTube URL)", placeholder="https://www.youtube.com/watch?v=...")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("✨ Eksekusi Analisis Otonom"):
        if url_input:
            st.success("Mesin neural sedang memproses stream video...")
        else:
            st.error("Harap masukkan tautan video yang valid pada kolom di atas.")
            
    st.markdown(
        "<p style='text-align: center; color: #60a5fa; font-size: 0.85rem; margin-top: 1rem;'>"
        "Akses uji coba terbuka • Didukung oleh PT Paidi.ai Group (Malang)"
        "</p>", 
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)


# Bagian Alur Kerja (3 Pilar Sistem)
st.markdown("<br><h2 style='text-align: center; font-weight: 800; color: #ffffff; font-size: 1.5rem;'>Arsitektur 3 Langkah Kerja</h2><br>", unsafe_allow_html=True)

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
    "“Saya mendedikasikan pengembangan Paidi.ai untuk meruntuhkan hambatan produksi media. "
    "Visi kami sederhana: biarkan teknologi otonom menangani kerumitan teknis, sehingga kreator "
    "bisa sepenuhnya mendedikasikan energi untuk substansi materi dan kreativitas.”"
    "</p>"
    "<strong style='color: #ffffff;'>Usman cip4nky</strong> · <em style='color: #60a5fa;'>Founder of Usman cip4nky</em>"
    "<p style='color: #60a5fa; font-size: 0.85rem; margin-top: 0.8rem;'>📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139</p>"
    "<p style='color: #93c5fd; font-size: 0.85rem; margin-top: 0.3rem;'>📞 Hotline: 083853413171 | ✉️ Email: support@paidi.ai</p>"
    '</div>',
    unsafe_allow_html=True
)


# ================= 4. FOOTER KORPORAT AMAN (MENGGUNAKAN KOLOM NATIVE STREAMLIT) =================
st.markdown('<div class="footer-container">', unsafe_allow_html=True)

f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown("### ⚡ Paidi.ai")
    st.markdown(
        "<span style='color: #93c5fd; font-size: 0.9rem;'>Infrastruktur perangkat lunak berbasis kecerdasan buatan terdepan di Indonesia untuk otomatisasi repurposing video jangka panjang.</span>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<span style='color: #60a5fa; font-size: 0.85rem;'>🏢 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139<br>📞 083853413171<br>✉️ support@paidi.ai</span>", 
        unsafe_allow_html=True
    )

with f_col2:
    st.markdown("### Eksplorasi")
    st.markdown(
        "<span style='color: #93c5fd; font-size: 0.9rem; line-height: 1.8;'>Modul Inti<br>Alur Kerja<br>Skema Lisensi<br>Pusat Bantuan</span>", 
        unsafe_allow_html=True
    )

with f_col3:
    st.markdown("### Sosial Media")
    st.markdown(
        "<span style='color: #93c5fd; font-size: 0.9rem; line-height: 1.8;'>TikTok: @Paidi.ai.idn<br>Instagram: @Paidi.ai.idn</span>", 
        unsafe_allow_html=True
    )
    st.markdown("### Regulasi")
    st.markdown(
        "<span style='color: #93c5fd; font-size: 0.9rem; line-height: 1.8;'>Kebijakan Privasi<br>Perjanjian Layanan</span>", 
        unsafe_allow_html=True
    )

st.markdown("<hr style='border: none; border-top: 1px solid #1d3557; margin: 2rem 0 1rem 0;'>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: #60a5fa; font-size: 0.85rem;'>"
    "© 2026 PT Paidi.ai Group. Didirikan 2026. Hak Cipta Dilindungi Undang-Undang.<br>"
    "Engineered with excellence from Malang, Indonesia."
    "</div>", 
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
