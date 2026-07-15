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

# ------------------------
# HEADER
# ------------------------

st.markdown("### Earlier this month   July 2026")

# ------------------------
# CARD
# ------------------------

outer_left, outer_middle, outer_right = st.columns([1, 8, 3])

with outer_left:
    st.markdown("# 🛡️")

with outer_middle:

    with st.container(border=True):

        title_col, date_col, arrow_col = st.columns([6, 2, 1])

        with title_col:
            st.subheader("Your Login History")

        with date_col:
            st.write("")
            st.write(latest["date"])

        with arrow_col:
            st.write("")

            arrow = "⌃" if st.session_state.expanded else "⌄"

            if st.button(arrow, key="toggle"):
                st.session_state.expanded = not st.session_state.expanded
                st.rerun()

        st.error(latest["title"])

# ------------------------
# EXPANDED CONTENT
# ------------------------

if st.session_state.expanded:

    st.markdown("### EVENTS")

    for event in events:

        icon_col, content_col = st.columns([1, 12])

        with icon_col:

            if event["status"] == "error":
                st.markdown("### 🛡️")
            else:
                st.markdown("### ✅")

        with content_col:

            if event["status"] == "error":

                st.markdown(
                    f"""
                    <div style="
                        background:#FCE8E8;
                        color:#C62828;
                        padding:10px 14px;
                        border-radius:10px;
                        font-size:14px;">
                        {event['title']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:

                st.markdown(
                    f"""
                    <div style="
                        background:#E8F5E9;
                        color:#2E7D32;
                        padding:10px 14px;
                        border-radius:10px;
                        font-size:14px;">
                        {event['title']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.caption(event["date"])

            if "next_steps" in event:

                st.markdown("##### Next Steps")

                for step in event["next_steps"]:
                    st.markdown(
                        f"""
                        <div style="font-size:13px; margin-bottom:4px;">
                        • {step}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        st.divider()
