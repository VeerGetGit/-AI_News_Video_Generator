import streamlit as st
import requests
import os

st.title("🌐 AI News Video Generator")

num_articles = st.number_input("Number of top news articles", min_value=1, max_value=5, value=1)
if st.button("Generate Video"):
    with st.spinner("Generating AI news video..."):
        response = requests.post(
            "http://127.0.0.1:5000/generate_video",
            json={"num_articles": num_articles}
        )
        if response.status_code == 200:
            video_path = response.json()["video_path"]
            st.success("🎬 Video generated successfully!")
            st.video(video_path)
        else:
            st.error(f"Error: {response.json().get('error')}")
