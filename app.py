import streamlit as st
import yt_dlp
import os

st.title("🎬 AI Video Clipper")

url = st.text_input("Tempel Link Video:")

if st.button("Download Video"):
    if url:
        st.write("Sedang mengunduh video...")
        try:
            # Menambahkan opsi tambahan agar tidak diblokir YouTube (Error 403)
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': 'video.mp4',
                'geo_bypass': True,
                'nocheckcertificate': True,
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            st.success("Video berhasil diunduh!")
            st.video("video.mp4")
        except Exception as e:
            st.error(f"Gagal: {e}")
    else:
        st.error("Masukkan link!")
