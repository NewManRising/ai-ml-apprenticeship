import os
from openai import OpenAI
from dotenv import load_dotenv
from ai.website_extractor import extract_website_text

load_dotenv()

my_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=my_key)


def summarize_company(website_text):

  response = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
           Using only the website content below, write a concise
        one-paragraph summary of what this company does.

        Website content:
        {website_text}
        """

)
  return response.output_text

website_text = extract_website_text("https://www.gametz.com")
summary = summarize_company(website_text)

print(summary)