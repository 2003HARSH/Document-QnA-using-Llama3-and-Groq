import streamlit as st
from langchain_utils import get_pdf_text, get_text_chunks, get_vector_store,user_input

st.set_page_config(page_icon='📚',
                   page_title="Document📃 QnA🙋‍♂️ using Groq",                  
)

GOOGLEPALM_API_KEY=st.secrets['google_palm']
GROQ_API_KEY=st.secrets['groq_api']

def main():
    st.header("Document📃 QnA💁 using Llama3 and Groq⏩")
    st.write("Please don't❌ upload any private Documents...")
    st.markdown("""---""")
    user_question = st.text_input("Ask a Question from the PDF Files")

    if st.button('Generate Answer'):
        if user_question:
            output=user_input(user_question,GROQ_API_KEY,GOOGLEPALM_API_KEY)
            st.write(output[0])
            document=output[1]
            for i in range(len(document)):
                st.markdown("""---""")
                st.write("Source Document:",document[i].metadata['source'])
                st.write("From Page Number:",document[i].metadata['page'])

    with st.sidebar:
        st.title("Upload your PDF files here:")
        pdf_docs = st.file_uploader("You may upload multiple files. Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                docs = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(docs)
                get_vector_store(text_chunks,GOOGLEPALM_API_KEY)
                st.success("Done")



if __name__ == "__main__":
    main()

