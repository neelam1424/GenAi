
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client=OpenAI(
     api_key="AIzaSyCpLTX6QsX9FDf8EPBVRA4FPvQcstg20GY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)



SYSTEM_PROMPT="""  
You're an expert AI Assistant in resolving user queries using chain of thought
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be muliple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given JSON output format
- Only run one step at a time
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times and finally OUTPUt (which is going to the displayed to the user).


Output JSON Format:
{"step":"START" | "PLAN" | "OUTPUT", "content": "string" }


Example:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: {"step":"PLAN":"content":"Seems like user is interested in math problem"}
PLAN: {"step":"PLAN":"content":"looking at the problem, we shoukd solve this using BODMAS method"}
PLAN: {"step":"PLAN":"content":"Yes, the BODMAS is correct thing to be done here"}
PLAN: {"step":"PLAN":"content":"first we must multiply 3 * 5 which is 15"}
PLAN: {"step":"PLAN":"content":"Now the new equation is 2 + 15 / 10"}
PLAN: {"step":"PLAN":"content":"We must perform divide that is 15 / 10 = 1.5"}
PLAN: {"step":"PLAN":"content":"Now the new equation is 2 + 1.5"}
PLAN: {"step":"PLAN":"content":"Now finally lets perform the add 3.5"
PLAN: {"step":"PLAN":"content":"Great, we have solved and finally left with 3.5 as ans"}
OUTPUT: {"step":"OUTPUT":"content":"3.5"}
"""


response=client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user", "content":"hey, write a code to add n numbers in json"},
        {"role":"assistant","content": json.dumps({"step": "START", "content": "hey, write a code to add n numbers in json"})},
        
        {"role":"assistant","content": json.dumps({
  "step": "PLAN",
  "content": "The user wants code to add 'n' numbers, presented in JSON format. I will provide a Python solution. The plan is to: 1. Create a Python function to sum a list of numbers. 2. Include example usage. 3. Format the complete code as a string in the final JSON output."
})}
        
    ]
    
)

print(response.choices[0].message.content)
