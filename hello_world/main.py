from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client =OpenAI(
    api_key="AIzaSyCpLTX6QsX9FDf8EPBVRA4FPvQcstg20GY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"user", "content":"Hey, I am Neelam More! Nice to meet you"}
    ]
)

print(response.choices[0].message.content)