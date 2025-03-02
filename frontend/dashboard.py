import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.title("SaaS Issue Tracker")
st.sidebar.header("Filter Errors")

severity_filter = st.sidebar.selectbox("Filter by Severity", ["All", "Low", "Medium", "High"])
status_filter = st.sidebar.selectbox("Filter by Status", ["All", "New", "Resolved", "Escalated"])

st.subheader("Error Logs")

response = requests.get(f"{API_URL}/errors")
if response.status_code == 200:
    errors = response.json()
    filtered_errors = [
        error for error in errors
        if (severity_filter == "All" or error["severity"] == severity_filter)
        and (status_filter == "All" or error["status"] == status_filter)
    ]

    for error in filtered_errors:
        with st.expander(f"{error['error_type']} - {error['severity']}"):
            st.write(f"Message: {error['message']}")
            st.write(f"Timestamp: {error['timestamp']}")
            new_status = st.selectbox(f"Update Status", ["New", "Resolved", "Escalated"], key=error["id"])
            if st.button(f"Update {error['id']}"):
                requests.post(f"{API_URL}/update_error", json={"id": error["id"], "status": new_status})
                st.success(f"Updated to {new_status}")
else:
    st.error("Failed to fetch error logs.")
