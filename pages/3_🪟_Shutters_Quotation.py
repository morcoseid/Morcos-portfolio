import streamlit as st

st.set_page_config(page_title="Shutters Automation", page_icon="🪟", layout="wide")

st.markdown("""
<div style='background-color: #f8f9fa; padding: 15px; border-left: 5px solid #1a73e8; border-radius: 5px; margin-bottom: 20px;'>
    <h4 style='margin-top: 0;'>👋 Hi, I'm Morcos Eid | Cost Engineer & Architect</h4>
    <p style='margin-bottom: 0;'>I specialize in bridging the gap between technical estimation and software automation. By engineering custom tools from scratch, I empower cross-functional teams to eliminate bottlenecks, negotiate clear scopes with clients, and deliver mathematically flawless proposals.</p>
</div>
""", unsafe_allow_html=True)

st.title("🪟 Shutters Bulk Quotation System")

st.markdown("""
### 📌 The Challenge
Calculating shutter quotes required manually parsing varying window dimensions, selecting the correct motor specifications from an external catalog, calculating dry costs, and manually formatting PDF documents. 

### 🚀 The Solution
I developed a robust **Google Apps Script** solution with an interactive HTML menu interface. The system ingests window sizes and quantities, automatically resolves dry-cost margins and flat rates for remote controls against an agreed motor catalog, and executes a brute-force retry mechanism to bypass API limits during PDF generation.

### 📊 The Impact
The tool features a "Bulk Run" option that processes multiple tabs simultaneously across 5 distinct product options. It successfully turned a tedious, multi-hour calculation task into a 1-click execution.
""")

st.divider()

st.subheader("🖥️ Interactive Menu Simulation")
st.info("🔒 *This replicates the custom HTML dialog built into the Google Sheets environment.*")

st.markdown("#### Quote Automation - Select Actions")
st.checkbox("1. Generate Safety - Zinconium 5.5cm")
st.checkbox("2. Generate Normal - BK 5cm")
st.checkbox("3. Generate Manual - Normal BK 5cm")
st.checkbox("7. Bulk Run 'All 5 Options' - All Tabs")
st.checkbox("9. Create Motor & Cost Study - Active Tab")

st.button("▶️ Run Selected Actions (Disabled)", disabled=True)
st.success("✅ Process Complete: Successfully generated 15 quotes across 3 tabs.")
