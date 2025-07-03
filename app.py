
import streamlit as st
from database import create_table, insert_defect, get_all_defects
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

create_table()

st.title("🛠️ Smart Defect Enlister & Tracker")

st.header("📥 Log a New Defect")
with st.form("defect_form"):
    module = st.text_input("Module Name")
    description = st.text_area("Defect Description")
    severity = st.selectbox("Severity", ["Low", "Medium", "High"])
    status = st.selectbox("Status", ["Open", "In Progress", "Closed"])
    assigned_to = st.text_input("Assigned To")
    date_reported = st.date_input("Reported On", date.today())
    resolution_date = st.date_input("Resolution Date", date.today())
    submit = st.form_submit_button("Submit Defect")

    if submit:
        insert_defect(str(date_reported), module, description, severity, status, assigned_to, str(resolution_date))
        st.success("✅ Defect logged successfully!")

st.header("📋 All Defects Logged")
rows = get_all_defects()
df = pd.DataFrame(rows, columns=[
    "ID", "Reported Date", "Module", "Description", "Severity",
    "Status", "Assigned To", "Resolution Date"
])
st.dataframe(df)

st.header("📊 Defects by Severity")
if not df.empty:
    severity_counts = df["Severity"].value_counts()
    fig, ax = plt.subplots()
    severity_counts.plot(kind='bar', color=['green', 'orange', 'red'], ax=ax)
    ax.set_ylabel("Number of Defects")
    ax.set_title("Severity-wise Defect Count")
    st.pyplot(fig)
