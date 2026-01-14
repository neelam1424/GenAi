

from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI()

def get_weather(city:str):
    url=f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"the weather in {city} is {response.text}"
    
    return "Something went wrong"
    

def main():
    print("Chat started. Type 'exit' to quit.")

    while True:
        user_query = input("> ")

        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_query}
            ]
        )

        print("bot:", response.choices[0].message.content)
    print(get_weather("goa"))

if __name__ == "__main__":
    main()
