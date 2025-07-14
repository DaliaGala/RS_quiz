import streamlit as st

# Initialize session state variables
if "questions" not in st.session_state:
    st.session_state.questions = [
    # Data Format: Raw vs Processed
    {"question": "Parquet", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "Relational Database", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "TXT", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "JSON", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "CSV", "options": ["Raw", "Processed"], "answer": "Processed"},
    {"question": "Excel", "options": ["Raw", "Processed"], "answer": "Processed"},
    {"question": "Power BI Dashboard", "options": ["Raw", "Processed"], "answer": "Processed"},

    # Data Type Identification
    {"question": "\"2025-07-14\"", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Datetime"},
    {"question": "\"Hello World\"", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "String"},
    {"question": "42", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Integer"},
    {"question": "3.14", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Float"},
    {"question": "true", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Boolean"},
    {"question": "[1, 2, 3]", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Array/List"},

    # Internal vs External Data Source
    {"question": "A spreadsheet created by a colleague", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "A program that collects office temperature daily", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "A public website where users submit data", "options": ["Internal", "External"], "answer": "External"},
    {"question": "A government open data portal", "options": ["Internal", "External"], "answer": "External"},
    {"question": "A survey conducted by your team", "options": ["Internal", "External"], "answer": "Internal"},

    # Internal vs External Data System
    {"question": "Oracle HR", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Microsoft Suite", "options": ["Internal", "External"], "answer": "External"},
    {"question": "SharePoint", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Teams", "options": ["Internal", "External"], "answer": "External"},
    {"question": "A cloud app built by your IT team", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "Power BI dashboard built by your colleagues", "options": ["Internal", "External"], "answer": "Internal"},

    # Internal vs External Data Infrastructure
    {"question": "A server hosted by your IT department", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "A website and database hosted by contractors", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Cloud infrastructure leased and managed by your IT team", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "Cloud infrastructure fully managed by NEC", "options": ["Internal", "External"], "answer": "External"},

    # Is This File on the Cloud?
    {"question": "Excel file on my laptop", "options": ["Yes", "No"], "answer": "No"},
    {"question": "CSV file on a shared network drive", "options": ["Yes", "No"], "answer": "No"},
    {"question": "File in SharePoint", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "File in RSCloud", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "SETS back-office files", "options": ["Yes", "No"], "answer": "Yes"}
]

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = None

@st.fragment
def question_fragment():
    """
        Fragment to display a question and capture the user's response.
    """
    question_data = st.session_state.questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}/{len(st.session_state.questions)}")
    st.write(question_data['question'])

    selected_option = st.radio('Choose an answer: ', question_data['options'])
    if st.button('Submit'):
        if selected_option == question_data['answer']:
            st.session_state.feedback = ('success', 'Correct! 🎉')
            st.session_state.score += 1
        else:
            st.session_state.feedback = ("error", f"Wrong! The correct answer was: {question_data['answer']}")

        if st.session_state.current_question + 1 < len(st.session_state.questions):
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.current_question = None
            st.rerun()

@st.fragment
def feedback_fragment():
    """
    Fragment to display feedback messages.
    """
    if st.session_state.feedback:
        msg_type, msg_content = st.session_state.feedback
        if msg_type == "success":
            st.success(msg_content)
        elif msg_type == "error":
            st.error(msg_content)
        st.session_state.feedback = None

@st.fragment
def score_fragment():
    """
        Fragment to display the user’s current score.
    """
    st.metric('Current Score', st.session_state.score)

@st.fragment
def restart_quiz_fragment():
    """
        Fragment to restart the quiz.
    """
    if st.button('Restart Quiz'):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.rerun()

# Main application
st.title('Interactive Quiz App')

feedback_fragment()

if st.session_state.current_question is not None:
    score_fragment()
    question_fragment()
else:
    st.subheader('Quiz Finished! 🎉')
    st.write(f"Your final score is {st.session_state.score}/{len(st.session_state.questions)}.")
    restart_quiz_fragment()
