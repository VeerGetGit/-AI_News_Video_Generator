# Task 1: AI-Based Trending News Video Generator

## **Project Overview**

This project is an **automated news video generation tool** that scrapes trending news articles and converts them into short, engaging videos. It uses the **Groq API (openai-gpt-oss-120B)** for script generation and fetches relevant stock videos from **Pexels Video API**. The final output includes AI-generated voice narration stitched with stock videos to produce a 30–60 second news video.

---

## **Objective**

- Scrape trending news articles  
- Generate concise scripts using **Groq API**  
- Fetch relevant stock videos from **Pexels Video API**  
- Convert scripts to voice narration  
- Produce narrated news videos automatically  

---

## **Workflow**

1. User initiates video generation via frontend (Streamlit)  
2. News scraper fetches trending articles  
3. Script is generated using **Groq API (openai-gpt-oss-120B)**  
4. Keywords from the script are used to fetch stock videos from **Pexels**  
5. Script is converted to voice narration using Text-to-Speech  
6. Video clips and audio narration are stitched together into the final video  

---

## **System Architecture**

Trending News Source
↓
News Scraper
↓
Groq API (Script Generation)
↓
Pexels Video Fetcher
↓
Text-to-Speech Module
↓
Video Generator & Stitcher
↓
Final News Video Output


---

## **Technology Stack**

- **Programming Language:** Python  
- **Backend:** Flask  
- **Frontend:** Streamlit  
- **News Scraping:** Web APIs / Requests  
- **Script Generation:** Groq API (openai-gpt-oss-120B)  
- **Video Source:** Pexels Video API  
- **Text-to-Speech:** Python TTS libraries  
- **Video Processing:** MoviePy  
- **Version Control:** Git & GitHub  

---

## **Modules Overview**

- **News Scraper:** Fetches trending news content  
- **Script Generator:** Generates concise scripts using Groq LLM  
- **Pexels Video Fetcher:** Downloads relevant stock videos  
- **Text-to-Speech Module:** Converts script to narration  
- **Video Generator & Stitcher:** Creates the final news video  

---

## **Setup & Installation**

1. **Clone the repository**
```bash
git clone https://github.com/VeerGetGit/-AI_News_Video_Generator.git
cd -AI_News_Video_Generator



