# bot.py
import streamlit as st
# 寫入訊息到 session state
from utils import write_message
# 從自訂模組中導入生成回應的函數
from solutions.agent import generate_response

# 設置頁面配置，包括標題和頁面圖標
st.set_page_config("Ebert", page_icon=":movie_camera:")

# 檢查 session_state 中是否已存在 `messages`` 鍵
if "messages" not in st.session_state:
    # 如果不存在就進行初始化
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi, How can I help you?",
        },
    ]


# 定義一個處理提交動作的函數
def handle_submit(message):
    # 顯示加載動畫
    with st.spinner("Thinking..."):
        print(f'===bot.py -> message(用戶)：類型 {type(message)}:{message}===')
        # 調用 generate_response 來處理消息並獲取回應
        response = generate_response(message)
        # 使用 write_message 函數將回應寫入 session_state
        write_message("assistant", response)


print('=01_bot.py=')
# 遍歷 session_state 中的 messages 並逐一顯示
for message in st.session_state.messages:
    print(f'===bot.py -> message(機器)：類型 {type(message)}:{message}===')
    write_message(
        # 消息的角色
        message["role"],
        # 消息内容
        message["content"],
        # 這裡設置 save 為 False，表示不將此消息再次保存到 session_state
        save=False
    )

# 利用 Streamlit 的 chat_input 獲取用戶輸入
# 假如用戶輸入的不是空白
if prompt := st.chat_input("怎麼了？有話就說吧～"):
    # 使用自訂 `utils` 中的函數，將用戶的輸入作為一條消息保存
    write_message("user", prompt)
    # 處理用戶輸入的消息
    handle_submit(prompt)
