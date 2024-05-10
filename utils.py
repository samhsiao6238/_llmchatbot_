# utility.py
import streamlit as st


# 參數：角色、內容、是否儲存
def write_message(role, content, save=True):
    print('=utility.py -> 調用 `write_message` 處理訊息=')
    """
    這是一個輔助函數，將訊息保存到 `session state`，然後將訊息寫入 UI
    """
    # 如果 save 參數為 True，則將訊息添加到 session_state 中的 messages 列表
    if save:
        print('=utility.py -> 添加訊息到 session_state=')
        st.session_state.messages.append({
            # 消息的角色，例如 'user' 或 'assistant'
            "role": role,
            # 消息的內容
            "content": content
        })
    else:
        print('=utility.py -> 不添加訊息到 session_state=')

    # 寫入 UI
    # 使用 Streamlit 的 chat_message 上下文管理器來顯示訊息
    # 這將根據訊息的角色來在界面上分配適當的樣式
    with st.chat_message(role):
        # 使用 markdown 函數將內容格式化後顯示在 UI 上
        st.markdown(content)
