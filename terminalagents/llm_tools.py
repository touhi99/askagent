import os
from langchain.agents import load_tools
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.tools import YouTubeSearchTool

def load_conditional_tools(llm):
    # List of always required tools
    tools_to_load = ['requests_all', 'terminal', 'wikipedia', 'human', 'llm-math', 'arxiv']
    
    # Conditional tool loading based on environment variables
    if 'SERPAPI_API_KEY' in os.environ:
        tools_to_load.append('serpapi')
    if 'WOLFRAM_ALPHA_APPID' in os.environ:
        tools_to_load.append('wolfram-alpha')
    
    tools = load_tools(tools_to_load, llm=llm, allow_dangerous_tools=True)
    
    tools.append(PubmedQueryRun())
    tools.append(YouTubeSearchTool())
    if 'TAVILY_API_KEY' in os.environ:
        tools.append(TavilySearchResults())

    return tools