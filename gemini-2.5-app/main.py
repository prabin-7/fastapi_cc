from fastapi import FastAPI 
import gradio as gr 
from gemini_service import generate_response 
import uvicorn 

app = FastAPI() 


@app.get("/")
def read_root(): 
    return {"message": "Welcome to Gemini with FastAPI and gradio"}

@app.post("/api/chat")
def chat_endpoint(prompt: str):
    response = generate_response(prompt)
    return {"response": response}

#Gradio ui setup 

def gradio_chat_interface(user_message, history): 
    bot_response = generate_response(user_message) 
    return bot_response 


demo = gr.ChatInterface(
    fn = gradio_chat_interface, 
    title = "Gemini Chatbot",
    description = "Ask gemini anything! ",
    type = "messages"
) 


app = gr.mount_gradio_app(app, demo, path= "/gradio")

if __name__=="__main__":
    print("Starting Server ...")
    print("Api available at http://localhost:8000")
    print("Gradio UI available at http://localhost:8000/gradio")
    
    
    #uvicorn to run the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port = 8000)