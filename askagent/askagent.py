import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_groq.chat_models import ChatGroq
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from askagent.llm_tools import load_conditional_tools
import argparse

def main():
    parser = argparse.ArgumentParser(description="Enter your question:")
    parser.add_argument('--model', type=str, default='openai', help="Which LLM Model? Default is Groq (llama3)")
    parser.add_argument('--verbose', type=bool, default=False, help="If verbose should be printed")
    parser.add_argument('prompt', type=str, help="Prompt for LLM")
    args = parser.parse_args()

    #Load LLMs
    if args.model.lower()=='groq':
        llm = ChatGroq(temperature=0.2, streaming=False, groq_api_key=os.environ["GROQ_API_KEY"], model_name="llama3-70b-8192") #model_name="mixtral-8x7b-32768"
    elif args.model.lower()=='openai':
        llm = ChatOpenAI(model_name="gpt-4-turbo", streaming=True, openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.0)
    elif args.model.lower()=='llama3':
        llm = OllamaFunctions(model="llama3")


    # Load tools
    try:
        tools = load_conditional_tools(llm)
    except:
        print("Error fetching tools")

    #Define prompts
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """You are an Unix terminal assistant.
            Use your tools to answer questions. If you do not have a tool to answer the question, say so. 
            Return only the answers. e.g.,
            human: command for showing all the files (including hidden) in current directory
            AI: ls -la
            """),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )

    #Define agents
    try:
        agent = create_openai_tools_agent(llm, tools, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=args.verbose)
        result = agent_executor.invoke({"input": args.prompt})
        print(result['output'])
    except:
        print("Error Agent call")

if __name__ == "__main__":
    print("Script is running directly")
    main()