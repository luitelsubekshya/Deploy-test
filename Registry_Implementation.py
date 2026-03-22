import streamlit as st
import pandas as pd
from datetime import date

# Full Site List
all_sites = [
    "B and B Hospital", "B and C Hospital", "Birat Nursing Home", "BMCTH", 
    "BPKIHS", "Chitwan Medical College", "Civil Service Hospital", 
    "Dhulikhel", "Frontline", "Grande Intl. Hospital", "HAMS Hospital", 
    "Kirtipur Hospital", "Neurocardio", "Norvic", "Om Hospital", 
    "Sahid Gangalal", "TUTH", "Nagarik", "Mediciti", "GMC"
]

st.set_page_config(page_title="NICRF Registry Tracker", layout="wide")

st.sidebar.header("Site Selection")
target_site = st.sidebar.selectbox("Choose Hospital", all_sites)

st.title(f"📑 Registry Implementation: {target_site}")

# Tabs for Organization
tab1, tab2, tab3 = st.tabs(["🏗️ Logistics & Admin", "💻 Tech & Onboarding", "💬 Site Feedback"])

with tab1:
    st.subheader("Phase 1: Foundation")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Legal & Personnel**")
        st.checkbox("MOU signed with site", key=f"mu_{target_site}")
        st.checkbox("Identify Site Lead & Incharge", key=f"ld_{target_site}")
        st.checkbox("Collect Data Collector details", key=f"dc_{target_site}")
        
    with c2:
        st.write("**Hardware & Capacity**")
        st.checkbox("Confirm Site has Device (Tablet/Laptop)", key=f"dv_{target_site}")
        st.checkbox("Confirm Bed Numbers & Lab Units", key=f"bl_{target_site}")
        st.checkbox("Internet Connectivity Verified", key=f"net_{target_site}")
        
       

with tab2:
    st.subheader("Phase 2: Digital Integration")
    st.checkbox("Platform Development complete", key=f"pd_{target_site}")
    st.checkbox("Create & Share Logins via Email", key=f"lo_{target_site}")
    st.checkbox("Introduce in WhatsApp Group", key=f"wa_{target_site}")
    
    st.divider()
    st.write("**Reporting & Compliance**")
    # NEW: Implementation Sheet Update
    st.checkbox("✅ Update Internal Implementation Sheet", key=f"sheet_{target_site}")
    st.checkbox("Notify NICRF Central Team", key=f"ni_{target_site}")

 # NEW: Handover Logic
    handover = st.checkbox("Handover device if needed", key=f"ho_{target_site}")
    if handover:
        # Indent the sub-selection for better UI
        device_type = st.radio(
            "Select Device Type:",
            ["Tablet", "Laptop"],
            key=f"dt_{target_site}",
            horizontal=True
        )
    
    # NEW: OTP Verification
    st.checkbox("OTP verified", key=f"otp_{target_site}")

with tab3:
    st.subheader("Phase 3: Feedback Loop")
    
    f_col1, f_col2 = st.columns([2, 1])
    
    with f_col1:
        feedback_type = st.selectbox("Issue Category", ["Technical Bug", "Workflow Suggestion", "Staffing Issue", "Data Quality Note"])
        st.text_area("Detailed Feedback/Observations", placeholder="Enter notes from daily follow-up or census checks...")
    
    with f_col2:
        st.write("**Action Items**")
        st.toggle("Flag for Refresher Training", key=f"ref_{target_site}")
        st.toggle("Critical Bug - Escalate to Dev Team", key=f"esc_{target_site}")

    if st.button("Save Daily Site Update"):
        st.success(f"Log updated for {target_site}!")
        

