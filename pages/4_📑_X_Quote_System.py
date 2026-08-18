import streamlit as st

st.set_page_config(page_title="X-Quote System", page_icon="📑", layout="wide")

st.markdown("""
<div style='background-color: #f8f9fa; padding: 15px; border-left: 5px solid #1a73e8; border-radius: 5px; margin-bottom: 20px;'>
    <h4 style='margin-top: 0;'>👋 Hi, I'm Morcos Eid | Cost Engineer & Architect</h4>
    <p style='margin-bottom: 0;'>I specialize in bridging the gap between technical estimation and software automation. By engineering custom tools from scratch, I empower cross-functional teams to eliminate bottlenecks, negotiate clear scopes with clients, and deliver mathematically flawless proposals.</p>
</div>
""", unsafe_allow_html=True)

st.title("📑 The X-Quote Automation System")

st.markdown("""
### 📌 The Challenge
Scaling the estimation department required bringing on team members who did not have deep, specialized cost engineering backgrounds. We needed a way to translate complex estimation logic into a simple, accessible interface.

### 🚀 The Solution
I architected a combined automation system using **Google Workspace APIs**. The pipeline consists of three core components:
1. **The Organizer:** A Google Form that takes raw sales/engineer input and expands it into a structured database.
2. **The Generator:** An Apps Script engine that reads the organized data, injects it into Google Doc templates, formats the tables dynamically, and logs the output.
3. **The Webhook:** A listener that allows external applications to trigger document generation and PDF conversions remotely.

### 📊 The Impact
By converting complex estimation into a guided, form-based workflow, **I empowered a cross-functional team to generate professional, accurate proposals entirely on their own.** This system became the backbone for all future automation scaling within the department.
""")

st.divider()

st.subheader("🖥️ Workflow Architecture")
st.info("🔒 *A simplified visualization of the API-driven data pipeline.*")

st.markdown("""
*   📝 **Sales/Engineer Input:** Submits basic request via Google Forms.
*   🗄️ **Data Organizer:** Apps Script parses dimensions, matches unit IDs, and assigns correct pricing rules in Google Sheets.
*   ⚙️ **Logic Engine:** Calculates VAT, applies terms and conditions, and assigns sequential serial numbers.
*   📄 **Document Generation:** Webhook triggers Google Docs to clone a template, format tables, and export a read-only PDF.
*   📂 **Delivery:** Files are saved to secure Drive folders and linked back to the master database.
""")
