from fastapi import FastAPI 
import gradio as gr 
from grok_service import generate_response 
import uvicorn 

app = FastAPI() 

@app.get("/") 
def read_root(): 
    return {"message": "Grok API server is running"}
            
@app.post("/api/chat") 
def chat_endpoint(prompt: str): 
    response = generate_response(prompt)
    return {"response" : response} 

def gradio_chat_interface(user_message, history): 
    bot_response = generate_response(user_message)
    return bot_response 
    
demo = gr.ChatInterface(
    fn = gradio_chat_interface, 
    title = "Grok Chatbot",
    description = " Powered by xAI and FAstAPI",
    type = "messages"
)

app = gr.mount_gradio_app(app, demo, path = "/gradio") 

if __name__ == "__main__": 
    print("starting grok app") 
    print("Api availabel at http://localhost;8000")
    print("ui available at: http://localhost:8000/gradio")
    
    uvicorn.run(app, host = "127.0.0.1", port = 8000) 
