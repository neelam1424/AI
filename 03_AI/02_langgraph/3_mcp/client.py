from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()


import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"Python",
            "args": [ "mathserver.py"],
            "transport":"stdio",
            },

            "weather":{
                "url":"http://localhost:8000/mcp",
                "tansport":"streamable_http",
            }
        }
    )


    import os
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


    tools = await client.get_tools()
    model = OpenAI(model="gpt-4.1")
    agent = create_react_agent(
        model,tools
    )