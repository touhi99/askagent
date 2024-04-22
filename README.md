### AskAgent - Mac Terminal LLM Agents

This is a simple Mac/Ubuntu terminal assistant with agents capable of various tasks. Purpose is to quickly with `askagent` command able to get answer without looking through via ChatGPT interface or searching in Google. Ideally, it can also execute unix command if permissed but use at your own risk. But for simple command i.e., "Go to desktop and list all the pdf's there" it can execute `['cd ~/Desktop', 'ls *.pdf']` and show the results. 

## Installation

This project uses Poetry for package management. To install Poetry, follow the instructions [here](https://python-poetry.org/docs/#installation).

Once you have Poetry installed, you can install the project dependencies with:

```
poetry install
poetry shell
askagent
```

## Configuration

It requires certain environment variables to be set in order to operate correctly. Below are the necessary environment variables and a brief description of their use:

- `OPENAI_API_KEY`: If OpenAI is going to be used for the model.
- `GROQ_API_KEY`: If Groq (Llama-70B) is going to be used for the model. 
- `WOLFRAM_ALPHA_APPID`: (optional) Complex calculation, Math etc.
- `SERPAPI_API_KEY`: (optional) Searching Google search
- `TAVILY_API_KEY`: (optional) Searching Tavily API search

Export the API Keys to use the app (for example):
```
export OPENAI_API_KEY='your_api_key'
export SERPAPI_API_KEY='your_database_url'
```

For development, rename the `.env.example` to `.env` and update the API KEYS

## Usage

To run the tool, execute the following from the command line:

```askagent "What is the capital of France?"```

### **Argument Details**

The program takes the following arguments 

- `--model`: An optional argument that specifies which LLM model to use. Default is `openai` (alternative options, groq (running llama70B))
- `--verbose`: An optional argument that specifies to a boolean to check intermediate steps. Default is `False`
- `prompt`: A required positional argument that specifies the prompt for the LLM

For example:

``` askagent --model groq --verbose True  "Find me any latest Diffusion video paper" ```

Some other further example:
```
askagent  "command to check mac cpu/gpu processing"
askagent --verbose=True  "Give me the command to find any pdf in my system"
askagent --verbose=True  "what does latest AI news say??"
askagent --verbose True  "what's the weather at Munich now?"
askagent --verbose=True  "what causes lung cancer? Get from medical expert"
askagent "give me top 5  Mrbeast channel video url"
askagent "What is 2x+5 = -3x + 7? and why?"
askagent "what's the command to see free space on my mac?"
```

## TODO:
- Add Llama3 local (from Ollama)
- Add more tools