import os
import io
import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

st.set_page_config(page_title="LeadGen v03")

# Initialize session state once
if "leads" not in st.session_state:
    st.session_state["leads"] = None

st.title("Intelligent Sales Lead Generator")

st.write("Get AI-Powered Business Leads With A Click Of A Button.")

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

# Demo Mode
demo_mode = st.sidebar.toggle("Demo Mode", value=True)
if demo_mode:
    st.info("Running in Demo Mode with sample data")




# Generate Leads

if st.button("Generate Leads"):

    params = {
        "location": location,
        "keyword": keyword,
        "min_rating": min_rating,
        "min_reviews": min_reviews,
        "demo": demo_mode
    }

    with st.spinner("Generating leads...hang tight", show_time=True):
        try:
            response = requests.get(
                f"{API_BASE_URL}/leads",
                params=params,
                timeout=60
            )
            response.raise_for_status()
            data = response.json()

        # Save results so they survive Streamlit reruns
            st.session_state["leads"] = data

        except requests.RequestException as e:
            st.error(f"Network Error. Try again later. {e}")


# Displaying Results

if st.session_state["leads"] == []:

    st.warning("No Leads found")


elif st.session_state["leads"]:

    data = st.session_state["leads"]

    df = pd.DataFrame(data)

    st.success(f"{len(data)} Leads found!")


# Lead Table

    display_columns = [
        "Name",
        "Rating",
        "Reviews",
        "Score",
        "Qualification",
        "Website"
    ]

    display_df = df[display_columns]

    st.dataframe(
        display_df,
        width="stretch"
    )


   # AI Lead Details

    selected_name = st.selectbox(
        "Select a lead to view AI insights",
        options=df["Name"].tolist(),
        index=None,
        placeholder="Choose a company..."
    )

    if selected_name:

        selected_lead = df[
            df["Name"] == selected_name
        ].iloc[0]

        st.subheader(selected_lead["Name"])

        st.write("### Company Summary")
        company_summary = selected_lead["Company_Summary"]

        if pd.isna(company_summary):
            st.write("No AI enrichment available.")
        else:
            st.write(company_summary)


        st.write("### Products / Services")
        products_services = selected_lead["Products_Services"]

        if products_services:
            for item in products_services:
                st.write(f"- {item}")
        else:
            st.write("No AI enrichment available.")

        st.write("### Sales Insight")
        sales_insight = selected_lead["Sales_Insight"]

        if pd.isna(sales_insight):
            st.write("No AI enrichment available.")
        else:
            st.write(sales_insight)


        st.write("### Qualification Reason")
        qualification_reason = selected_lead["Qualification_Reason"]

        if pd.isna(qualification_reason):
            st.write("No AI enrichment available.")
        else:
            st.write(qualification_reason)


# Excel Download

    # Stores binary Excel data in memory
    excel_buffer = io.BytesIO()

    # Writes the full dataframe to the in-memory Excel file
    df.to_excel(
        excel_buffer,
        index=False,
        engine="openpyxl"
    )

    excel_buffer.seek(0)

    st.download_button(
        label="Download Excel File",
        data=excel_buffer.getvalue(),
        file_name="leads.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        icon=":material/download:",
        on_click="ignore"
    )