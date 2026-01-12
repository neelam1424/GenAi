
from dotenv import load_dotenv
from openai import OpenAI
import json
import os

load_dotenv()

client=OpenAI(
     api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)



SYSTEM_PROMPT = """
You are an expert assistant.
Solve the problem using step-by-step reasoning internally.
Do NOT reveal your reasoning.

Return ONLY valid JSON in this format:
{"answer": "string"}
"""



print("\n\n\n")


message_history=[
    {"role":"system","content":SYSTEM_PROMPT}
]

user_query = input("Type here:-  ")
message_history.append({"role":"user", "content": user_query})



response=client.chat.completions.create(
        model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=message_history
        
    )
    
    
raw_result = response.choices[0].message.content
result=json.loads(raw_result)

print("Answer:", result["answer"])
   
   
print("\n\n\n")


    

