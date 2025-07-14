import streamlit as st

# Define quiz questions and answers
quiz = {
    "Data Format: Raw vs Processed": [
        ("Parquet", "Raw"),
        ("Relational Database", "Raw"),
        ("TXT", "Raw"),
        ("JSON", "Raw"),
        ("CSV", "Processed"),
        ("Excel", "Processed"),
        ("Power BI Dashboard", "Processed")
    ],
    "Data Type Identification": [
        ("\"2025-07-14\"", "Datetime"),
        ("\"Hello World\"", "String"),
        ("42", "Integer"),
        ("3.14", "Float"),
        ("true", "Boolean"),
        ("[1, 2, 3]", "Array/List")
    ],
    "Internal vs External Data Source": [
        ("A spreadsheet created by a colleague", "Internal"),
        ("A program that collects office temperature daily", "Internal"),
        ("A public website where users submit data", "External"),
        ("A government open data portal", "External"),
        ("A survey conducted by your team", "Internal")
    ],
    "Internal vs External Data System": [
        ("Oracle HR", "External"),
        ("Microsoft Suite", "External"),
        ("SharePoint", "External"),
        ("Teams", "External"),
        ("A cloud app built by your IT team", "Internal"),
        ("Power BI dashboard built by your colleagues", "Internal")
    ],
    "Internal vs External Data Infrastructure": [
        ("A server hosted by your IT department", "Internal"),
        ("A website and database hosted by contractors", "External"),
        ("Cloud infrastructure leased and managed by your IT team", "Internal"),
        ("Cloud infrastructure fully managed by NEC", "External")
    ],
    "Is This File on the Cloud?": [
        ("Excel file on my laptop", "No"),
        ("CSV file on a shared network drive", "No"),
        ("File in SharePoint", "Yes"),
        ("File in RSCloud", "Yes"),
        ("SETS back-office files", "Yes")
    ]
}

st.title("Data Systems & Cloud Knowledge Quiz")

score = 0
total = 0

# Iterate through each section
for section, questions in quiz.items():
    st.header(section)
    for question, correct_answer in questions:
        total += 1
        user_answer = st.radio(
            f"Q: {question}",
            options=["Raw", "Processed", "String", "Integer", "Float", "Datetime", "Boolean", "Array/List", "Internal", "External", "Yes", "No"],
            key=f"{section}-{question}"
        )
        if user_answer == correct_answer:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer: {correct_answer}")

# Display final score
st.markdown("---")
st.subheader(f"Your Final Score: {score} out of {total}")
