import os
from openai import OpenAI
from dotenv import load_dotenv
from schemas import CompanyEnrichment
from ai.website_extractor import extract_website_text

load_dotenv()

my_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=my_key)


def summarize_company(website_text):

    response = client.responses.parse(
    model="gpt-5.6-luna",
    input=f"""
    Using only the website content below, thoroughly analyze the company.
       
    Return:
        - A concise company summary
        - A list of the main products or services
        - Useful B2B sales insights
        - Whether it looks like a potentially valuable prospect and why

    Website content:
    {website_text}
    """,
    text_format=CompanyEnrichment

)
    return response.output_parsed


website_text = extract_website_text("https://www.gametz.com")
summary = summarize_company(website_text)

print(summary)