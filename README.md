# Document QnA with Llama3, Groq API, LangChain, and Streamlit

Welcome to the **Document QnA** project! This project leverages the power of Llama3 and Groq API, integrated with LangChain, FAISS, Google Palm Embeddings, and deployed on Streamlit, to provide an interactive question-and-answer system based on document content.

### Streamlit UI:
![](https://github.com/2003HARSH/Document-QnA-using-Llama3-and-Groq/blob/main/docs/static/docqna.png)
### LangSmith Monitoring:
![](https://github.com/2003HARSH/Document-QnA-using-Llama3-and-Groq/blob/main/docs/static/langsmith.png)

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Document QnA is an interactive application that allows users to upload documents and ask questions related to the content of those documents. The system uses advanced language models to understand and respond to user queries accurately, and it can also identify the page number of the PDF where the relevant context is found.

## Features

- **Document Upload**: Easily upload multiple documents for analysis.
- **Interactive QnA**: Ask questions and receive answers based on the document content.
- **Page Number Identification**: Find out the page number in the PDF where the context is present.
- **Relevant Document Identification**: Automatically identify which document contains the relevant answer.
- **Streamlit Interface**: User-friendly web interface for seamless interaction.
- **Powered by Llama3 and Groq API**: Utilizes advanced language models for natural language understanding.
- **Efficient Text Processing**: Uses RecursiveCharacterTextSplitter for effective text handling.
- **Enhanced Search**: Employs FAISS for efficient similarity search.
- **Advanced Embeddings**: Uses Google Palm Embeddings for improved text representations.

## Installation

To get started with the Document QnA project, follow these steps:

1. **Clone the repository:**
   ```bash
   https://github.com/2003HARSH/Document-QnA-using-Llama3-and-Groq.git
   cd Document-QnA-using-Llama3-and-Groq
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root directory and add your API keys and necessary configurations.
   ```env
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_PALM_API_KEY=your_google_palm_api_key
   ```

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Upload documents:**
   - Go to the running Streamlit app in your web browser.
   - Use the document upload feature to upload one or more documents.

3. **Ask questions:**
   - Enter your questions in the provided text box.
   - Get answers based on the content of the uploaded documents, along with the page number and document name where the context is found.
4. **Don't want to install, try it out here** https://document-qna-using-llama3-and-groq.streamlit.app/

## Configuration

Ensure your `.env` file is correctly set up with the required API keys. The application relies on these keys to interact with Llama3, Groq API, and other services for processing and generating responses.

## Technologies Used

- **Llama3**: Advanced language model for natural language processing.
- **Groq API**: Powerful API providing faster inference to language models.
- **LangChain**: Framework for building applications with language models.
- **FAISS**: Efficient similarity search.
- **Google Palm Embeddings**: Advanced embeddings for improved text representation.
- **RecursiveCharacterTextSplitter**: Tool for effective text handling.
- **Streamlit**: Fast way to build and share data apps.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!

---

## Contact

- **Author**: Harsh Gupta
- **Email**: harshnkgupta@gmail.com
- **GitHub**: [@2003HARSH](https://github.com/2003HARSH)

---

Thank you for using Document QnA! We hope it enhances your document analysis and interaction experience.

