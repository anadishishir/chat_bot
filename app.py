from flask import Flask, request, jsonify, render_template  
from pypdf import PdfReader 
from sentence_transformers import SentenceTransformer 
from transformers import pipeline 
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity 

app = Flask(__name__) 

# Models 
embedder = SentenceTransformer("all-MiniLM-L6-v2") 
generator = pipeline("text2text-generation" , model = "google/flan-t5-small") 

# Data 
with open("data.txt" , "r") as f : 
    chunks = f.read().split("\n") 

chunk_embeddings = embedder.encode(chunks) 

# Memory 
chat_sessions = {} 

# Similarity 
def cosine_similarity(a , b) : 
    return np.dot(a , b) / (np.linalg.norm(a) * np.linalg.norm(b)) 

def retrive(query) : 
    query_embedding = embedder.encode([query])[0] 
    scores = [cosine_similarity(query_embedding , emb) for emb in chunk_embeddings] 
    best_idx = np.argmax(scores) 
    return chunks[best_idx] 

# Chat Route 
@app.route("/chat" , methods = ["POST"]) 

def home() : 
    return render_template(index.html) 

def chat() : 
    global chat_sessions 

    user_query = request.json.get("message") 
    user_id = request.json.get("user_id" , "default_user") 

    # Create History If New User 
    if user_id not in chat_sessions : 
        chat_sessions[user_id] = [] 

    history = chat_sessions[user_id] 

    # Retrive Context 
    context = retrive(user_query) 

    # Add User Message 
    history.append(f"User : {user_query}") 

    # Keep Last 5 Messages 
    history = history[-5:] 
    chat_sessions[user_id] = history 

    history_text = "\n".join(history) 

    prompt = f"""
    You are a helpful assistant. 

    Conversation : 
    {history_text} 

    Context : 
    {context} 

    Answer the latest question. 
    """ 

    response = generator(prompt , max_length = 120 , do_sample = False) 
    answer = response[0]["generated_text"] 

    # Add Bot Reply 
    chat_sessions[user_id].append(f"Bot:{answer}") 

    return jsonify({
        "answer" : answer , 
        "history" : chat_sessions[user_id] 
    }) 

