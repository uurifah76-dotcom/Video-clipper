import streamlit as st

st.set_page_config(page_title="AI Video Clipper Pro", layout="wide")

# Membuat Navigasi Menu Utama (Tab ala Web Profesional)
menu_beranda, menu_kredit, menu_affiliate, menu_akun = st.tabs([
    "🏠 Beranda", 
    "💳 Kredit & Paket", 
    "🤝 Affiliate", 
    "👤 Akun"
])

# ================= 1. MENU BERANDA (TEMPAT CLIPPER) =================
with menu_beranda:
    st.title("🎬 AI Video Clipper - Studio")
    st.write("Ubah video panjang dari YouTube menjadi klip pendek otomatis.")
    
    # Sidebar untuk Pengaturan Pro (Nanti dikunci untuk berbayar)
    with st.sidebar:
        st.header("⚙️ Pengaturan Pro")
        st.write("Fitur ini akan dikunci untuk pengguna berbayar.")
        template_sub = st.selectbox("Template Subtitle", ["Basic", "Neon Pop", "Minimalist", "Bold Color"], disabled=True)
        template_hook = st.selectbox("Template Visual Hook", ["None", "Split Screen", "Dynamic Zoom"], disabled=True)
        rasio = st.selectbox("Rasio Aspek", ["9:16 (TikTok/Reels)", "16:9 (YouTube)", "1:1 (Square)"])
        resolusi = st.select_slider("Resolusi Target", options=["480p", "720p", "1080p"], value="1080p")

    url = st.text_input("Tempel Link YouTube:")

    col1, col2 = st.columns(2)
    with col1:
        start_time = st.time_input("Waktu Mulai")
    with col2:
        end_time = st.time_input("Waktu Selesai")

    if st.button("Mulai Proses Clipping"):
        if url:
            st.info(f"Proses dimulai untuk: {url}")
            st.write(f"Rasio: {rasio} | Resolusi: {resolusi}")
            st.warning("Mesin AI pemotong video sedang dalam tahap integrasi.")
        else:
            st.error("Masukkan link terlebih dahulu!")

# ================= 2. MENU KREDIT & PEMBAYARAN =================
with menu_kredit:
    st.title("💳 Kredit & Paket Berlangganan")
    st.info("🎁 **Bonus Pengguna Baru:** Kamu mendapatkan Free Beberapa Kredit Skor untuk mencoba membuat clipping gratis!")
    
    st.metric(label="Sisa Kredit Skor Anda", value="3 Kredit Gratis")
    
    st.markdown("---")
    st.subheader("Pilih Paket Berlangganan Sesuai Kebutuhanmu")
    
    col_lite, col_prem, col_vip = st.columns(3)
    
    with col_lite:
        st.markdown("### Paket Lite")
        st.write("Cocok untuk pemula")
        st.markdown("**Rp 49.000 / bln**")
        st.write("• 50 Kredit/bulan\n• Resolusi 720p\n• Tanpa Watermark Dasar")
        st.button("Pilih Lite", key="btn_lite")
        
    with col_prem:
        st.markdown("### Paket Premium")
        st.write("Paling Populer 🔥")
        st.markdown("**Rp 99.000 / bln**")
        st.write("• 150 Kredit/bulan\n• Resolusi 1080p\n• Template Subtitle Pro")
        st.button("Pilih Premium", key="btn_prem")
        
    with col_vip:
        st.markdown("### Paket VIP")
        st.write("Untuk Agensi / Profesional")
        st.markdown("**Rp 199.000 / bln**")
        st.write("• Kredit Unlimited\n• Resolusi 4K / 1080p Prioritas\n• Semua Template & Fitur AI Terbuka")
        st.button("Pilih VIP", key="btn_vip")

# ================= 3. MENU AFFILIATE =================
with menu_affiliate:
    st.title("🤝 Program Affiliate AI Clipper")
    st.write("Mau dapat penghasilan tambahan? Bantu promosikan website ini ke para *clipper* di luar sana dan dapatkan komisi menarik setiap ada yang berlangganan dari link kamu!")
    
    st.markdown("---")
    st.subheader("💡 Cara Kerja Affiliate:")
    st.write("1. **Daftar** untuk mendapatkan link unik khusus milikmu.")
    st.write("2. **Sebarkan link** tersebut ke media sosial, grup kreator, atau kontenmu.")
    st.write("3. **Dapatkan Komisi** dari setiap pengguna yang mendaftar dan membeli paket melalui link tersebut.")
    
    st.success("💰 **Keuntungan:** Komisi hingga **30%** dari total transaksi referral kamu secara berkelanjutan!")
    
    with st.form("form_affiliate_reg"):
        st.subheader("Formulir Pendaftaran Affiliate")
        nama = st.text_input("Nama Lengkap")
        email = st.text_input("Email Aktif")
        channel = st.text_input("Link Media Sosial / Channel Utama (TikTok/YouTube/IG)")
        submit_reg = st.form_submit_button("Daftar Sekarang")
        
        if submit_reg:
            if nama and email:
                st.success("Pendaftaran berhasil! Link referral unikmu akan segera dikirimkan ke email.")
            else:
                st.error("Mohon lengkapi nama dan email.")

# ================= 4. MENU AKUN =================
with menu_akun:
    st.title("👤 Akun Saya")
    st.write("Kelola informasi profil dan status langgananmu di sini.")
    
    st.text_input("Nama Pengguna", value="Urifah Creator")
    st.text_input("Email", value="pengguna@email.com")
    st.selectbox("Status Paket Saat Ini", ["Free Trial (New User)", "Lite Member", "Premium Member", "VIP Member"], disabled=True)
    
    if st.button("Simpan Perubahan Profil"):
        st.success("Perubahan berhasil disimpan!")
