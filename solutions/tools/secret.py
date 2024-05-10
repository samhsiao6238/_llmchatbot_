# secret.py
import streamlit as st
import os


# 自訂函數
def get_secret(key):
    # 檢查是否在 Streamlit 雲端環境中運行，Streamlit 雲端環境會設置特定的環境變量
    if "STREAMLIT_SHARING_MODE" in os.environ:
        # 在 Streamlit 雲端，使用 st.secrets 讀取配置
        try:
            return st.secrets[key]
        except KeyError:
            print(f"Key {key} not found in Streamlit secrets.")
    else:
        # 在本機環境，嘗試從 .env 文件讀取配置
        from dotenv import load_dotenv

        load_dotenv()  # 讀取 .env 文件中的環境變量
        secret_value = os.getenv(key)
        if secret_value is not None:
            return secret_value
        else:
            print(f"Key {key} not found in environment variables.")
