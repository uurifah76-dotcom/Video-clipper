import streamlit as st

# 1. PENGATURAN HALAMAN
st.set_page_config(
    page_title="Paidi Clipp.ai | AI Video Clipper Indonesia", 
    page_icon="✂️", 
    layout="centered"
)

# 2. CSS KUSTOM UNTUK TAMPILAN PROFESIONAL CLEAN & MODERN
st.markdown("""
    <style>
    /* Styling Dasar Halaman */
    .stApp {
        background-color: #ffffff;
        color: #111111;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Memperbaiki Top Bar / Header agar menyatu rapi */
    header[data-testid="stHeader"] {
        background-color: #ffffff !important;
        border-bottom: 1px solid #eaeaea;
    }
    
    /* Styling Kartu / Kotak Konten */
    .youclip-card {
        background-color: #fcfcfc;
        border: 1px solid #eaeaea;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
    }
    
    /* Tombol Utama */
    div.stButton > button {
        background-color: #4f46e5;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 14px 24px;
        font-weight: 600;
        width: 100%;
        font-size: 1rem;
        transition: all 0.2s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: #4338ca;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }

    /* Footer Profesional Multi-Kolom */
    .footer-container {
        background-color: #f9fafb;
        border-top: 1px solid #eaeaea;
        padding: 3rem 1rem 2rem 1rem;
        margin-top: 4rem;
        border-radius: 16px 16px 0 0;
    }
    
    .footer-heading {
        font-weight: 700;
        font-size: 1.05rem;
        color: #111111;
        margin-bottom: 1rem;
    }
    
    .footer-links {
        color: #4b5563;
        font-size: 0.95rem;
        line-height: 2;
        text-decoration: none;
    }

    /* Sembunyikan elemen bawaan Streamlit yang mengganggu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# ================= 3. KONTEN UTAMA WEBSITE =================

# Header Custom Nama Brand Baru di atas konten
st.markdown(
    "<div style='display: flex; align-items: center; justify-content: space-between; padding: 1rem 0; border-bottom: 1px solid #eaeaea; margin-bottom: 2rem;'>"
    "<div style='font-size: 1.25rem; font-weight: 800; color: #111111;'>✂️ Paidi Clipp<span style='color: #4f46e5;'>.ai</span></div>"
    "<div style='background-color: #4f46e5; color: white; border-radius: 50%; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; font-weight: bold;'>U</div>"
    "</div>",
    unsafe_allow_html=True
)

# Bagian Hero / Beranda Utama
st.markdown(
    "<h1 style='text-align: center; font-size: 2.5rem; font-weight: 800; letter-spacing: -1px;'>"
    "Ubah Video YouTube Panjang<br>Jadi <span style='color: #4f46e5; font-style: italic;'>Shorts Viral Otomatis</span>"
    "</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #4b5563; font-size: 1.1rem; margin-top: 1rem; margin-bottom: 2rem;'>"
    "Tempel link YouTube. AI kami akan memilih momen terbaik, memotongnya vertikal, "
    "dan menambahkan subtitle otomatis dalam hitungan menit."
    "</p>", 
    unsafe_allow_html=True
)

# Kotak Input Utama
st.markdown('<div class="youclip-card">', unsafe_allow_html=True)
url_input = st.text_input("Tempel Link YouTube", placeholder="https://www.youtube.com/watch?v=...")
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 Coba Sekarang Gratis"):
    if url_input:
        st.success("Menganalisis tautan video...")
    else:
        st.error("Silakan masukkan link YouTube terlebih dahulu.")
st.markdown(
    "<p style='text-align: center; color: #6b7280; font-size: 0.85rem; margin-top: 1rem;'>"
    "Tanpa kartu kredit. Gratis 1 kredit percobaan."
    "</p>", 
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)


# Bagian Penjelasan / Fitur Singkat
st.markdown("<br><h2 style='text-align: center; font-weight: 800;'>Cuma 3 Langkah.<br><i>Semudah Copy-Paste.</i></h2><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="youclip-card">', unsafe_allow_html=True)
    st.markdown("### 1️⃣ Tempel Link")
    st.write("Masukkan tautan video panjang dari YouTube ke dashboard Paidi Clipp.ai.")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="youclip-card">', unsafe_allow_html=True)
    st.markdown("### 2️⃣ AI Bekerja")
    st.write("Sistem otomatis mendeteksi bagian paling menarik dan lucu dari video.")
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="youclip-card">', unsafe_allow_html=True)
    st.markdown("### 3️⃣ Siap Upload")
    st.write("Unduh hasil klip vertikal lengkap dengan subtitle animasi siap viral.")
    st.markdown('</div>', unsafe_allow_html=True)


# Bagian Profil Founder / Cerita Singkat dengan Data Nama & Foto Baru
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="youclip-card" style="text-align: center;">', unsafe_allow_html=True)

# Placeholder Foto Profil Profesional menggunakan avatar random yang estetik
st.markdown(
    "<div style='display: flex; justify-content: center; margin-bottom: 1rem;'>"
    "<img src='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=300&q=80' "
    "style='width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #4f46e5;'>"
    "</div>", 
    unsafe_allow_html=True
)

st.markdown("### Halo, saya Usman cip4nky")
st.write(
    "“Saya membangun Paidi Clipp.ai karena satu alasan: Kreator hebat seperti Anda "
    "seharusnya fokus berkarya dan bicara, bukan membuang waktu mengurusi teknis editing yang membosankan.”"
)
st.markdown("<br><strong>Usman cip4nky</strong> · <em>Founder Paidi Clipp.ai</em>", unsafe_allow_html=True)
st.markdown("<p style='color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;'>📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ================= 4. FOOTER PROFESIONAL MULTI-KOLOM =================
st.markdown("""
    <div class="footer-container">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 2rem; max-width: 1000px; margin: 0 auto;">
            
            <!-- Kolom 1: Brand & Deskripsi -->
            <div style="flex: 2; min-width: 250px;">
                <div style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">
                    ✂️ Paidi Clipp.ai
                </div>
                <p style="color: #4b5563; font-size: 0.95rem; line-height: 1.5;">
                    AI video clipper Indonesia yang membantu kreator mengubah video YouTube panjang jadi klip viral untuk TikTok, Reels & Shorts.
                </p>
                <p style="color: #6b7280; font-size: 0.85rem; margin-top: 0.5rem;">
                    🏢 Kantor Pusat: Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139
                </p>
            </div>
            
            <!-- Kolom 2: Produk -->
            <div style="flex: 1; min-width: 140px;">
                <div class="footer-heading">Produk</div>
                <div class="footer-links">
                    Fitur Utama<br>
                    Cara Kerja<br>
                    Harga & Paket<br>
                    FAQ<br>
                    Tentang Kami
                </div>
            </div>
            
            <!-- Kolom 3: Legal -->
            <div style="flex: 1; min-width: 140px;">
                <div class="footer-heading">Legal</div>
                <div class="footer-links">
                    Kebijakan Privasi<br>
                    Ketentuan Layanan<br>
                    Kebijakan Pengembalian Dana
                </div>
            </div>
            
        </div>
        
        <hr style="border: none; border-top: 1px solid #eaeaea; margin: 2rem 0 1.5rem 0;">
        
        <div style="text-align: center; color: #6b7280; font-size: 0.9rem;">
            © 2026 Paidi Clipp.ai. Semua hak dilindungi.<br>
            Made with ❤️ in Indonesia
        </div>
    </div>
""", unsafe_allow_html=True)
