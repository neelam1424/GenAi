#Zero Shot Prompting :- giving instructions directly


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI(
     api_key="AIzaSyCpLTX6QsX9FDf8EPBVRA4FPvQcstg20GY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#Zero Shot Prompting: Directly giving the instruction to model
SYSTEM_PROMPT="You should only and only answer the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry.  "


response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user", "content":"hey, can you tell me a joke"}
    ]
    
)

print(response.choices[0].message.content)
#1. Zero -shot Prompting: The model is given a direct question or task without prior examples