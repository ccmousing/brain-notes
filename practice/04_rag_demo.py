import chromadb

# create chrmabd client
chromadb_client = chromadb.Client()

# create collection
collection = chromadb_client.create_collection(name="note")

# add documents to collection
collection.add(
    ids=["id1", "id2"],
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges",
    ],
)

# query the collection

results = collection.query(
    query_texts=[
        "This is a query document about hawaii"
    ],  # Chroma will embed this for you
    n_results=2,  # how many results to return
)
print(results)
