from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json

# Initialize Flask app
app = Flask(__name__)

# Load models and index
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
    chatbotmodel = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")
    faiss_index = faiss.read_index("faiss_index.index")
    with open("metadata.json", "r") as f:
        metadata = json.load(f)
except Exception as e:
    print(f"Error loading models or index: {e}")
    exit()

# Functions for retrieval and response generation
def retrieve_papers(query, top_k=5):
    try:
        query_embedding = model.encode([query])
        distances, indices = faiss_index.search(query_embedding, top_k)
        results = [metadata[i] for i in indices[0]]
        return results
    except Exception as e:
        print(f"Error retrieving papers: {e}")
        return []

def generate_response(query, retrieved_papers):
    try:
        context = "\n".join([f"Title: {p['title']}, Authors: {p['authors']}" for p in retrieved_papers])
        input_text = f"User query: {query}\nAnswer the query:"
        inputs = tokenizer.encode(input_text, return_tensors="pt")
        outputs = chatbotmodel.generate(inputs, max_length=500)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return ""

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form.get('query', '')
    
    # Validate input
    if not user_query.strip():
        return render_template('response.html', user_query=user_query, papers=[], response="Please enter a valid query.")
    
    retrieved_papers = retrieve_papers(user_query)
    response = generate_response(user_query, retrieved_papers)
    
    # Validate response
    if not response.strip():
        return render_template(
            'response.html', 
            user_query=user_query, 
            papers=retrieved_papers, 
            response="No relevant papers found or unable to generate a response."
        )
    
    return render_template(
        'response.html',
        user_query=user_query,
        papers=retrieved_papers,
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True)
