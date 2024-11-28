# 2024-11-25
# Andreas Kretz
# This code currently doesn't work because the preparation of the text for ElasticSearch doesn't work
# Try to fix this and write the data

import json, os  # Importing JSON for handling JSON data and os for interacting with the operating system
import fitz  # PyMuPDF
from llama_index.core import Document, Settings  # Importing Document class and Settings for managing LlamaIndex
from llama_index.core.node_parser import SentenceSplitter  # Importing SentenceSplitter to split text into smaller chunks
from llama_index.core.ingestion import IngestionPipeline  # Importing IngestionPipeline for managing data ingestion
from llama_index.embeddings.ollama import OllamaEmbedding  # Importing OllamaEmbedding for generating text embeddings
from llama_index.vector_stores.elasticsearch import ElasticsearchStore  # Importing ElasticsearchStore for vector storage
from dotenv import load_dotenv  # Importing load_dotenv to load environment variables from a .env file
from llama_index.core import VectorStoreIndex, QueryBundle, Response, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from index_raw import es_vector_store
from ollama import chat
from ollama import ChatResponse

# extract text form the pdf with PyMuPDF
def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = page.get_text()
        text += page_text
    print(text)
    
    return text

# feed the pdf into mistral and get a JSON back
# this fails currently because I cannot get a good answer from mistral. the problem is with escaping \n and '. 

def prepare_text_to_json(text_to_summarize):
    instruction_template = "Here's a text. Encapsulate it into a json as a string and don't turn it into json attributes. Keep it flat. The attribute where the text should go into is called text. Create another attribute of the json called name and put the name of the person there:"
    
    response: ChatResponse = chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': instruction_template + text_to_summarize,
        },
    ])
 
    
    print(".....Prepared this json.....\n")
    print(response['message']['content'])

    return response['message']['content']


# Define an Elasticsearch vector store with configuration for local Elasticsearch
es_vector_store = ElasticsearchStore(
    index_name="student_cvs",  # Name of the Elasticsearch index
    vector_field='conversation_vector',  # Field to store the vector representation of the text
    text_field='conversation',  # Field to store the original text
    es_url="http://localhost:9200"  # URL of the local Elasticsearch instance
)

local_llm = Ollama(model="mistral")

def main():
    ollama_embedding = OllamaEmbedding("mistral")   # Initialize the embedding model for generating embeddings using the "mistral" model

    # Set up an ingestion pipeline with transformations and the Elasticsearch vector store
    pipeline = IngestionPipeline(   
        transformations=[
            
            SentenceSplitter(chunk_size=350, chunk_overlap=50), # Split text into chunks of size 350 with 50 characters of overlap
            ollama_embedding, # Use the embedding model to generate embeddings for the chunks
        ],
        vector_store=es_vector_store  # Use the configured Elasticsearch vector store
    )

    extracted = extract_text_from_pdf('Liam_McGivney_CV.pdf')   #extract the text from the CV
    prepped_json = prepare_text_to_json(extracted)      # prepare the json

    #create a document (I think this is wrong right now)
    documents = Document(text=prepped_json['text'], metadata={"name": prepped_json['name']})
    #documents = [Document(text=item['text']) for entry in prepped_json]
    #documents = [Document(text=item['text'], metadata={"name": item['name']}) for item in prepped_json]

    pipeline.run(documents=documents)   # Run the pipeline to process documents and store embeddings in Elasticsearch
    print(".....Done running pipeline.....\n")  # Print a completion message

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function
