import openai
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_elasticsearch import ElasticsearchStore

class QuestionAnswerer: 
    def __init__(self, api_key, model="gpt-3.5-turbo-0125"):
        openai.api_key = api_key
        self.model = model
        self.embeddings = OpenAIEmbeddings()
    

    def answer_questions(self, questions, document_text, top_k = 3):
        answers = {}
        text_splitter = CharacterTextSplitter(        
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap  = 100,
            length_function = len,
        )
        # Split the text into chunks
        doc_chunks = text_splitter.split_text(document_text)
        doc_chunks = text_splitter.create_documents(doc_chunks)

        db = ElasticsearchStore.from_documents(
            doc_chunks, 
            self.embeddings, 
            es_url="http://localhost:9200", 
            index_name="zania_bot",
            strategy=ElasticsearchStore.ApproxRetrievalStrategy(
                hybrid=False,
            )
        )

        answers = {}
        system_prompt = "You are a helpful chat assistant. You will need to answer some questions based on the context given."
        for question in questions:
            # Retrieve relevant documents
            docs = db.similarity_search(question,  k=top_k)
            context = "\n".join([doc.page_content for doc in docs])
            # Construct the prompt for the LLM
            prompt = f"\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
            response = openai.chat.completions.create(
                model=self.model,
                messages=[ {"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
            )
            answers[question] = response.choices[0].message.content.strip()
        return answers