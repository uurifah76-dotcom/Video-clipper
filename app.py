import streamlit as st

# 1. PENGATURAN HALAMAN
st.set_page_config(
    page_title="Paidi Clipp.ai | Next-Gen AI Video Studio", 
    page_icon="⚡", 
    layout="centered"
)

# 2. CSS KUSTOM - TEMA BIRU KHAS MALANG (AREMA BLUE & NAVY ELEGAN)
st.markdown("""
    <style>
    /* Tema Biru Khas Malang (Kombinasi Biru Arema, Navy Gelap & Sentuhan Putih Clean) */
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
    .custom-panel {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
    }
    
    /* Tombol Interaktif Warna Biru Khas Malang & Aksen Cerah */
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

    /* Footer Eksklusif */
    .footer-area {
        background-color: #060913;
        border-top: 1px solid #1d3557;
        padding: 3rem 1.5rem 2rem 1.5rem;
        margin-top: 4rem;
        border-radius: 20px 20px 0 0;
    }
    
    .footer-title {
        font-weight: 700;
        font-size: 1.1rem;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    
    .footer-text {
        color: #93c5fd;
        font-size: 0.95rem;
        line-height: 2.2;
    }
    </style>
""", unsafe_allow_html=True)


# ================= 3. STRUKTUR UTAMA HALAMAN =================

# Navigasi Atas / Brand Identitas Baru
st.markdown(
    "<div style='display: flex; align-items: center; justify-content: space-between; padding: 1rem 0; border-bottom: 1px solid #1d3557; margin-bottom: 2rem;'>"
    "<div style='font-size: 1.3rem; font-weight: 900; color: #ffffff; letter-spacing: -0.5px;'>⚡ Paidi Clipp<span style='color: #60a5fa;'>.ai</span></div>"
    "<div style='background: linear-gradient(135deg, #1d4ed8, #3b82f6); color: white; border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.1rem;'>U</div>"
    "</div>",
    unsafe_allow_html=True
)

# Hero Section (Judul & Tagline Baru yang Orisinal)
st.markdown(
    "<h1 style='text-align: center; font-size: 2.4rem; font-weight: 800; letter-spacing: -1px; color: #ffffff; line-height: 1.3;'>"
    "Ekstraksi Konten Sinematik<br>Dari Video Panjang Menjadi <span style='color: #60a5fa; font-style: italic;'>Reels Daya Tarik Tinggi</span>"
    "</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #93c5fd; font-size: 1.05rem; margin-top: 1rem; margin-bottom: 2rem;'>"
    "Sistem kecerdasan buatan otonom kami memindai durasi penuh, mengidentifikasi segmen paling bernilai tinggi, "
    "serta meraciknya dalam format vertikal siap edar."
    "</p>", 
    unsafe_allow_html=True
)

# Area Input Tautan
st.markdown('<div class="custom-panel">', unsafe_allow_html=True)
url_input = st.text_input("Tautan Sumber Media (YouTube URL)", placeholder="https://www.youtube.com/watch?v=...")
st.markdown("<br>", unsafe_allow_html=True)
if st.button("✨ Eksekusi Analisis Otonom"):
    if url_input:
        st.success("Mesin neural sedang memproses stream video...")
    else:
        st.error("Harap masukkan tautan video yang valid pada kolom di atas.")
st.markdown(
    "<p style='text-align: center; color: #60a5fa; font-size: 0.85rem; margin-top: 1rem;'>"
    "Akses uji coba terbuka • Tanpa instrumen penagihan otomatis."
    "</p>", 
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)


# Bagian Alur Kerja (3 Pilar Sistem)
st.markdown("<br><h2 style='text-align: center; font-weight: 800; color: #ffffff;'>Arsitektur 3 Langkah Kerja</h2><br>", unsafe_allow_html=True)

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown('<div class="custom-panel">', unsafe_allow_html=True)
    st.markdown("### 📥 1. Ingest Data")
    st.write("Kirimkan tautan arsip video berdurasi panjang ke dalam sistem komputasi cloud kami.")
    st.markdown('</div>', unsafe_allow_html=True)
with col_b:
    st.markdown('<div class="custom-panel">', unsafe_allow_html=True)
    st.markdown("### 🧠 2. Deep Scanning")
    st.write("Algoritma machine learning menyeleksi puncak impresi, emosi, dan inti narasi terbaik.")
    st.markdown('</div>', unsafe_allow_html=True)
with col_c:
    st.markdown('<div class="custom-panel">', unsafe_allow_html=True)
    st.markdown("### 🚀 3. Instant Export")
    st.write("Unduh kompilasi video vertikal beresolusi tinggi dengan sinkronisasi teks dinamis.")
    st.markdown('</div>', unsafe_allow_html=True)


# Profil Founder & Identitas Wilayah (Orisinal & Khas)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="custom-panel" style="text-align: center;">', unsafe_allow_html=True)

st.markdown(
    "<div style='display: flex; justify-content: center; margin-bottom: 1rem;'>"
    "<img src='https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80' "
    "style='width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #3b82f6;'>"
    "</div>", 
    unsafe_allow_html=True
)

st.markdown("### Dibalik Layar Bersama Usman cip4nky")
st.write(
    "“Saya mendedikasikan pengembangan Paidi Clipp.ai untuk meruntuhkan hambatan produksi media. "
    "Visi kami sederhana: biarkan teknologi otonom menangani kerumitan teknis, sehingga kreator "
    "bisa sepenuhnya mendedikasikan energi untuk substansi materi dan kreativitas.”"
)
st.markdown("<br><strong>Usman cip4nky</strong> · <em>Chief Executive Officer & Founder</em>", unsafe_allow_html=True)
st.markdown("<p style='color: #60a5fa; font-size: 0.9rem; margin-top: 0.5rem;'>📍 Pusat Operasional: Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ================= 4. FOOTER KORPORAT MULTI-KOLOM =================
st.markdown("""
    <div class="footer-area">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 2rem; max-width: 1000px; margin: 0 auto;">
            
            <!-- Kolom Identitas -->
            <div style="flex: 2; min-width: 260px;">
                <div style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin-bottom: 0.5rem;">
                    ⚡ Paidi Clipp.ai
                </div>
                <p style="color: #93c5fd; font-size: 0.95rem; line-height: 1.6;">
                    Infrastruktur perangkat lunak berbasis kecerdasan buatan terdepan di Indonesia untuk otomatisasi repurposing video jangka panjang.
                </p>
                <p style="color: #60a5fa; font-size: 0.85rem; margin-top: 0.75rem;">
                    🏢 Kantor Pusat: Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139
                </p>
            </div>
            
            <!-- Kolom Direktori -->
            <div style="flex: 1; min-width: 140px;">
                <div class="footer-title">Eksplorasi</div>
                <div class="footer-text">
                    Modul Inti<br>
                    Alur Kerja<br>
                    Skema Lisensi<br>
                    Pusat Bantuan<br>
                    Perseroan
                </div>
            </div>
            
            <!-- Kolom Kepatuhan Hukum -->
            <div style="flex: 1; min-width: 140px;">
                <div class="footer-title">Regulasi</div>
                <div class="footer-text">
                    Kebijakan Privasi Data<br>
                    Perjanjian Pengguna<br>
                    Sanggahan Tanggung Jawab
                </div>
            </div>
            
        </div>
        
        <hr style="border: none; border-top: 1px solid #1d3557; margin: 2.5rem 0 1.5rem 0;">
        
        <div style="text-align: center; color: #60a5fa; font-size: 0.9rem;">
            © 2026 PT Paidi Teknologi Indonesia. Hak Cipta Dilindungi Undang-Undang.<br>
            Engineered with excellence from Malang, Indonesia.
        </div>
    </div>
""", unsafe_allow_html=True)
