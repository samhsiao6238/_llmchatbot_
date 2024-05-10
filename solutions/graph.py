# graph.py
# 導入自訂函數
from solutions.tools.secret import get_secret
from langchain_community.graphs import Neo4jGraph
# dotenv
# import os
# from dotenv import load_dotenv
# # 環境參數
# load_dotenv()

# 註解變數取的方式
# NEO4J_URI = os.getenv("NEO4J_URI")
# NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
# NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
# 改寫用 get_secret 函數取得變數
NEO4J_URI = get_secret("NEO4J_URI")
NEO4J_USERNAME = get_secret("NEO4J_USERNAME")
NEO4J_PASSWORD = get_secret("NEO4J_PASSWORD")

# Neo4j Graph
graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
)
