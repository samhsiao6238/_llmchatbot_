# vector.py
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain.chains import RetrievalQA
from solutions.llm import llm, embeddings
from solutions.tools.secret import get_secret

# 載入套件
import os
from dotenv import load_dotenv
# 載入環境變數
load_dotenv()

# 註解變數取的方式
# NEO4J_URI = os.getenv("NEO4J_URI")
# NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
# NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
# 改寫用 get_secret 函數取得變數
NEO4J_URI = get_secret("NEO4J_URI")
NEO4J_USERNAME = get_secret("NEO4J_USERNAME")
NEO4J_PASSWORD = get_secret("NEO4J_PASSWORD")

neo4jvector = Neo4jVector.from_existing_index(
    embeddings,                 # <1>
    url=NEO4J_URI,              # <2>
    username=NEO4J_USERNAME,    # <3>
    password=NEO4J_PASSWORD,    # <4>
    index_name="moviePlots",    # <5>
    node_label="Movie",         # <6>
    text_node_property="plot",  # <7>
    embedding_node_property="plotEmbedding",  # <8>
    retrieval_query="""
    RETURN
        node.plot AS text,
        score,
        {
            title: node.title,
            directors: [ (person)-[:DIRECTED]->(node) | person.name ],
            actors: [ (person)-[r:ACTED_IN]->(node) | [person.name, r.role] ],
            tmdbId: node.tmdbId,
            source: 'https://www.themoviedb.org/movie/'+ node.tmdbId
        } AS metadata
    """,
)

retriever = neo4jvector.as_retriever()

kg_qa = RetrievalQA.from_chain_type(
    llm,  # <1>
    chain_type="stuff",  # <2>
    retriever=retriever,  # <3>
)
