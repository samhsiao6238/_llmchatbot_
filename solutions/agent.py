# agent.py
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from solutions.llm import llm
from solutions.tools.vector import kg_qa
from solutions.tools.finetuned import cypher_qa

# tools 的列表定義了其他狀況發生時的設定
tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=llm.invoke,
        return_direct=True,
    ),
    Tool.from_function(
        name="Cypher QA",
        description="Provide info about movies questions using Cypher",
        func=cypher_qa,
        return_direct=True,
    ),
    Tool.from_function(
        name="Vector Search Index",
        description="Provides info about movie plots using Vector Search",
        func=kg_qa,
        return_direct=True,
    ),
]

# 調用 langchain 函數 ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=5,
    return_messages=True,
)

# 調用 langchain 函數 hub.pull() 生成
agent_prompt = hub.pull("hwchase17/react-chat")
# 調用 langchain 函數 create_react_agent，傳入 `llm`、`tools`、`Agent 的回應`
agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agent=agent, tools=tools, memory=memory, verbose=True
)

# 這是原本的函數，改寫添加了判斷的機制
# def generate_response(prompt):
#     response = agent_executor.invoke({"input": prompt})
#     return response["output"]


def generate_response(prompt):
    try:
        # 回應
        response = agent_executor.invoke({"input": prompt})
        #
        if isinstance(response['output'], dict):
            print('=agent.py -> 備註：回應是一個 dict=')
            response_output = ''
            for item in response['output']:
                if response_output:
                    response_output += ', '
                response_output += str(item)
        else:
            # 回應訊息
            print('=agent.py -> 備註：回應訊息=')
            response_output = str(response['output'])
        return response_output
    except Exception as e:
        print('=agent.py -> 備註：回應發生錯誤=')
        return f"Error processing response: {str(e)}"
