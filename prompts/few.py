#Few Shot prompting


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI(
     api_key="AIzaSyCpLTX6QsX9FDf8EPBVRA4FPvQcstg20GY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#Few Shot Prompting: Directly giving the instructions to the model and few examples to the model
SYSTEM_PROMPT="""
You should only and only answer the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry.  

Rule:
-Strictly follow the output in Json format

Output Format:
{{
    "code":"string" or "None",
    "isCodingQuestion":boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{"code}": null, "isCodingQuestion": false}

Q:Hey, Write a code in python for adding two numbers.
A: {{"code": def add(a,b):
       return a + b ,"isCodingQuestion": false }}

"""


response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user", "content":"hey, write a code to add n numbers in js"}
    ]
    
)

print(response.choices[0].message.content)

#2. Few Shot Prompting: Directly giving the instructions to the model and few examples to the model