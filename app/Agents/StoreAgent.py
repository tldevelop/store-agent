from .Components.graph import Agent
from .Prompts.system_prompt import system_prompt
from app.tools.store_tool import ApiTask
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from langgraph.checkpoint.sqlite import SqliteSaver

#Generate chat model from HuggingFace Meta Llama 3.3 70B

model_id = "meta-llama/Llama-3.3-70B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=model_id,
    task="text-generation",
    temperature=0.5,
    max_new_tokens=520,
    do_sample=False,
)

chat_model = ChatHuggingFace(llm=llm)

#Define thread for conversation persistence
thread = {'configurable':{'thread_id':'1'}}

#define agent executor
def agent_executor(user_request:str) -> str:
    with SqliteSaver.from_conn_string(':memory:') as memory:
        assistant = Agent(
            model=chat_model,
            tools=[ApiTask],
            system=system_prompt,
            checkpointer=memory
        )
        request = [HumanMessage(content=user_request)]
        result = assistant.graph.invoke({'messages':request},thread)
    
    return result['messages'][-1].content