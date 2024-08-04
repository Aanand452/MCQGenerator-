import os
import json
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file,get_table_data

# importing necessary packages packages from langchain 
from langchain.llms import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback


#load environment variables from -.env file 

load_dotenv()

#Access the environment variables from .env file 
KEY=os.getenv("OPENAI_API_KEY")

llm =ChatOpenAI(openai_api_key=KEY,model="gpt-3.5-turbo",temperature=0.3)