import streamlit as st

# Initialize session state variables
if "questions" not in st.session_state:
    st.session_state.questions = [
    # Data Format: Raw vs Processed
    {"question": "What data type is a .CSV or an .XLSX file most often used for?", "options": ["Raw", "Processed"], "answer": "Processed"},
    {"question": "What type of data is stored in a Relational Database like that which forms the back-office of SETS?", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "What data type is stored in these types of files: .PARQUET, .TXT, .JSON?", "options": ["Raw", "Processed"], "answer": "Raw"},
    {"question": "What data type can a Power BI Dashboard be used for?", "options": ["Raw", "Processed"], "answer": "Processed"},

    # Data Type Identification
    {"question": "What data format is \"20250714T13:22-0500\"?", "options": ["String", "Integer", "Float", "Datetime"], "answer": "Datetime"},
    {"question": "What data format is \"Hello World\"?", "options": ["String", "Integer", "Float", "Datetime"], "answer": "String"},
    {"question": "What data format is \"42\"?", "options": ["String", "Integer", "Float", "Datetime"], "answer": "Integer"},
    {"question": "What data format is \"3.14\"?", "options": ["String", "Integer", "Float", "Datetime"], "answer": "Float"},

    # Internal vs External Data Source
    {"question": "To Revenue Scotland, what kind of a data source is SETS?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "To Revenue Scotland, what kind of data system is SETS?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is SETS hosted on an internal or external data infrastructure?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is NEC's infrastructure internal or external?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Are the SETS back-office files held in NEC Cloud?", "options": ["Yes", "No"], "answer": "Yes"},

    {"question": "Is Oracle Cloud HR an data source, system or infrastructure?", "options": ["Source", "System", "Infrastructure"], "answer": "System"},
    {"question": "Is Oracle Cloud HR an internal or external data system?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is the data held in Oracle Cloud HR an internal or external data source?", "options": ["Internal", "External"], "answer": "Internal"},
    
    {"question": "Is a CSV file provided to you by Stats & MI team a data source, system or infrastructure?", "options": ["Source", "System", "Infrastructure"], "answer": "Source"},
    {"question": "Is Microsoft Power BI a data source, system or infrastructure?", "options": ["Source", "System", "Infrastructure"], "answer": "System"},
    {"question": "Is a Power BI dashboard built by for you from the CSV file which Stats & MI gave you an internal or external data system?", "options": ["Internal", "External"], "answer": "Internal"},
    
    {"question": "What kind of data source is a spreadsheet created by your colleague?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "Is SharePoint an internal or external data system?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "Is this file on the cloud: a spreadsheet created by your colleague which you uploaded to SharePoint?", "options": ["Yes", "No"], "answer": "Yes"},

    {"question": "To Revenue Scotland, what kind of a data source is the data from National Records of Scotland (NRS)?", "options": ["Internal", "External"], "answer": "External"},
    {"question": "You saved data from NRS in an Excel file on your laptop. This file is stored on an external data system.", "options": ["True", "False"], "answer": "False"},
    {"question": "You saved the same data from NRS in an Excel file on Teams. This file is stored on an external data system.", "options": ["True", "False"], "answer": "True"},
    {"question": "You saved the same data from NRS as a CSV file on a shared network drive. This file is stored on an external data system", "options": ["True", "False"], "answer": "False"},

    # Internal vs External Data Infrastructure
    {"question": "Will RSCloud contain internal or external data sources?", "options": ["Internal", "External", "Both"], "answer": "Both"},
    {"question": "Is RSCloud an internal or external data system?", "options": ["Internal", "External"], "answer": "Internal"},
    {"question": "Will RSCloud be hosted on internal or external data infrastructure?", "options": ["Internal", "External"], "answer": "External"},
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
