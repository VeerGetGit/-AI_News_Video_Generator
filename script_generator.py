from groq import Groq
from dotenv import load_dotenv
import os
import random


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file.")

client = Groq(api_key=GROQ_API_KEY)

def generate_script(topic_summary: str) -> dict:
    """
    Generates narration and diverse visual keywords.
    Returns:
        {
            'narration': str,
            'visual_keywords': [str, ...]
        }
    """
    narration_prompt = f"""Write a 90-second engaging news narration for TTS about: {topic_summary}
Use plain text only. Make it lively, detailed, and suitable for audio narration."""

    keywords_prompt = f"""
Extract 7-10 **unique** visual keywords or short scenes (1-3 words each) 
from this news summary. Make each keyword different from each other and avoid generic words like 'news' or 'headlines'. 
Output as a comma-separated list:
{topic_summary}
"""


    try:
        
        narration_completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": narration_prompt}],
            temperature=1.2,
            max_completion_tokens=300,
            top_p=1,
            reasoning_effort="medium",
            stream=False
        )
        narration_text = narration_completion.choices[0].message.content.strip()
        narration_text = " ".join(narration_text.split())  
        if not narration_text:
            narration_text = topic_summary

        
        keywords_completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": keywords_prompt}],
            temperature=1.5,
            max_completion_tokens=120,
            top_p=1,
            reasoning_effort="medium",
            stream=False
        )
        raw_keywords = keywords_completion.choices[0].message.content
        visual_keywords = [kw.strip() for kw in raw_keywords.replace("\n", ",").split(",") if kw.strip()]
        visual_keywords = [kw for kw in visual_keywords if kw.isascii() and len(kw.split()) <= 3]

        raw_keywords = keywords_completion.choices[0].message.content
        visual_keywords = [kw.strip() for kw in raw_keywords.replace("\n", ",").split(",") if kw.strip()]
        visual_keywords = [kw for kw in visual_keywords if kw.isascii() and len(kw.split()) <= 3]

        
        import random
        random.shuffle(visual_keywords)
        visual_keywords = visual_keywords[:5]


        if not visual_keywords:
            visual_keywords = ["news", "headlines", "report", "journalist", "breaking news"]
        return {"narration": narration_text, "visual_keywords": visual_keywords}

    except Exception as e:
        print("Error generating script or keywords:", e)
        return {"narration": topic_summary, "visual_keywords": ["news", "headlines"]}
