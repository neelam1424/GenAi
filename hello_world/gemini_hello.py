from google import genai

client=genai.Client(
    api_key="AIzaSyCpLTX6QsX9FDf8EPBVRA4FPvQcstg20GY"
)


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)