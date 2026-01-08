import os 
from dotenv import load_dotenv
from google import genai 

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")
if not api_key: 
    raise ValueError("Api key is not found")

client = genai.Client(api_key= api_key)

def generate_response(prompt: str) -> str: 
    """send text prompt to geminin and get response"""
    
    try: 
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt,
        )
        return response.text 
    except Exception as e: 
        return f"Error connecting to Gemini API: {str(e)}"
    