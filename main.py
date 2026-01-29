from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Summarize the following text:\n{text}"
    )
    return response.output_text

if __name__ == "__main__":
    user_text = input("Enter text to summarize:\n")
    summary = summarize(user_text)
    print("\nSummary:\n", summary)
