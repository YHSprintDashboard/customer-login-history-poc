import streamlit as st

st.set_page_config(
    page_title="Customer Login History",
    layout="wide"
)
st.markdown("""
<style>

.stApp {
    background-color: #f3f1f5;
}

section[data-testid="stSidebar"] {
    background-color: #46105d;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

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

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# FEATURE SWITCH
# ----------------------------------

SHOW_LOGIN_HISTORY_POC = False

st.markdown("""
<style>

/* Main Hero */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 20px !important;
}

/* Right hand cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: transparent;
}

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

    # Sidebar

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

    # Layout

    main_col, right_col = st.columns([3, 1])
    
    with main_col:
    
        with st.container(border=True):
            
    
            hero_left, hero_right = st.columns([2, 1])
    
            with hero_left:
    
                st.markdown(
                    "<span style='color:#FF5E8A;font-size:20px;font-weight:bold;'>GOOD MORNING</span>",
                    unsafe_allow_html=True
                )
    
                st.markdown("## Welcome back, Prem.")
    
                st.write(
                    "Here's what's happening with your home at 15 Test Close, Testgate."
                )
    
                st.warning(
                    "⚠️ Your rent is overdue. Please pay £47.50 as soon as possible."
                )
    
            with hero_right:
    
                st.caption("CURRENT BALANCE")
    
                st.markdown(
                    "<h1 style='color:#FF7373;'>-£47.50</h1>",
                    unsafe_allow_html=True
                )
    
                st.write("Your rent is overdue")
    
                st.divider()
    
                st.caption("NEXT PAYMENT")
                st.write("1 October 2026")
    
                st.divider()
    
                st.caption("WEEKLY RENT")
                st.write("£118.00")
    
                st.button(
                    "Make a Payment",
                    type="primary",
                    use_container_width=True
                )
    
                st.button(
                    "View Statements",
                    use_container_width=True
                )
                
    
        st.write("")
    
        c1, c2, c3, c4 = st.columns(4)
    
        with c1:
    
            st.markdown("""
            <div style="
            background:#F9E3EB;
            padding:20px;
            border-radius:20px;
            min-height:160px;">
    
            <h3>🔧 Log a Repair</h3>
    
            <p>Tell us about a problem with your home</p>
    
            <b style="color:#D41468;">
            Start →
            </b>
    
            </div>
            """, unsafe_allow_html=True)
    
        with c2:
    
            st.markdown("""
            <div style="
            background:#E7ECFC;
            padding:20px;
            border-radius:20px;
            min-height:160px;">
    
            <h3>💳 Rent & Payments</h3>
    
            <p>
            View your balance, statements and payments
            </p>
    
            <b style="color:#3E4EB8;">
            View →
            </b>
    
            </div>
            """, unsafe_allow_html=True)
    
        with c3:
    
            st.markdown("""
            <div style="
            background:#F7F0D7;
            padding:20px;
            border-radius:20px;
            min-height:160px;">
    
            <h3>👤 My Details</h3>
    
            <p>
            Update your contact and personal information
            </p>
    
            <b style="color:#D59B00;">
            View →
            </b>
    
            </div>
            """, unsafe_allow_html=True)
    
        with c4:
    
            st.markdown("""
            <div style="
            background:#DDF2EE;
            padding:20px;
            border-radius:20px;
            min-height:160px;">
    
            <h3>📋 Submit a Case</h3>
    
            <p>
            Log a complaint, query or feedback
            </p>
    
            <b style="color:#008E7A;">
            Start →
            </b>
    
            </div>
            """, unsafe_allow_html=True)
    
        st.write("")
    
        st.markdown("""
        <div style="
        background:#45105F;
        padding:20px;
        border-radius:20px;
        color:white;
        ">
    
        <h2 style="color:white;">Help & Support</h2>
    
        <div style="
        background:white;
        padding:15px;
        border-radius:10px;
        color:#999;
        margin-top:20px;
        margin-bottom:20px;">
        Search help articles...
        </div>
    
        <p>How do I set up a direct debit for rent?</p>
        <p>What repairs is Yorkshire Housing responsible for?</p>
        <p>How do I report a neighbour dispute?</p>
        <p>What should I do if I have a leak?</p>
        <p>How do I end my tenancy?</p>
    
        </div>
        """, unsafe_allow_html=True)
    
        with right_col:
    
            st.markdown("""
            <div style="
            background:white;
            padding:20px;
            border-radius:20px;
            border:1px solid #E5E5E5;
            ">
            
            <h3>Get in Touch</h3>
            
            <div style="
            background:#45105F;
            color:white;
            padding:15px;
            text-align:center;
            border-radius:12px;
            margin-bottom:15px;
            font-weight:bold;">
            💬 Ask a Question
            </div>
            
            <div style="
            background:white;
            color:#D41468;
            padding:15px;
            text-align:center;
            border-radius:12px;
            border:2px solid #F3A1BA;
            font-weight:bold;">
            🚨 Emergency Repair
            </div>
            
            </div>
            """, unsafe_allow_html=True)
    
            st.write("")
    
            with st.container(border=True):
    
                st.caption("#24-8312 • Repair")
            
                st.markdown("**Leaking kitchen tap**")
            
                st.write("Booked: 12 Sep 2026")
            
                st.success("IN PROGRESS")
    
            with st.container(border=True):
        
                st.caption("#24-7901 • Complaint")
            
                st.markdown("**Noise from neighbouring property**")
            
                st.write("Closed: 28 Aug 2026")
            
                st.success("COMPLETED")
    
        st.markdown("""
        <div class="yh-footer">
            © 2026 Yorkshire Housing. All Rights Reserved.
        </div>
        """, unsafe_allow_html=True)
