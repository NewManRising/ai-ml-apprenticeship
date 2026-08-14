import os
from openai import OpenAI
from dotenv import load_dotenv
from schemas import CompanyEnrichment
from ai.website_extractor import extract_website_text

load_dotenv(override=True)

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
        - A useful sales insight describing a potential business need, opportunity, or angle
        - A qualification assessment explaining whether this looks like a potentially valuable prospect and why

    Do not invent facts that are not supported by the website content.

    Website content:
    {website_text}
    """,
    text_format=CompanyEnrichment

)
    return response.output_parsed