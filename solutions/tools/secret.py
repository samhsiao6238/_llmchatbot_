# secret.py
# 原本沒有導入 dotenv，這裡要添加
import os
from dotenv import load_dotenv
#
load_dotenv()

# 新增判斷函數
def get_secret(key):
    try:
        # 嘗試從 Streamlit secrets 獲取敏感資訊
        return st.secrets[key]
    except AttributeError:
        # 如果 st.secrets 沒有該鍵或 st.secrets 未被設定，則從環境變量中獲取
        return os.getenv(key)