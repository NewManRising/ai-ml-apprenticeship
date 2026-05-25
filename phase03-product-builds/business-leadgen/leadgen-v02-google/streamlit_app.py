import os
import requests
import pandas as pd
import streamlit as st



st.set_page_config(page_title="LeadGen v02")

st.title("Sales Lead Generator")

st.write("Get business leads with a click of a button.")

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
    with st.spinner("Generating Leads...", show_time=True):
        # Local Development Only
         response = requests.get(
            "http://127.0.0.1:8000/leads",
           params=params
          )
         # response = requests.get(
         #  f"{API_BASE_URL}/leads",
         #  params=params
         # )

         response.raise_for_status()

         data = response.json()

         if len(data) == 0:
            st.warning("No Leads found")
         else:
            df = pd.DataFrame(data)
            st.success(f"{len(data)} Leads found!")

            st.dataframe(df, width="stretch")

            excel_response = requests.get(
                f"{API_BASE_URL}/leads/excel",
                params=params
            )

            excel_response.raise_for_status()

            st.download_button(
                label="Download Excel File",
                data=excel_response.content,
                file_name="leads.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                icon=":material/download:"
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
