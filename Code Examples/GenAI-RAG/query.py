# query.py
from llama_index.core import VectorStoreIndex, QueryBundle, Response, Settings
from llama_index.embeddings.ollama import  OllamaEmbedding
from llama_index.llms.ollama import Ollama
from index_raw import es_vector_store

# Local LLM to send user query to
local_llm = Ollama(model="mistral") # Initialize a local language model (LLM) using the "mistral" model from Ollama
Settings.embed_model= OllamaEmbedding("mistral")    # Create a VectorStoreIndex from the existing Elasticsearch vector store

index = VectorStoreIndex.from_vector_store(es_vector_store) # Create a VectorStoreIndex from the existing Elasticsearch vector store
query_engine = index.as_query_engine(local_llm, similarity_top_k=10)    # Create a query engine from the index using the local LLM and set top-k similarity results to 10

# Define the query string for the question you want to ask the system you'll see that it has some problems understanding the context 
# Especially how to find the policy number from the person's name. 

#query="Give me summary of water related issues"
#query="What policy number does emily green, born April 10th, 1988 have?"
#query="Who has the policy number DEF4567"
#query="What information about the person do you need to determin the policy number?"
query="What policy number does emily green, living in 101 Pine St, Boston, MA 02101 have?"

# Create a QueryBundle object, which packages the query and its embedding
# The embedding is generated using the configured embedding model in Settings
bundle = QueryBundle(query, embedding=Settings.embed_model.get_query_embedding(query))

# Use the query engine to execute the query bundle against the vector store
# and retrieve the most relevant results
result = query_engine.query(bundle)

# Print the results of the query to the console
print(result)




