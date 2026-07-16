import streamlit as st

# ----------------------------------
# FEATURE SWITCH
# ----------------------------------

SHOW_LOGIN_HISTORY_POC = False

st.markdown("""
<style>

/* Main page */
.stApp {
    background-color: #f3f1f5;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #46105d;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Customer Login History",
    layout="wide"
)

if SHOW_LOGIN_HISTORY_POC:

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
    # LAYOUT
    # ------------------------
    
    outer_left, outer_middle, outer_right = st.columns([1, 8, 3])
    
    with outer_left:
        st.markdown("# ❌")
    
    with outer_middle:
    
        # ONE SINGLE CONTAINER
        with st.container(border=True):
    
            # Header row
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
    
            # Top summary
            st.error(latest["title"])
    
            # ------------------------
            # EXPANDED CONTENT INSIDE CARD
            # ------------------------
    
            if st.session_state.expanded:
    
                st.divider()
    
                st.markdown("#### EVENTS")
    
                for idx, event in enumerate(events):
    
                    icon_col, content_col = st.columns([1, 12])
    
                    with icon_col:
    
                        if event["status"] == "error":
                            st.markdown("## ❌")
                        else:
                            st.markdown("## ✅")
    
                    with content_col:
    
                        banner_left, banner_right = st.columns([6, 1])
    
                        with banner_left:
    
                            if event["status"] == "error":
                                st.error(event["title"])
                            else:
                                st.success(event["title"])
    
                        with banner_right:
                            st.caption(event["date"])
    
                        if "next_steps" in event:
    
                            st.markdown("##### Next Steps")
    
                            for step in event["next_steps"]:
                                st.markdown(
                                    f"<div style='font-size:13px'>• {step}</div>",
                                    unsafe_allow_html=True
                                )
    
                    if idx < len(events) - 1:
                        st.divider()

else:

    st.sidebar.markdown("## 🏠 Yorkshire Housing")
    st.sidebar.markdown("Customer Portal")

    st.sidebar.divider()

    st.sidebar.markdown("🏠 Home")
    st.sidebar.markdown("🔧 Repairs")
    st.sidebar.markdown("💳 Rent & Payments")
    st.sidebar.markdown("📋 My Cases")
    st.sidebar.markdown("🏡 My Home")
    st.sidebar.markdown("💬 Get in Touch")

    with st.container(border=True):

        st.markdown("##### GOOD MORNING")
    
        st.title("Welcome back, Sarah.")
    
        st.write(
            "Here's what's happening with your home at 14 Maple Close, Harrogate."
        )
    
        st.warning(
            "⚠️ Your rent is overdue. Please pay £47.50 as soon as possible."
        )

