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
    # CUSTOM STYLES
    # ------------------------

    st.markdown("""
    <style>

    .hero-card{
        background:#45105F;
        border-radius:20px;
        padding:30px;
        color:white;
    }

    .help-card{
        background:#45105F;
        border-radius:20px;
        padding:25px;
        color:white;
    }

    .repair-card{
        background:#FBE8F1;
        border-radius:18px;
        padding:20px;
        min-height:220px;
    }

    .rent-card{
        background:#EEF0FF;
        border-radius:18px;
        padding:20px;
        min-height:220px;
    }

    .details-card{
        background:#FFF8E1;
        border-radius:18px;
        padding:20px;
        min-height:220px;
    }

    .case-card{
        background:#E8FAF8;
        border-radius:18px;
        padding:20px;
        min-height:220px;
    }

    .side-card{
        background:white;
        border-radius:18px;
        padding:20px;
        border:1px solid #E6E2EC;
    }

    .yh-footer{
        position:fixed;
        bottom:0;
        left:0;
        width:100%;
        background:#45105F;
        color:white;
        text-align:center;
        padding:12px;
        z-index:999;
    }

    </style>
    """, unsafe_allow_html=True)

    # ------------------------
    # MAIN LAYOUT
    # ------------------------

    main_col, right_col = st.columns([3,1])

    # ------------------------
    # MAIN COLUMN
    # ------------------------

    with main_col:

        st.markdown("""
        <div class="hero-card">
            <div style="color:#FF5E8A;font-weight:bold;">
                GOOD MORNING
            </div>

            <h1 style="color:white;">
                Welcome back, Prem.
            </h1>

            <p style="font-size:18px;color:#D8CBE3;">
                Here's what's happening with your home at 15 Test Close, Testgate.
            </p>

            <div style="
                background:#6C2149;
                padding:18px;
                border-radius:12px;
                margin-top:20px;">
                ⚠️ Your rent is overdue. Please pay £47.50 as soon as possible.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # ------------------------
        # QUICK ACTION TILES
        # ------------------------

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown("""
            <div class="repair-card">
                <h3>🔧 Log a Repair</h3>
                <p>Tell us about a problem with your home</p>
                <b>Start →</b>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="rent-card">
                <h3>💳 Rent & Payments</h3>
                <p>View balance and payment information</p>
                <b>View →</b>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="details-card">
                <h3>👤 My Details</h3>
                <p>Manage your contact information</p>
                <b>View →</b>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown("""
            <div class="case-card">
                <h3>📋 Submit a Case</h3>
                <p>Complaints, queries and feedback</p>
                <b>Start →</b>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        # ------------------------
        # HELP & SUPPORT
        # ------------------------

        st.markdown("""
        <div class="help-card">
            <h2 style="color:white;">Help & Support</h2>

            <div style="
                background:white;
                color:#777;
                padding:15px;
                border-radius:10px;
                margin-bottom:20px;">
                Search help articles...
            </div>

            <p>• How do I set up a direct debit for rent?</p>
            <p>• What repairs is Yorkshire Housing responsible for?</p>
            <p>• How do I report a neighbour dispute?</p>
            <p>• What should I do if I have a leak?</p>
            <p>• How do I end my tenancy?</p>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------
    # RIGHT COLUMN
    # ------------------------

    with right_col:

        st.markdown("""
        <div class="side-card">
            <h3>Get in Touch</h3>
            <hr>
            <p>💬 Ask a Question</p>
            <p>🚨 Emergency Repair</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="side-card">
            <h3>My Open Cases</h3>

            <p><strong>#24-8312 Repair</strong></p>
            <p>Leaking kitchen tap</p>

            <hr>

            <p><strong>#24-7901 Complaint</strong></p>
            <p>Noise from neighbouring property</p>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------
    # FOOTER
    # ------------------------

    st.markdown("""
    <div class="yh-footer">
        © 2026 Yorkshire Housing. All Rights Reserved.
    </div>
    """, unsafe_allow_html=True)
