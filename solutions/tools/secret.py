# secret.py
# 原本沒有導入 dotenv，這裡要添加
import os
from dotenv import load_dotenv

# 判斷環境取得密鑰
def get_secret(key):
    try:
        # 嘗試從 Streamlit secrets 獲取敏感資訊
        return st.secrets[key]
    except AttributeError:
        # 如果 st.secrets 沒有該鍵或 st.secrets 未被設定，則從環境變量中獲取
        return os.getenv(key)

# 改寫
# def get_secret(key):
#     # 檢查是否在 Streamlit 雲端環境中運行，Streamlit 雲端環境會設置特定的環境變量
#     if 'STREAMLIT_SHARING_MODE' in os.environ:
#         # 在 Streamlit 雲端，使用 st.secrets 讀取配置
#         try:
#             return st.secrets[key]
#         except KeyError:
#             print(f"Key {key} not found in Streamlit secrets.")
#     else:
#         # 在本機環境，嘗試從 .env 文件讀取配置
#         from dotenv import load_dotenv
#         load_dotenv()  # 讀取 .env 文件中的環境變量
#         secret_value = os.getenv(key)
#         if secret_value is not None:
#             return secret_value
#         else:
#             print(f"Key {key} not found in environment variables.")