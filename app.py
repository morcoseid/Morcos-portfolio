import streamlit as st
import pandas as pd

st.set_page_config(page_title="O West Quotation Engine", page_icon="🏢", layout="wide")

st.title("🏢 O West Extra Works Quotation Engine")

# --- PROJECT CONTEXT (STAR Method) ---
st.markdown("""
### 📌 The Challenge
Pricing luxury villas and residential modifications involved complex, manual Excel workflows that were prone to human error and created significant bottlenecks during peak request volumes.

### 🎯 The Goal
To build a scalable, foolproof digital tool that standardizes BOQ preparation, eliminates mathematical errors, and empowers sales and engineering teams to generate quotes instantly.

### 🚀 The Solution
I developed a full-stack Python/Streamlit web application that dynamically groups pricing matrices. It processes up to 18 luxury package variants simultaneously, calculates VAT and profit margins, and uses Webhooks to auto-generate official PDF proposals directly in Google Workspace.

### 📊 The Impact
**Reduced quoting time from hours to 3 minutes**, guaranteeing 100% pricing accuracy and maximizing the volume of processed orders for the Extra Work Department.
""")

st.divider()

# --- SANITIZED MOCKUP SECTION ---
st.subheader("🖥️ Interactive UI Mockup")
st.info("🔒 **Data Privacy Notice:** This is a sanitized simulation of the user interface. Live database connections, actual pricing logic, and client data have been completely removed to protect company confidentiality.")

# Fake Input Controls to show your UI design skills
col1, col2 = st.columns(2)
with col1:
    st.selectbox("Select Unit Typology (Simulated)", ["3 Bedrooms + Nanny", "4 Bedrooms", "Standalone Villa"])
    st.selectbox("Select Request Type (Simulated)", ["Furniture Package - Luxury", "Roof Room Extension", "Double Height Closing"])
    st.button("🚀 Generate Official Proposal (Disabled)", disabled=True)

with col2:
    st.metric("Estimated Turnaround Time", "3 Minutes", "-95% vs Manual Process")
    st.metric("Mathematical Accuracy", "100%", "Zero Error Tolerance")

st.markdown("### 📊 Sample Output Structure")
st.caption("A simulated example of the automatically generated BOQ matrix prior to PDF compilation.")

# Fake Data to show you know how to handle Pandas/DataFrames in Streamlit
mock_data = pd.DataFrame({
    "No.": [1, 2, 3],
    "Description": [
        "Supply & Install Master Bedroom Furniture as per approved design (Sanitized Data)", 
        "Reception & Living Room Fit-out Package (Sanitized Data)", 
        "Electrical Works & AC Allocation (Sanitized Data)"
    ],
    "Unit": ["LS", "LS", "LS"],
    "QTY": [1.0, 1.0, 1.0],
    "Rate (EGP)": ["XXX,XXX.XX", "XXX,XXX.XX", "XX,XXX.XX"],
    "Total Amount (EGP)": ["XXX,XXX.XX", "XXX,XXX.XX", "XX,XXX.XX"]
})

st.dataframe(
    mock_data, 
    hide_index=True, 
    use_container_width=True,
    column_config={
        "No.": st.column_config.NumberColumn(width="small"),
        "Description": st.column_config.TextColumn(width="large")
    }
)
