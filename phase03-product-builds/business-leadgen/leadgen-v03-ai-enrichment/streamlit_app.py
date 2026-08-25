import os
import io
import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")


st.set_page_config(page_title="LeadGen v03")

st.title("Intelligent Sales Lead Generator")

st.write("Get business leads powered by AI with a click of a button.")

col1, col2 = st.columns(2, border=True)

with col1:
    location = st.text_input(
        "Location",
        placeholder="Los Angeles, CA"
    )
    min_rating = st.slider(
        "Minimum Rating",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.1
    )

with col2:
    keyword = st.text_input(
        "Business Type",
        placeholder="Roofing"
    )

    min_reviews = st.slider(
        "Minimum Reviews",
        min_value=0,
        max_value=500,
        value=50
    )

if st.button("Generate Leads"):

    params = {
        "location": location,
        "keyword": keyword,
        "min_rating": min_rating,
        "min_reviews": min_reviews
    }
    with st.spinner("Generating leads...hang tight", show_time=True):
        # Local Development Only
        # response = requests.get(
        #   "http://127.0.0.1:8000/leads",
        #   params=params
        # )

         response = requests.get(
           f"{API_BASE_URL}/leads",
            params=params,
            timeout=60
            )

         response.raise_for_status()

         data = response.json()

         if len(data) == 0:
            st.warning("No Leads found")
         else:
            df = pd.DataFrame(data)
            st.success(f"{len(data)} Leads found!")

            st.dataframe(df, width="stretch")

         # Stores binary data in memory
            excel_buffer = io.BytesIO()


           # excel_response = requests.get(
           #     f"{API_BASE_URL}/leads/excel",
           #     params=params,
           #     timeout=60
           # )

            # Writes file to xlsx
            df.to_excel(excel_buffer, index=False, engine="openpyxl")
            excel_buffer.seek(0)

            st.download_button(
                label="Download Excel File",
                data=excel_buffer.getvalue(),
                file_name="leads.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                icon=":material/download:",
                on_click="ignore"
            )

       # Local Development Only
       #  with open("leads.xlsx", "rb") as file:
       #     st.download_button(
       #         label="Download Excel File",
       #         data=file,
       #         file_name="leads.xlsx",
       #         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
       #         icon=":material/download:"

       #     )
