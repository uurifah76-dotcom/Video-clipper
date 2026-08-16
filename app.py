import streamlit as st

st.set_page_config(page_title="AI Video Clipper", page_icon="🎬")

st.title("🎬 AI Video Clipper")
st.write("Masukkan link video untuk memproses golden moments secara otomatis.")

video_url = st.text_input("Tempel Link Video di sini:")

if st.button("Mulai Clipping"):
    if video_url:
        st.info(f"Menerima link: {video_url}")
        st.warning("Sedang memproses... (Fitur AI sedang disiapkan)")
        # Di sini nanti kita akan tambahkan kode AI-nya
    else:
        st.error("Silakan masukkan link video terlebih dahulu!")
