import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code(code: str, language: str = "auto") -> dict:
    prompt = f"""
    You are an expert code reviewer. Review the following {language} code and provide:
    1. A brief overall review
    2. A list of specific suggestions for improvement
    
    Code to review:
```{language}
    {code}
```
    
    Respond in JSON format only, no markdown:
    {{
        "review": "overall review here",
        "suggestions": ["suggestion 1", "suggestion 2", "suggestion 3"]
    }}
    """
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert code reviewer. Always respond in valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    result = json.loads(response.choices[0].message.content)
    
    return {
        "language": language,
        "review": result["review"],
        "suggestions": result["suggestions"]
    }