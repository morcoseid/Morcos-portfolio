import streamlit as st
import pandas as pd

st.set_page_config(page_title="Automated BOQ Matrix", page_icon="📊", layout="wide")

st.markdown("""
<div style='background-color: #f8f9fa; padding: 15px; border-left: 5px solid #1a73e8; border-radius: 5px; margin-bottom: 20px;'>
    <h4 style='margin-top: 0;'>👋 Hi, I'm Morcos Eid | Cost Engineer & Architect</h4>
    <p style='margin-bottom: 0;'>I specialize in bridging the gap between technical estimation and software automation. By engineering custom tools from scratch, I empower cross-functional teams to eliminate bottlenecks, negotiate clear scopes with clients, and deliver mathematically flawless proposals.</p>
</div>
""", unsafe_allow_html=True)

st.title("📊 Automated BOQ Matrix Generator")

st.markdown("""
### 📌 The Challenge
Transforming raw architectural measurements into a fully priced, client-ready Bill of Quantities (BOQ) was a fragmented process requiring constant manual cross-referencing between opening schedules, room selections, and pricing databases.

### 🚀 The Solution
I designed a specialized tool chest in **Bluebeam Revu** to standardize measurement outputs. I then architected a Python engine using **Pandas DataFrames** to extract the Bluebeam CSVs, cross-reference them with Excel-based material selections and opening schedules, and dynamically calculate areas, deductions, and margins. 

### 📊 The Impact
Outputs a highly structured, dynamically formatted 4-level hierarchical BOQ in Excel. This single source of truth completely eliminated manual data entry errors.
""")

st.divider()

st.subheader("🖥️ Simulated Output Structure")
st.info("🔒 *Showing a sanitized DataFrame simulation of the 4-level hierarchical logic.*")

mock_boq_data = pd.DataFrame({
    "No.": ["1", "1.1", "1.1.1", "1.1.1.A", "1.1.1.B"],
    "Item": [
        "FINISHES", 
        "Wall Finishes", 
        "Paint", 
        "Supply & Apply Plastic Paint - For: Master Bedroom [Code: P-01]", 
        "Supply & Apply Plastic Paint - For: Living Room [Code: P-01]"
    ],
    "Unit": ["", "", "", "m²", "m²"],
    "Qty": ["", "", "", 45.5, 62.0],
    "Rate (EGP)": ["", "", "", "XX.XX", "XX.XX"]
})

st.dataframe(mock_boq_data, hide_index=True, use_container_width=True)
st.button("⬇️ Download Sanitized Sample Excel (Disabled)", disabled=True)
