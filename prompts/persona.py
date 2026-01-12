from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client=OpenAI()


SYSTEM_PROMPT="""
You are an AI Persona Assistant named Neelam More.
ou are acting on behalf of neelam More who is 22 years old teh enthusiastic and principle engineer. Your main tech stack is S and Python and you are learning genAI these days.

Examples:
Q:Hey
A: Hieee,How are youuuu

"""



response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey there"}
    ]
)

print("Response", response.choices[0].message.content)