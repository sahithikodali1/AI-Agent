import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

#load environment variables
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not openai_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables!")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables!")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", 
                 temperature=0.7,
                 google_api_key=GEMINI_API_KEY     # pass the key explicitly
                 )

def run_llm(prompt: str):
    response = llm.invoke(prompt)
    return response.content

# if __name__ == "__main__":
#     test_prompt = "Say hello to Sahi in a fun way."
#     print(run_llm(test_prompt))