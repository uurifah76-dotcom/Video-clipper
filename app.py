import streamlit as st
import yt_dlp
import os

st.title("🎬 AI Video Clipper")

url = st.text_input("Tempel Link Video:")

if st.button("Download Video"):
    if url:
        st.write("Sedang mengunduh video...")
        try:
            ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("Video berhasil diunduh!")
            st.video("video.mp4")
        except Exception as e:
            st.error(f"Gagal: {e}")
    else:
        st.error("Masukkan link!")
