# llm.py
# 導入自訂函數
from solutions.tools.secret import get_secret
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
# 載入庫
# import os
# from dotenv import load_dotenv
# 載入環境變數
# load_dotenv()

# 註解原本取的變數的方式
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_MODEL = os.getenv("OPENAI_MODEL")
# 改寫
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")
OPENAI_MODEL = get_secret("OPENAI_MODEL")

# 建立 ChatOpenAI 實體
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model=OPENAI_MODEL,
)

# OpenAIEmbeddings 是用來生成和處理嵌入向量（embeddings）
# 這些嵌入向量是從使用 OpenAI 模型（如 GPT-4）生成的文本中獲取的
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
