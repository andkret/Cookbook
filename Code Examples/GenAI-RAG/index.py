import json, os  # Importing JSON for handling JSON data and os for interacting with the operating system
from llama_index.core import Document, Settings  # Importing Document class and Settings for managing LlamaIndex
from llama_index.core.node_parser import SentenceSplitter  # Importing SentenceSplitter to split text into smaller chunks
from llama_index.core.ingestion import IngestionPipeline  # Importing IngestionPipeline for managing data ingestion
from llama_index.embeddings.ollama import OllamaEmbedding  # Importing OllamaEmbedding for generating text embeddings
from llama_index.vector_stores.elasticsearch import ElasticsearchStore  # Importing ElasticsearchStore for vector storage
from dotenv import load_dotenv  # Importing load_dotenv to load environment variables from a .env file

def get_documents_from_file(file):
    """Reads a JSON file and returns a list of Document objects"""

    # Open the JSON file in read-text mode
    with open(file=file, mode='rt') as f:
        conversations_dict = json.loads(f.read()) # Load the file contents into a Python dictionary
      
    # Create a list of Document objects using the 'conversation' field as text 
    # and 'conversation_id' field as metadata
    documents = [Document(text=item['conversation'],
                          metadata={"conversation_id": item['conversation_id']})
                 for item in conversations_dict]
    
    return documents # Return the list of Document objects



# Define an Elasticsearch vector store with configuration for local Elasticsearch
es_vector_store = ElasticsearchStore(
    index_name="calls",  # Name of the Elasticsearch index
    vector_field='conversation_vector',  # Field to store the vector representation of the text
    text_field='conversation',  # Field to store the original text
    es_url="http://localhost:9200"  # URL of the local Elasticsearch instance
)

# Uncomment this if using Elastic Cloud and ensure ELASTIC_CLOUD_ID and ELASTIC_API_KEY are set in the .env file

# Load the .env file contents into environment variables
# This is used to access sensitive information like API keys or credentials
# load_dotenv('.env')

# es_vector_store = ElasticsearchStore(
#     index_name="calls",  # Name of the Elasticsearch index
#     vector_field='conversation_vector',  # Field for vector embeddings
#     text_field='conversation',  # Field for storing original text
#     es_cloud_id=os.getenv("ELASTIC_CLOUD_ID"),  # Cloud ID from the .env file
#     es_api_key=os.getenv("ELASTIC_API_KEY")  # API key from the .env file
# )

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

    documents = get_documents_from_file(file="conversations.json")  # Load data from a JSON file and convert it to a list of Document objects

    pipeline.run(documents=documents)   # Run the pipeline to process documents and store embeddings in Elasticsearch
    print(".....Done running pipeline.....\n")  # Print a completion message

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function
