import os
import json
from dotenv import find_dotenv, load_dotenv
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from app.structures.available_tasks import tasks
from app.utils.alternative_parser import alternative_parser
from app.utils.message_parser import message_parser

#load env file
_ = load_dotenv(find_dotenv())

#args schema
class ApiInput(BaseModel):
    message: str = Field(description="Should be the message in JSON format that you were asked to generate")

#get endpoint & set headers
endpoint = os.getenv('API_URL')

headers = {
    'apikey':os.getenv('SUPABASE_KEY'),
    'Authorization': os.getenv('SUPBASE_TOKEN')
}

#define tool
def api_task(message:str) -> str:
    try:
        data = message_parser(message)
        task = data.get('task')
        if task in tasks:
            tasks[task](payload=data,headers=headers,endpoint=endpoint)
        else:
            print('Task not registered')
    except json.JSONDecodeError:
        print('Output parser failed, trying loads')
        try:
            data = alternative_parser(message)
            task = data.get('task')
            if task in tasks:
                tasks[task](payload=data,headers=headers,endpoint=endpoint)
            else:
                print('task not registered')
        except json.JSONDecodeError:
            print('both methods failed')
            return None

ApiTask = StructuredTool.from_function(
    func=api_task,
    name="API_task",
    description="Do CRUD tasks in an API",
    args_schema=ApiInput,
    return_direct=True
)