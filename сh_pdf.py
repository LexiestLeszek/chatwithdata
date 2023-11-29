from langchain.document_loaders.pdf import PyPDFLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import sys

DB_FAISS_PATH = "vectorstore/db_faiss"
loader = PyPDFLoader(file_path="data/startsmall-staysmall.pdf")
# loader = CSVLoader(file_path="data/users.csv", encoding="utf-8", csv_args={'delimiter': ','})
data = loader.load()
print(data)

# Split the text into Chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
text_chunks = text_splitter.split_documents(data)

# Download Sentence Transformers Embedding From Hugging Face
embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2',
                                   model_kwargs={'device': 'cpu'})

# COnverting the text Chunks into embeddings and saving the embeddings into FAISS Knowledge Base
db = FAISS.from_documents(text_chunks, embeddings)

db.save_local(DB_FAISS_PATH)

llm = CTransformers(model='./model/orca-mini-3b-gguf2-q4_0.gguf',
                    model_type="llama",
                    max_new_tokens=512,
                    temperature=0.1)

qa = ConversationalRetrievalChain.from_llm(llm,retriever=db.as_retriever(search_kwargs={'k': 3}))

while True:
    chat_history = []
    query = input(f"Input Prompt: ")
    if query == 'exit':
        print('Exiting')
        sys.exit()
    if query == '':
        continue
    result = qa({"question":query, "chat_history":chat_history})
    print("Response: ", result['answer'])