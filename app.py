import streamlit as st

# 1. PENGATURAN HALAMAN
st.set_page_config(page_title="AI Video Clipper Pro | Studio", layout="wide")

# 2. CSS KUSTOM UNTUK TAMPILAN PROFESSIONAL SAAS & CORPORATE
st.markdown("""
    <style>
    :root {
        --bg-color: #0e1117;
        --card-bg: #161b22;
        --text-color: #c9d1d9;
        --accent-color: #2f81f7;
        --border-color: #30363d;
    }
    
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-color);
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Header & Branding */
    .corporate-header {
        background: linear-gradient(135deg, #1f6feb22 0%, #161b22 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        border: 1px solid var(--border-color);
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .brand-name {
        font-size: 2.8rem;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: -1px;
        margin-bottom: 0.2rem;
    }
    
    .brand-tagline {
        color: #8b949e;
        font-size: 1.1rem;
    }

    /* Kotak Kontainer Utama */
    .studio-card {
        background-color: var(--card-bg);
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        margin-bottom: 1.5rem;
    }
    
    /* Tombol Utama */
    div.stButton > button {
        background-color: var(--accent-color);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        width: 100%;
        transition: 0.2s;
    }
    
    div.stButton > button:hover {
        background-color: #388bfd;
        box-shadow: 0 0 12px rgba(47, 129, 247, 0.4);
    }

    /* Bagian Company Profile / Footer Korporat */
    .corporate-footer-section {
        background-color: var(--card-bg);
        padding: 2.5rem;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        margin-top: 4rem;
    }
    
    .footer-title {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    /* Sembunyikan Menu Bawaan Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# ================= 3. HEADER KORPORAT =================
st.markdown("""
    <div class="corporate-header">
        <div class="brand-name">⚡ CLIPPER<span style="color: #2f81f7;">.AI</span> STUDIO</div>
        <div class="brand-tagline">Platform Otomasi Konten Video Berbasis Kecerdasan Buatan Terdepan</div>
    </div>
""", unsafe_allow_html=True)


# ================= 4. NAVIGASI UTAMA (TABS) =================
menu_beranda, menu_kredit, menu_affiliate, menu_akun = st.tabs([
    "🏠 Beranda Studio", 
    "💳 Kredit & Harga", 
    "🤝 Program Affiliate", 
    "👤 Akun Saya"
])


# --- TAB 1: BERANDA ---
with menu_beranda:
    col_main, col_settings = st.columns([2, 1])
    
    with col_main:
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        st.markdown("### 🪄 Generator Klip Otomatis")
        url_input = st.text_input("Tempel Tautan YouTube:", placeholder="https://www.youtube.com/watch?v=...")
        
        c1, c2 = st.columns(2)
        with c1:
            start_t = st.time_input("Mulai Waktu")
        with c2:
            end_t = st.time_input("Selesai Waktu")
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Mulai Proses Clipping AI"):
            if url_input:
                st.success("Sistem sedang menganalisis video...")
            else:
                st.error("Silakan masukkan tautan video terlebih dahulu.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_settings:
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        st.markdown("### ⚙️ Pengaturan Output")
        durasi = st.selectbox("Durasi Target", ["15s - 30s", "30s - 90s (Viral)", "90s+"])
        subtitle = st.selectbox("Gaya Subtitle", ["Basic Clean", "Neon Pop", "Dynamic Cinematic"])
        rasio = st.selectbox("Rasio Aspek", ["9:16 (TikTok / Reels)", "16:9 (YouTube)", "1:1 (Square)"])
        resolusi = st.selectbox("Resolusi", ["720p HD", "1080p FHD", "4K Ultra"])
        st.markdown('</div>', unsafe_allow_html=True)


# --- TAB 2: KREDIT & HARGA ---
with menu_kredit:
    st.markdown('<div class="studio-card">', unsafe_allow_html=True)
    st.title("💳 Paket Berlangganan & Kredit")
    st.info("🎁 Akun baru mendapatkan saldo percobaan (Free Trial) otomatis.")
    st.metric(label="Saldo Kredit Anda", value="3 Kredit")
    st.markdown('</div>', unsafe_allow_html=True)


# --- TAB 3: AFFILIATE ---
with menu_affiliate:
    st.markdown('<div class="studio-card">', unsafe_allow_html=True)
    st.title("🤝 Program Kemitraan Affiliate")
    st.write("Dapatkan komisi pasif dengan merekomendasikan platform kami.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- TAB 4: AKUN ---
with menu_akun:
    st.markdown('<div class="studio-card">', unsafe_allow_html=True)
    st.title("👤 Manajemen Akun")
    st.text_input("Nama Pengguna", value="Creator Profesional")
    st.text_input("Email Terdaftar", value="creator@domain.com")
    st.markdown('</div>', unsafe_allow_html=True)


# ================= 5. BAGIAN PROFIL PERUSAHAAN DI BAWAH (CORPORATE FOOTER) =================
st.markdown("""
    <div class="corporate-footer-section">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 2rem;">
            <div style="flex: 1; min-width: 250px;">
                <div class="footer-title">Tentang Perusahaan</div>
                <p style="color: #8b949e; font-size: 0.95rem; line-height: 1.6;">
                    <b>PT Clipper Teknologi Indonesia</b> didirikan pada tahun 2026 dengan misi memberdayakan para pembuat konten (*content creators*) dan agensi digital di seluruh dunia melalui solusi teknologi kecerdasan buatan (*AI*) mutakhir untuk efisiensi produksi video vertikal.
                </p>
            </div>
            
            <div style="flex: 1; min-width: 200px;">
                <div class="footer-title">Legalitas & Dukungan</div>
                <p style="color: #8b949e; font-size: 0.95rem; line-height: 1.6;">
                    • Dukungan Teknis: support@clipperai.studio<br>
                    • Layanan Mitra Affiliate: partner@clipperai.studio<br>
                    • Status Server: 100% Operational (Cloud Node)
                </p>
            </div>
            
            <div style="flex: 1; min-width: 200px;">
                <div class="footer-title">Kantor Pusat</div>
                <p style="color: #8b949e; font-size: 0.95rem; line-height: 1.6;">
                    Sudirman Central Business District (SCBD)<br>
                    Jakarta Selatan, Indonesia<br>
                    © 2026 PT Clipper Teknologi Indonesia. All rights reserved.
                </p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
