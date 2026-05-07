import requests
import pandas as pd
import streamlit as st
from sympy.physics.vector.printing import params

st.set_page_config(page_title="LeadGen MVP")

st.title("AI Sales Lead Generator")

st.write("Get business leads with a click of a button.")

location = st.text_input(
    "Location",
    placeholder="Dallas, TX"
)

keyword = st.text_input(
    "Business Type",
    placeholder="Plumbing"
)


min_rating = st.slider(
    "Minimum Rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
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

    response = requests.get(
        "http://127.0.0.1:8000/leads",
        params=params
    )

    data = response.json()

    if len(data) == 0:
        st.warning("No Leads found")
    else:
        df = pd.DataFrame(data)
        st.success(f"{len(data)} Leads found!")

        st.dataframe(df)