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

    with outer_middle:

        st.markdown("### EVENTS")

        for event in events:

            icon_col, content_col = st.columns([1, 7])
    
            with icon_col:
    
                if event["status"] == "error":
                    st.markdown("### 🛡️")
                else:
                    st.markdown("### ✅")
    
            with content_col:

                banner_colour = "#FCE8E8" if event["status"] == "error" else "#E8F5E9"
                text_colour = "#C62828" if event["status"] == "error" else "#2E7D32"
            
                st.markdown(
                    f"""
                    <div style="
                        background:{banner_colour};
                        color:{text_colour};
                        padding:10px 14px;
                        border-radius:10px;
                        font-size:14px;
                        display:flex;
                        justify-content:space-between;
                        align-items:center;">
            
                        <span>{event['title']}</span>
            
                        <span style="
                            font-size:12px;
                            color:#666666;
                            white-space:nowrap;">
                            {event['date']}
                        </span>
            
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            
                if "next_steps" in event:
            
                    st.markdown("##### Next Steps")
            
                    for step in event["next_steps"]:
                        st.markdown(
                            f"""
                            <div style="
                                font-size:13px;
                                margin-bottom:6px;">
                                • {step}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
