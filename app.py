import streamlit as st
import os
import subprocess

# Konfigurasi Halaman
st.set_page_config(
    page_title="Paidi.ai - AI Video Studio",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- FUNGSI BACKEND OTOMATISASI CLIPPING YOUTUBE ---
def process_youtube_clip(youtube_url, start_time="00:00:10", end_time="00:00:40", output_filename="output_clip.mp4"):
    """
    Fungsi untuk mengunduh segmen video YouTube dan memotongnya
    menggunakan yt-dlp dan ffmpeg secara efisien.
    """
    try:
        os.makedirs("/tmp", exist_ok=True)
        temp_input = "/tmp/temp_full_video.mp4"
        output_path = f"/tmp/{output_filename}"

        # 1. Unduh resolusi rendah (360p) untuk menghemat RAM server
        download_command = [
            "yt-dlp",
            "-f", "best[height<=360]", 
            "-o", temp_input,
            youtube_url
        ]
        subprocess.run(download_command, check=True)

        # 2. Potong video menggunakan FFmpeg berdasarkan timestamp
        ffmpeg_command = [
            "ffmpeg",
            "-y",
            "-ss", str(start_time),
            "-i", temp_input,
            "-to", str(end_time),
            "-c:v", "libx264",
            "-c:a", "aac",
            "-strict", "experimental",
            output_path
        ]
        subprocess.run(ffmpeg_command, check=True)

        return output_path

    except Exception as e:
        print(f"Terjadi kesalahan saat memproses video: {e}")
        return None

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
st.sidebar.markdown("**Status Sistem:** 🚀 Produksi Aktif")
st.sidebar.markdown("**Kredit Anda:** 5 / 10 Sesi")
st.sidebar.markdown("📍 Malang, Indonesia")

# 1. Halaman Beranda & Studio
if menu == "Beranda & Studio":
    
    # --- JUDUL UTAMA STUDIO ---
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-size: 30px; margin-bottom: 8px;">⚡ Paidi.ai Video Studio</h1>
            <h3 style="color: #4da6ff; margin-top: 0; font-size: 18px;">Ekstraksi Konten Sinematik: Dari Video Panjang Menjadi Reels Daya Tinggi 🔗</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # --- PANEL STUDIO UTAMA ---
    st.markdown("### 🛠️ Studio Pemrosesan Konten")
    
    # Banner Promo Pengguna Baru
    st.markdown("""
    <div class="promo-banner">
        <span style="font-size: 14px; font-weight: bold; color: #4da6ff;">🎁 PROMO SPESIAL PENGGUNA BARU:</span>
        <p style="font-size: 13px; margin: 4px 0 0 0; opacity: 0.95;">Nikmati <strong>Ekstra 5 Sesi Gratis Tambahan</strong> + Diskon 50% untuk peningkatan paket pertama Anda hari ini!</p>
    </div>
    """, unsafe_allow_html=True)

    # Form Studio Input & Eksekusi Otomasi Klip
    st.markdown("#### 🔗 Tautan Sumber Media (YouTube URL)")
    link = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...", label_visibility="collapsed")
    
    col1, col2 = st.columns(2)
    with col1:
        durasi = st.selectbox("Durasi Target Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"])
        subtitle = st.selectbox("Gaya Subtitle / Headline", ["Dinamis Alex Hormozi Style", "Minimalis Clean", "Tanpa Subtitle"])
        rasio = st.selectbox("Rasio Aspek Video", ["9:16 (Vertical Reels/TikTok)", "1:1 (Square)", "16:9 (Horizontal)"])
    with col2:
        resolusi = st.selectbox("Resolusi Ekspor", ["1080p (Full HD)", "720p (HD)"])
        estimasi = st.selectbox("Estimasi Durasi Proses", ["⚡ Kilat (~3-5 Menit)", "Standard"])
        fokus = st.selectbox("Fokus Ekstraksi Konten", ["🔥 Deteksi Menyeluruh (AI Multi-Analisis)", "Fokus Hook Utama"])
    
    if st.button("✨ Eksekusi Analisis Otonom", type="primary"):
        if link:
            with st.spinner("🚀 Sistem AI sedang memindai dan memotong klip terbaik dari YouTube untuk Anda..."):
                # Memanggil fungsi pemrosesan video nyata
                hasil_klip = process_youtube_clip(link, start_time="00:00:10", end_time="00:00:40")
                
                if hasil_klip and os.path.exists(hasil_klip):
                    st.success("🎉 Klip video sinematik Anda berhasil dibuat!")
                    st.video(hasil_klip)
                    
                    # Tombol Unduh
                    with open(hasil_klip, "rb") as file:
                        st.download_button(
                            label="📥 Unduh Klip Hasil (MP4)",
                            data=file,
                            file_name="paidi_ai_reels_hasil.mp4",
                            mime="video/mp4"
                        )
                else:
                    st.error("⚠️ Gagal memproses video. Pastikan tautan YouTube aktif dan dapat diakses.")
        else:
            st.warning("⚠️ Silakan masukkan tautan YouTube terlebih dahulu!")

    # --- LANGKAH-LANGKAH PENGGUNAAN ---
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

    # --- PROFIL FOUNDER ---
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

    # --- INFORMASI KORPORAT ---
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

# Halaman Lainnya
elif menu == "Kredit & Paket":
    st.markdown("# 💳 Kredit & Paket Berlangganan")
    st.markdown("---")
    st.write("Sisa sesi pemrosesan AI Anda saat ini adalah **5 / 10 Sesi**.")
    st.button("Top Up Sesi Tambahan")

elif menu == "Program Affiliate":
    st.markdown("# 🤝 Program Affiliate Paidi.ai")
    st.markdown("---")
    st.write("Dapatkan komisi menarik dengan membagikan tautan referral eksklusif Anda ke sesama kreator.")
    st.code("https://paidi.ai/ref/usman_shidiq")

elif menu == "Akun & Profil":
    st.markdown("# 👤 Akun & Profil Founder")
    st.markdown("---")
    st.markdown("### Halo, saya Usman Shidiq")
    st.write('"Sebagai pengembang yang merintis Paidi.ai dari Malang, visi kami adalah memangkas kerumitan teknis produksi video pendek agar setiap kreator bisa fokus penuh pada pesan dan karya mereka."')
    st.markdown("**Usman Shidiq** · *Founder of Paidi.ai*")
    st.markdown("📍 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139")
    st.markdown("📞 Hotline: 083853413171 | ✉️ Email: support@paidi.ai")

# Footer Korporat
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 12px; line-height: 1.5;'>
    <strong>Paidi.ai</strong> — Infrastruktur perangkat lunak rintisan berbasis kecerdasan buatan untuk otomatisasi repurposing video di Indonesia.<br>
    🏢 Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139 | 📞 083853413171 | ✉️ support@paidi.ai<br>
    © 2026 PT Paidi.ai Group. Didirikan 2026. Hak Cipta Dilindungi Undang-Undang. Engineered with excellence in Malang, Indonesia.
</div>
""", unsafe_allow_html=True)
