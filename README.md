# GovTechTHA

Description:
Welcome to my repository for the GovTech Take-Home Assignment! This repository contains the code and process taken to cover the items in the later section. I apologise in advance for not using conventional frameworks and libraries for the frontend or not following conventional rules for the backend because my experience mainly lies with Data Science projects and fullstack ones. As I would still like to show what I've learnt and tried within the given period, I will be using Streamlit instead as I usually do to quickly build and deploy PoCs for my projects. As for the backend, I have and will try my best to read up and try to employ the frameworks and libraries to the best of my abilities. 

Contents:
- OpenAI API to interact with gpt-3.5-turbo
- Streamlit web application to converse with the LLM

To Be Added:
- database implementation for backend to connect to
- replace pseudocode for backend code
- adding functionality to allow users to use their own API Key

How to Use (Without Docker):
1. Pull from repo.
2. Navigate to "src" and install requirements using "pip install -r requirements.txt"
3. To load documentation, launch FastAPI using ```python -m uvicorn main:app --reload```
4. Documentation can be accessed at http://127.0.0.1:8000/docs . 
5. To load chat interface, launch Streamlit using ```python -m streamlit run app.py```
6. Web interface should automatically load.

How to View (Using Docker):
1. Pull from repo.
2. Create your own .env file and add it to the "src" folder, setting your API Key in the following format:

"OPENAI_KEY = {API_KEY}"

3. Run "docker build -t {image_name}:{version}"
4. Run "docker run -d -p {port}:8501 --name {webserver_name} {image_name}:{version}"
5. Visit the webpage at "http://localhost:9090/" in your browser

Requirements:

Python >= 3.8
Relevant Python libraries (FastAPI, Pydantic, Beanie, OpenAI)

Contact:
For any inquiries or assistance regarding the repository, please contact Keng Boon at kbang.2021@scis.smu.edu.sg.
