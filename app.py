import streamlit as st

st.set_page_config(page_title="Login History", layout="wide")

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

st.markdown("### Earlier this month   July 2026")

with st.expander("Your Login History"):

    st.markdown(
        f"""
        <div style="color:red;font-weight:bold;font-size:18px;">
        {latest['title']}
        </div>
        <div>{latest['date']}</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### EVENTS")

    for event in events:

        color = "#d32f2f" if event["status"] == "error" else "#2e7d32"

        st.markdown(
            f"""
            <div style="color:{color};font-weight:bold;">
            {event['title']}
            </div>
            <div>{event['date']}</div>
            """,
            unsafe_allow_html=True,
        )

        if "next_steps" in event:
            st.markdown("#### Next Steps")

            for step in event["next_steps"]:
                st.markdown(f"- {step}")

        st.markdown("---")
