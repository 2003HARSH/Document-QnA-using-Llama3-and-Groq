from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import GooglePalmEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
import tempfile


def get_pdf_text(pdf_docs):
    docs=[]
    for pdf in pdf_docs:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, pdf.name)
        with open(path, "wb") as f:
                f.write(pdf.getvalue())
        loader = PyPDFLoader(path)
        docs=docs+loader.load_and_split()
    print(docs)
    return  docs

def get_text_chunks(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_documents(docs)
    return chunks

def get_vector_store(docs,GOOGLEPALM_API_KEY):
    load_dotenv()
    embeddings = GooglePalmEmbeddings(google_api_key=GOOGLEPALM_API_KEY)
    vector_store = FAISS.from_documents(docs, embedding=embeddings)
    vector_store.save_local("faiss_index")
    print('got vector stores')

def get_conversational_chain(GROQ_API_KEY):
    load_dotenv()
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    llm=ChatGroq(groq_api_key=GROQ_API_KEY,
                 model_name='Llama3-8b-8192')

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question,GROQ_API_KEY,GOOGLEPALM_API_KEY):
    load_dotenv()
    embeddings = GooglePalmEmbeddings(google_api_key=GOOGLEPALM_API_KEY)
    
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question,k=2)

    chain = get_conversational_chain(GROQ_API_KEY)

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)
    
    return[response,docs]


