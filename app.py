import streamlit as st

st.set_page_config(
    page_title="Customer Login History",
    layout="wide"
)

# ------------------------
# DATA
# ------------------------

events = [
    {
        "status": "error",
        "date": "15 Jul 2026 14:23",
        "title": "Password reset started - new password not set, attempted to set trusted device unsuccessful",
        "next_steps": [
            "Advise the customer to set a new password if the password reset screen is still open.",
            "If the screen has been closed, ask the customer to restart the password reset process.",
            "The trusted device request has not been saved because the password reset was not completed.",
            "The customer will need to select Trusted Device again once logged on."
        ]
    },
    {
        "status": "success",
        "date": "15 Jul 2026 12:45",
        "title": "Password reset complete - logged in - device not trusted"
    },
    {
        "status": "success",
        "date": "14 Jul 2026 18:20",
        "title": "Password reset complete - logged in - trusted device"
    }
]

latest = events[0]

# ------------------------
# SESSION STATE
# ------------------------

if "expanded" not in st.session_state:
    st.session_state.expanded = False


def toggle():
    st.session_state.expanded = not st.session_state.expanded


# ------------------------
# HEADER
# ------------------------

st.markdown(
    """
    <div style="
        font-size:18px;
        font-weight:600;
        color:#1f355e;
        margin-bottom:20px;">
        Earlier this month
        <span style="color:#5d6d8f;font-weight:400;">
            &nbsp;&nbsp;July 2026
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------
# CARD
# ------------------------

col1, col2 = st.columns([1, 12])

with col1:
    st.markdown(
        """
        <div style="
            width:65px;
            height:65px;
            border-radius:50%;
            border:2px solid #d7deeb;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:30px;">
            🛡️
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div style="
            border:2px solid #d7deeb;
            border-radius:20px;
            padding:30px;
            background:white;">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;">

                <div style="
                    font-size:22px;
                    font-weight:700;
                    color:#1f355e;">
                    Your Login History
                </div>

                <div style="
                    color:#7081a3;
                    font-size:18px;">
                    {latest['date']}
                </div>

            </div>

            <div style="margin-top:25px;">

                <span style="
                    background:#fdecec;
                    color:#d62828;
                    padding:10px 16px;
                    border-radius:25px;
                    font-weight:600;">
                    {latest['title']}
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
