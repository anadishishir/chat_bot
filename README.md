Retrieval - Augmented Generation Based Context Aware ChatBot 

Made a simple RAG based ChatBot that answers questions based on the documents ( context ) it is provided. 
Also , implemented a simple User Interference for it. 
ChatBot also tores user history ( upto five chats ) for different users. 
ChatBot is based upon Hugging Face Models. 

Features : 
1. Stores user chat history ( upto five chats ) per user. 
2. Uses Embedding - based semantic search. 
3. Response generated are context - aware. 
4. Has Flask API for backend. 
5. Has a simple User Interference. 
6. It is completely local so there is no actual money used to run model. 

Tech Stack : 
1. Python 
2. Flask 
3. Hugging Face Transformers 
4. Sentence Transformers 
5. Hyper Text Markup Language 
6. Cascading Style Sheets 
7. JavaScript 

Working : 
1. First , incoming data is splitted into chunks. 
2. Then , these chunks are converted into embeddings. 
3. The most relevant chunk for query is founded. 
4. Generator generates answer using retrived context. 

To Run : 
pip install -r requirements.txt 
python app.py 

API : 
POST/chat 
{ 
    "message" : "Your Question" 
} 

Future Improvements : 
1. Add PDF support. 
2. Use vector database. 
3. Increasing chat history limit. 
4. Improving User Interference. 
5. Storing data on server. 
  

 