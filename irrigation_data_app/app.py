import streamlit as st
import pandas as pd

st.set_page_config(page_title="Irrigation Data Collection Tool", layout="centered")

st.title("🚜 Irrigation Data Collection Tool")
st.markdown("Designed for field staff to input and submit irrigation scheme data across multiple EPAs.")

# Dropdown for EPA selection
epa = st.selectbox("📍 Select EPA", ["Khudze EPA", "Mwanza EPA", "Thambani EPA"])

# Scheme Info
scheme_name = st.text_input("🏞️ Scheme Name")
location = st.text_input("🌍 Location")
area_ha = st.number_input("📐 Area (ha)", min_value=0.0, format="%.2f")

# Beneficiaries
st.markdown("### 👥 Beneficiary Details")
num_male = st.number_input("Number of Male Beneficiaries", min_value=0, step=1)
num_female = st.number_input("Number of Female Beneficiaries", min_value=0, step=1)
total_beneficiaries = num_male + num_female
st.success(f"✅ Total Beneficiaries: {total_beneficiaries}")

# Infrastructure Needed
st.markdown("### 🛠️ Infrastructure Needs")
infra = st.multiselect(
    "Select infrastructure components needed:",
    ["Weir", "Main Canal", "Secondary Canal", "Pipe Distribution", "Reservoir", "Tank", "Pump", "Other"]
)
infra_notes = st.text_area("Additional Infrastructure Notes")

# Technical Needs
st.markdown("### 📐 Technical Support Needs")
survey_needed = st.checkbox("Detailed Topographic Survey Needed")
design_needed = st.checkbox("Engineering Design Required")

# Submit Data
if st.button("✅ Submit"):
    st.success("Data submitted successfully!")
    submitted_data = {
        "EPA": epa,
        "Scheme Name": scheme_name,
        "Location": location,
        "Area (ha)": area_ha,
        "Male Beneficiaries": num_male,
        "Female Beneficiaries": num_female,
        "Total Beneficiaries": total_beneficiaries,
        "Infrastructure": ", ".join(infra),
        "Infra Notes": infra_notes,
        "Survey Needed": survey_needed,
        "Design Needed": design_needed
    }
    st.json(submitted_data)

# Export summary (optional)
with st.expander("📊 Summary Report (Downloadable in future version)"):
    st.write("Coming soon: export to Excel or Word for reporting and review.")
