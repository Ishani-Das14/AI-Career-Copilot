import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* ==========================================
   GOOGLE FONT
========================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


/* ==========================================
   GLOBAL
========================================== */

html,
body,
.stApp {
    font-family: "Inter", sans-serif;
}

.block-container{
    max-width:1250px;
    padding-top:1rem;
    padding-bottom:2rem;
}


/* ==========================================
   HIDE STREAMLIT UI
========================================== */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

[data-testid="stToolbar"]{
    display:none !important;
}

[data-testid="stDecoration"]{
    display:none !important;
}


/* ==========================================
   HEADINGS
========================================== */

h1{
    font-weight:800 !important;
    letter-spacing:-1px;
}

h2,h3{
    font-weight:700 !important;
}


/* ==========================================
   CARDS
========================================== */

[data-testid="stVerticalBlockBorderWrapper"]{

    background:#171B22;

    color:#C9D1D9;

    border:1px solid #2D3748;

    border-radius:18px;

    padding:20px;

    transition:0.25s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover{

    border-color:#3B82F6;
}


/* ==========================================
   BUTTONS
========================================== */

.stButton > button{

    width:100%;

    height:50px;

    border:none;

    border-radius:12px;

    background:#2563EB;

    color:white;

    font-weight:600;

    transition:.25s;
}

.stButton > button:hover{

    background:#1D4ED8;

    transform:translateY(-2px);

    box-shadow:0 0 18px rgba(37,99,235,.35);
}


/* ==========================================
   FILE UPLOADER
========================================== */

[data-testid="stFileUploaderDropzone"]{

    border:2px dashed #3B82F6;

    border-radius:16px;

    background:#111827;

    padding:24px;

    transition:.25s;
}

[data-testid="stFileUploaderDropzone"]:hover{

    border-color:#60A5FA;

    background:#162033;
}


/* ==========================================
   INPUTS
========================================== */

.stTextInput input{

    border-radius:12px;
}


/* ==========================================
   CHAT
========================================== */

[data-testid="stChatMessage"]{

    border-radius:16px;
}


/* ==========================================
   METRICS
========================================== */

[data-testid="stMetricValue"]{

    font-weight:700;
}


/* ==========================================
   PROGRESS BAR
========================================== */

.stProgress > div > div{

    background:#3B82F6;
}


/* ==========================================
   DIVIDER
========================================== */

hr{

    border:1px solid #2D3748;

    margin-top:28px;

    margin-bottom:28px;
}

</style>
""",
        unsafe_allow_html=True,
    )