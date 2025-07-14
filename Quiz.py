import streamlit as st

# Initialize session state variables
if "questions" not in st.session_state:
    st.session_state.questions = [
    # Data Format: Raw vs Processed
    {"question": "What data type is Parquet?", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "What data type is a Relational Database?", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "What data type is TXT?", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "What data type is JSON?", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "What data type is CSV?", "options": ["Raw", "Processed"], "answer": "Processed"},
    {"question": "What data type is Excel?", "options": ["Raw", "Processed"], "answer": "Processed"},
    {"question": "What data type is a Power BI Dashboard?", "options": ["Raw", "Processed"], "answer": "Processed"},

    # Data Type Identification
    {"question": "What data format is \"2025-07-14\"?", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Datetime"},
    {"question": "What data format is \"Hello World\"?", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "String"},
    {"question": "What data format is 42?", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Integer"},
    {"question": "What data format is 3.14?", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Float"},
    {"question": "What data format is true?", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Boolean"},
    {"question": "What data format is [1, 2, 3]?", "options": ["String", "Integer", "Float", "Datetime", "Boolean", "Array/List"], "answer": "Array/List"},

    # Internal vs External Data Source
    {"question": "What kind of data source is a spreadsheet created by a colleague?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "What kind of data source is a program that collects office temperature daily?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "What kind of data source is a public website where users submit data?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "What kind of data source is a government open data portal?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "What kind of data source is a survey conducted by your team?", "options": ["Internal", "External"], "answer": "Internal"},

    # Internal vs External Data System
    {"question": "Is Oracle HR an internal or external data system?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is Microsoft Suite an internal or external data system?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is SharePoint an internal or external data system?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is Teams an internal or external data system?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is a cloud app built by your IT team an internal or external data system?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "Is a Power BI dashboard built by your colleagues an internal or external data system?", "options": ["Internal", "External"], "answer": "Internal"},

    # Internal vs External Data Infrastructure
    {"question": "Is a server hosted by our IT department an internal or external data infrastructure?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "Is a website and database hosted by contractors an internal or external data infrastructure?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is cloud infrastructure leased and managed by our IT team an internal or external data infrastructure?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "Is cloud infrastructure fully managed by NEC an internal or external data infrastructure?", "options": ["Internal", "External"], "answer": "External"},

    # Is This File on the Cloud?
    {"question": "Is this file on the cloud: Excel file on my laptop?", "options": ["Yes", "No"], "answer": "No"},
    {"question": "Is this file on the cloud: CSV file on a shared network drive?", "options": ["Yes", "No"], "answer": "No"},
    {"question": "Is this file on the cloud: File in SharePoint?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is this file on the cloud: File in RSCloud?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is this file on the cloud: SETS back-office files?", "options": ["Yes", "No"], "answer": "Yes"}
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
