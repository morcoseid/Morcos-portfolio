import streamlit as st
import pandas as pd

st.set_page_config(page_title="O West Quotation Engine", page_icon="🏢", layout="wide")

st.markdown("""
<div style='background-color: #f8f9fa; padding: 15px; border-left: 5px solid #1a73e8; border-radius: 5px; margin-bottom: 20px;'>
    <h4 style='margin-top: 0;'>👋 Hi, I'm Morcos Eid | Cost Engineer & Architect</h4>
    <p style='margin-bottom: 0;'>I specialize in bridging the gap between technical estimation and software automation. By engineering custom tools from scratch, I empower cross-functional teams to eliminate bottlenecks, negotiate clear scopes with clients, and deliver mathematically flawless proposals.</p>
</div>
""", unsafe_allow_html=True)

st.title("🏢 O West Extra Works Quotation Engine")

st.markdown("""
### 📌 The Challenge
Pricing luxury villas and residential modifications involved complex, manual Excel workflows. Defining precise scopes with clients and sales teams was creating significant bottlenecks and exposing the company to pricing risks during peak request volumes.

### 🚀 The Solution
I developed a full-stack Python/Streamlit web application. The engine dynamically groups complex pricing matrices, processes up to 18 luxury package variants simultaneously, automatically calculates VAT and profit margins, and uses Webhooks to generate official PDF proposals directly in Google Workspace.

### 📊 The Impact
**Reduced quoting turnaround time from several hours to 3 minutes.** Guaranteed 100% mathematical accuracy, mitigated commercial risk, and maximized the volume of processed orders.
""")

st.divider()

st.subheader("🖥️ Interactive UI Mockup")
st.info("🔒 *Data Privacy Notice: Live database connections, actual pricing logic, and client data have been removed from this simulation to protect company confidentiality.*")

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Select Unit Typology (Simulated)", ["3 Bedrooms + Nanny", "4 Bedrooms", "Standalone Villa"])
    st.selectbox("Select Request Type (Simulated)", ["Furniture Package - Luxury", "Roof Room Extension", "Double Height Closing"])
    st.button("🚀 Generate Official Proposal (Disabled)", disabled=True)

with col2:
    st.metric("Estimated Turnaround Time", "3 Minutes", "-95% vs Manual Process")
    st.metric("Mathematical Accuracy", "100%", "Zero Error Tolerance")
    
st.markdown("#### Sample Output Structure")
mock_data = pd.DataFrame({
    "No.": [1, 2, 3],
    "Description": ["Supply & Install Master Bedroom Furniture", "Reception & Living Room Fit-out", "Electrical Works & AC Allocation"],
    "Unit": ["LS", "LS", "LS"],
    "QTY": [1.0, 1.0, 1.0],
    "Rate (EGP)": ["XXX,XXX.XX", "XXX,XXX.XX", "XX,XXX.XX"]
})
st.dataframe(mock_data, hide_index=True, use_container_width=True)
