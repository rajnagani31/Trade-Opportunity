from openai import OpenAI
from dotenv import load_dotenv
import json
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TradeLLM")

client = OpenAI()


SYSTEM_PROMPT = """ 
    You are a financial analysis assistant. Your task is to analyze trade opportunities in various sectors based on the latest market data and trends. 
    Provide insights, forecasts, and recommendations in a markdown format suitable for generating reports.
"""

def chat_with_openai(query):
    response = client.responses.create(
        model="gpt-5",
        instructions=SYSTEM_PROMPT,
        tools=[
            {"type": "web_search"},
            {
                "type": "function",
                "name": "creat_md_file_report",
                "description": "send relvent data for create md file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data": {"type": "string"},
                        "query": {"type": "string"},
                    },
                    "required": ["data"]
                }
            }
        ],
        tool_choice="auto",
        input=query,
    )

    print("LLM response:", response)

    for item in response.output:
        if item.type == "reasoning":
            continue

        if item.type == "function_call":
            print('yes')
            if item.name == "creat_md_file_report":
                args = json.loads(item.arguments)
                print('args for md file report:', args)
                creat_md_file_report(**args)

        elif item.type == "output_text":
            print(item.text)


# This function Used by LLM to create markdown file report
def creat_md_file_report(**args):
    data = args.get("data", None)
    query = args.get("query", "")
    OUTPUT_FILE = f'Trade_report_{query}.md'

    logger.info(f"Creating markdown report: {OUTPUT_FILE}")
    if data:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(data)
    else:
        logger.error("No data provided for markdown report creation.")