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

    with st.container(border=True):

        col_title, col_date = st.columns([4, 1])

        with col_title:
            st.subheader("Your Login History")

        with col_date:
            st.write("")
            st.write(latest["date"])

        st.error(latest["title"])


if st.button(
    "▼ Expand Login History"
    if not st.session_state.expanded
    else "▲ Collapse Login History",
    use_container_width=True,
):
    st.session_state.expanded = not st.session_state.expanded


if st.session_state.expanded:

    st.markdown("## Events")

    for event in events:

        if event["status"] == "error":
            st.error(event["title"])
        else:
            st.success(event["title"])

        st.caption(event["date"])

        if "next_steps" in event:

            st.markdown("### Next Steps")

            for step in event["next_steps"]:
                st.markdown(f"- {step}")

        st.divider()
