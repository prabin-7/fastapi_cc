import os 
from dotenv import load_dotenv 
from openai import OpenAI 

load_dotenv() 

api_key = os.getenv("XAI_API_KEY") 
if not api_key: 
    raise ValueError("API key not found") 

client = OpenAI( 
                api_key = api_key, 
                base_url = "https://api.x.ai/v1",)

def generate_response(prompt: str) -> str: 
    "send prompt to grok and get response"
    
    try: 
        response = client.chat.completions.create(
            model = "grok-3", 
            messages = [
            {"role": "system", "content": "YOur are a helpful assistant named Grok."},
            {"role": "user", "content": prompt},
            ],
            temperature = 0.5,
            stream = False,
        )
        return response.choices[0].message.content 
    except Exception as e: 
        return f"Error connecting to Grok : {str(e)}"
    
