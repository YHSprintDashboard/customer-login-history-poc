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

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px !important;
}

</style>
""", unsafe_allow_html=True)

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

    # ------------------------
    # SIDEBAR
    # ------------------------

    st.sidebar.markdown("## 🏠 Yorkshire Housing")
    st.sidebar.markdown("Customer Portal")

    st.sidebar.divider()

    st.sidebar.markdown("🏠 Home")
    st.sidebar.markdown("🔧 Repairs")
    st.sidebar.markdown("💳 Rent & Payments")
    st.sidebar.markdown("📋 My Cases")
    st.sidebar.markdown("🏡 My Home")
    st.sidebar.markdown("💬 Get in Touch")

    st.sidebar.divider()

    st.sidebar.markdown("### 👤 Prem Nair")
    st.sidebar.caption("Tenant since 2026")

    st.sidebar.markdown("👤 My Details")
    st.sidebar.markdown("⚙️ Account Settings")
    st.sidebar.markdown("🔑 Reset Password")
    st.sidebar.markdown("🚪 Log Out")

    # ------------------------
    # MAIN LAYOUT
    # ------------------------

    main_col, right_col = st.columns([3, 1])

    # ------------------------
    # MAIN CONTENT
    # ------------------------

    with main_col:

        st.markdown(
            """
            <div style="
                background:#45105F;
                padding:30px;
                border-radius:20px;
                color:white;">
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown(
            "<span style='color:#FF5E8A;font-weight:bold;'>GOOD MORNING</span>",
            unsafe_allow_html=True
        )
        
        st.title("Welcome back, Prem.")
        
        st.write(
            "Here's what's happening with your home at 15 Test Close, Testgate."
        )
        
        st.warning(
            "⚠️ Your rent is overdue. Please pay £47.50 as soon as possible."
        )
        
        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        # Quick Actions

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown("""
            <div class="quick-repair">
                <h3>🔧 Log a Repair</h3>
                <p>Tell us about a problem with your home</p>
                <b>Start →</b>
            </div>
            """,
            unsafe_allow_html=True)

        with c2:
            with st.container(border=True):
                st.markdown("### 💳")
                st.subheader("Rent & Payments")
                st.write("View balance and payment information")
                st.link_button("View →", "#")

        with c3:
            with st.container(border=True):
                st.markdown("### 👤")
                st.subheader("My Details")
                st.write("Manage your contact information")
                st.link_button("View →", "#")

        with c4:
            with st.container(border=True):
                st.markdown("### 📋")
                st.subheader("Submit a Case")
                st.write("Complaints, queries and feedback")
                st.link_button("Start →", "#")

        st.write("")

        # Help & Support

        st.markdown("""
        <div style="
        background:#45105F;
        padding:25px;
        border-radius:20px;
        color:white;">
        <h2>Help & Support</h2>
        </div>
        """,
        unsafe_allow_html=True)

            st.subheader("Help & Support")

            st.text_input(
                "",
                placeholder="Search help articles..."
            )

            st.markdown("##### POPULAR SEARCHES")

            st.write("• How do I set up a direct debit for rent?")
            st.write("• What repairs is Yorkshire Housing responsible for?")
            st.write("• How do I report a neighbour dispute?")
            st.write("• What should I do if I have a leak?")
            st.write("• How do I end my tenancy?")

    # ------------------------
    # RIGHT COLUMN
    # ------------------------

    with right_col:

        with st.container(border=True):

            st.subheader("Get in Touch")

            st.button(
                "💬 Ask a Question",
                use_container_width=True
            )

            st.button(
                "🚨 Emergency Repair",
                use_container_width=True
            )

        st.write("")

        with st.container(border=True):

            st.subheader("My Open Cases")

            st.info("Repair Case #24-8312 - Leaking kitchen tap")

            st.info(
                "Complaint Case #24-7901 - Noise from neighbouring property"
            )

            st.button(
                "View All Cases",
                use_container_width=True
            )

    # ------------------------
    # FOOTER
    # ------------------------

    st.markdown("""
    <style>
    .yh-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #46105d;
        color: white;
        text-align: center;
        padding: 12px;
        font-size: 12px;
        z-index: 999;
    }
    
    .stApp {
        padding-bottom: 60px;
    }
    </style>
    
    <div class="yh-footer">
        © 2026 Yorkshire Housing. All Rights Reserved.
    </div>
    """, unsafe_allow_html=True)
