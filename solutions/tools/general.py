# general.py
from langchain.tools import Tool
from solutions import llm

tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=llm.invoke,
        return_direct=True
    )
]
