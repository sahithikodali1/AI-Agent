import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

#load environment variables
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables!")

llm = ChatOpenAI(model_name="gpt-4", 
                 temperature=0.7,
                 api_key=openai_key     # pass the key explicitly
                 )

def run_llm(prompt: str):
    return llm(prompt)

