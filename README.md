# chatwithdata
Streamlit app to chat with data (RAG implementation using Orca-Mini3b, FAISS, Streamlit). Currently only *.csv type of data. You can upload any csv file and get insights out of it.

## Setup 
1. You need Python installed. If you don't have Python installed, install if from this [link](https://www.python.org/downloads/)

2. Clone the repository. 
```
git clone https://github.com/LexiestLeszek/chatwithdata.git
```

3. Once cloned, go inside the repository or folder.
```
cd chatwithdata
```

4. Thanks to the GPT4ALL guys, download the model file, create "model" folder in the main directory and put the model there 
```
https://gpt4all.io/models/gguf/orca-mini-3b-gguf2-q4_0.gguf
```

5. Create a virtual environment and activate it.
```
python3 -m venv .venv && source .venv/bin/activate
```

6. Install the packages from the requirements.txt file.
```
pip install -r requirements.txt
```
7. Run the streamlit app.
```
streamlit run ch.py
```

After running the streamlit command, you should now be able to access the app at http://localhost:XXXX/. Upload the csv file and happy chatting.
