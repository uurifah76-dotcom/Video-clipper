import streamlit as st
import yt_dlp
import os

st.title("🎬 AI Video Clipper (YouTube Edition)")

url = st.text_input("Tempel Link YouTube:")

# Placeholder untuk pengaturan proxy di masa depan
# Nanti jika sudah pakai server/proxy berbayar, tinggal diisi di sini
USE_PROXY = False 
PROXY_URL = "http://username:password@ip_proxy:port"  # Contoh format proxy berbayar

if st.button("Proses Video"):
    if url:
        st.write("Menghubungkan ke YouTube...")
        try:
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': 'video.mp4',
                'geo_bypass': True,
                'nocheckcertificate': True,
            }
            
            # Jika nanti sudah pakai proxy berbayar, sistem akan otomatis mengaktifkannya
            if USE_PROXY:
                ydl_opts['proxy'] = PROXY_URL

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            st.success("Video berhasil diunduh!")
            st.video("video.mp4")
        except Exception as e:
            st.error(f"Gagal mengunduh: {e}")
            st.info("Catatan: Error 403 terjadi karena batasan IP server gratisan. Ini akan teratasi otomatis saat nanti beralih ke server/proxy berbayar.")
    else:
        st.error("Masukkan link terlebih dahulu!")
