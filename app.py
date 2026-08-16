import streamlit as st

st.set_page_config(
    page_title="Morcos Eid | Cost Engineer & Automation Developer",
    page_icon="🏗️",
    layout="wide"
)

st.title("Morcos Eid")
st.subheader("Quantity Surveyor | Architect | Cost Engineer")
st.write("📍 Cairo, Egypt | 📞 015 017 36365 | ✉️ morcoseid@gmail.com")
st.markdown("[LinkedIn](https://linkedin.com/in/morcos-eid)")

st.divider()

st.header("Professional Summary")
st.write("""
Cost Engineer and architectural professional with 5 years of regional experience across Egypt and the UAE, specializing in complex extra-work cost estimation and scope management for massive residential communities. Currently completing my PRMG certification at AUC.

What distinguishes my approach is a strong proactive ability to engineer custom workflow automations (Python, Streamlit, Google Apps Script). By bridging the gap between technical estimation and software automation, I eliminate manual bottlenecks, guarantee mathematical accuracy across complex pricing matrices, and empower cross-functional teams to streamline project delivery from the pre-construction phase through completion.
""")

st.divider()

st.header("Projects & Automations")
st.write("Explore my quotation engines and estimation tools below:")

# Embed your live O West app directly on the page
st.subheader("🏢 O West Extra Works Quotation Engine")
st.components.v1.iframe(
    "https://quote-generator-e6hjx58cyaw8jnscti9pmm.streamlit.app/?embed=true",
    height=800,
    scrolling=True
)
