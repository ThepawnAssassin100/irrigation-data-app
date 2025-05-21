import streamlit as st
from supabase import create_client, Client

# Initialize Supabase client with secrets (set these in Streamlit secrets)
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Irrigation Data Collection Tool", layout="centered")

st.title("🚜 Irrigation Data Collection Tool")
st.markdown("Designed for field staff to input and submit irrigation scheme data across multiple EPAs.")

# EPA selection
epa = st.selectbox("📍 Select EPA", ["Khudze EPA", "Mwanza EPA", "Thambani EPA"])

# Scheme info
scheme_name = st.text_input("🏞️ Scheme Name")
location = st.text_input("🌍 Location")
area_ha = st.number_input("📐 Area (ha)", min_value=0.0, format="%.2f")

# Beneficiaries
st.markdown("### 👥 Beneficiary Details")
num_male = st.number_input("Number of Male Beneficiaries", min_value=0, step=1)
num_female = st.number_input("Number of Female Beneficiaries", min_value=0, step=1)
total_beneficiaries = num_male + num_female
st.success(f"✅ Total Beneficiaries: {total_beneficiaries}")

# Infrastructure
st.markdown("### 🛠️ Infrastructure Needs")
infra = st.multiselect(
    "Select infrastructure components needed:",
    ["Weir", "Main Canal", "Secondary Canal", "Pipe Distribution", "Reservoir", "Tank", "Pump", "Other"]
)
infra_notes = st.text_area("Additional Infrastructure Notes")

# Technical needs
st.markdown("### 📐 Technical Support Needs")
survey_needed = st.checkbox("Detailed Topographic Survey Needed")
design_needed = st.checkbox("Engineering Design Required")

# Submit data
if st.button("✅ Submit"):
    if not scheme_name or not location:
        st.error("Please fill in Scheme Name and Location before submitting.")
    else:
        data = {
            "epa": epa,
            "scheme_name": scheme_name,
            "location": location,
            "area_ha": area_ha,
            "num_male": num_male,
            "num_female": num_female,
            "total_beneficiaries": total_beneficiaries,
            "infrastructure": ", ".join(infra),
            "infra_notes": infra_notes,
            "survey_needed": survey_needed,
            "design_needed": design_needed
        }
        response = supabase.table("irrigation_submissions").insert(data).execute()
        if response.status_code == 201:
            st.success("Data submitted successfully to Supabase!")
        else:
            st.error(f"Error submitting data: {response.status_code}")
