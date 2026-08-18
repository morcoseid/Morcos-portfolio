import streamlit as st

st.set_page_config(
    page_title="Morcos Eid | Cost Engineer & Automation Developer",
    page_icon="🏗️",
    layout="wide"
)

# --- HEADER SECTION ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Morcos Eid")
    st.subheader("Quantity Surveyor | Architect | Cost Engineer")
    st.markdown("📍 Cairo, Egypt | 📞 015 017 36365 | ✉️ morcoseid@gmail.com")
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/morcos-eid)")

with col2:
    # Placeholder for your professional photo
    st.info("Cost Engineering & Python Automation")

st.divider()

# --- PROFESSIONAL SUMMARY ---
st.header("Professional Summary")
st.write("""
Cost Engineer and architectural professional with 5 years of regional experience across Egypt and the UAE, specializing in complex extra-work cost estimation and scope management for massive residential communities. Currently advancing my expertise through the PRMG Project Management Diploma at the American University in Cairo (AUC). 

What distinguishes my approach is a proactive drive to engineer custom workflow automations (Python, Streamlit, Google Apps Script) from scratch. By bridging the gap between technical estimation and software automation, I eliminate manual bottlenecks, guarantee mathematical accuracy across complex pricing matrices, and empower cross-functional teams to streamline project delivery from the pre-construction phase through completion.
""")

st.divider()

# --- PROFESSIONAL EXPERIENCE ---
st.header("Professional Experience")

with st.expander("🏗️ ORASCOM DEVELOPMENT (O West) | Cost Engineer", expanded=True):
    st.write("**Jul 2026 - Present** (Previously Quantity Surveyor: Sep 2024 - Jul 2026)")
    st.write("""
    - **Cost Estimation & Scope Management:** Manage BOQ scope and cost estimation for client modification requests (pools, roof rooms, landscapes, interior finishes). Negotiate custom variations directly with sales teams and clients.
    - **Digital Integration:** Calibrate advanced measurement workflows across AutoCAD, Bluebeam Revu, and PlanSwift to translate bespoke client needs into cost-effective, standardized products.
    - **Process Optimization via Automation:** Engineered multiple custom applications (O West Quotation Engine, Shutters Bulk Quoter, Automated BOQ Matrix, X-Quote) using Python and Google Apps Script to reduce quoting time from hours to minutes.
    """)

with st.expander("🏢 IMPERIUM GROUP | Quantity Surveyor & Estimator"):
    st.write("**Jun 2022 - Sep 2024 (UAE - Remotely)**")
    st.write("""
    - Prepared highly detailed Bill of Quantities (BOQs) for over 150 projects, primarily focusing on luxury villas, encompassing interior fit-out, exterior, landscape, civil, and renovation scopes.
    - Employed value engineering principles and managed Variation Orders (VOs) to optimize costs and timelines.
    - Implemented PlanSwift and customized templates to drastically expedite the BOQ preparation process.
    """)

with st.expander("📐 MODERN INTERIORS | Quantity Surveyor"):
    st.write("**Aug 2021 - Jun 2022 (Giza, Egypt)**")
    st.write("""
    - Executed precise Quantity Take-Offs for consultant review and invoicing on high-profile projects, including Monai & Le Flandrine at Water Way, Kent College School, and residential units at SODIC.
    - Coordinated with procurement, tendering, and commercial teams to facilitate the rapid issuance of POs and VOs.
    """)

with st.expander("🎓 AL MASAR Training Center | Operations Manager & Team Leader"):
    st.write("**Jun 2024 - Sep 2025 (KSA - Remotely)**")
    st.write("""
    - Spearheaded the recruitment, onboarding, and mentoring of a multidisciplinary team of 5 instructors across 6 training rounds.
    - Previously served as an Instructor (Feb 2023 - May 2024), delivering high-impact training in Interior Design Principles, AutoCAD, Revit, and 3ds Max.
    """)

st.divider()

# --- EDUCATION & SKILLS TABS ---
tab1, tab2 = st.tabs(["🎓 Education & Certifications", "💻 Technical Skills"])

with tab1:
    st.subheader("The American University in Cairo (AUC)")
    st.write("**Diploma in Project Management (PRMG) | 2023 - Present**")
    st.write("- *Courses:* Project Planning & Control, Resource Management, Budgeting & Financial Control, Cost Estimation, Project Bids & Contracts.")
    
    st.subheader("Cairo University | Faculty of Engineering")
    st.write("**Bachelor’s Degree in Architecture | 2016 - 2021**")
    st.write("- *Graduation Project:* Excellent | *Cumulative:* Good")

with tab2:
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("#### Architecture & Estimation")
        st.write("AutoCAD, Bluebeam Revu, PlanSwift, Revit, 3ds Max, Lumion")
    with col_b:
        st.markdown("#### Programming & Automation")
        st.write("Python, Streamlit, Pandas, Google Apps Script, REST APIs / Webhooks")
    with col_c:
        st.markdown("#### Business & Data")
        st.write("Advanced Excel, Google Workspace, DataFrames, Client Negotiation")

st.info("👈 **Please use the sidebar menu to explore interactive demos of my engineering automation tools.**")
