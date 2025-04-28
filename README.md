📄 LLM_DOC_QA
A Document Q&A system powered by LLMs (Large Language Models).
This application allows users to upload documents (like PDFs) and ask questions based on their content.
It also uses Google Search for external queries when answers are not found inside the documents.

✨ Features
📚 Upload and query documents (PDF supported).

🤖 Local LLM-based document answering.

🔎 External Google Search integration for broader queries.

🌐 Deployed using Docker on Render.

🛠️ Built with Flask, LangChain (or similar framework), and Google Custom Search API.

🏗️ Project Structure
bash
Copy code

LLM_DOC_QA/
├── app/
│   ├── static/        
│   ├── templates/     
│   ├── uploads/       
├── project_venv/      
├── Dockerfile         
├── education_sample.pdf 
├── google_search.py   
├── llm_search.py      
├── main.py            
├── utils.py           
├── requirements.txt   
├── .gitignore         
├── README.md          


🚀 How to Run Locally
Clone the repository

bash
Copy code
git clone https://github.com/your-username/LLM_DOC_QA.git
cd LLM_DOC_QA
Create a virtual environment and activate it

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up environment variables

Create a .env file (if needed) with:

ini
Copy code
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
Run the application

bash
Copy code
python main.py
Access it at http://localhost:5000

🐳 Docker Deployment
Build Docker Image:

bash
Copy code
docker build -t llm_doc_qa .
Run Docker Container:

bash
Copy code
docker run -d -p 5000:5000 llm_doc_qa
🌍 Deployment on Render
This app is deployed on Render using an image hosted on Docker Hub.

Make sure to set the following environment variables in Render:

GOOGLE_API_KEY

GOOGLE_CSE_ID

📜 Technologies Used
Python

Flask

LangChain / RAG

Google Custom Search API

Docker

Render.com (for deployment)
https://llm-question-answer.onrender.com


✍️ Author
Anisha Mohanty


✅ TODO
 Improve UI/UX for uploads and results.

 Add support for more file formats (e.g., DOCX).

 Implement authentication (optional).

 Caching frequent queries.

