import streamlit as st

st.set_page_config(page_title="Candace Bot - Case Manager", page_icon="🧭", layout="centered")

st.title("🧭 Candace: The Accountability Anchor")
st.subheader("Case Manager & Progress Tracker")

st.markdown("**Style of Play:** Versatile, dependable, always on point")

st.markdown("""
Candace tracks the athlete's recruiting efforts, monitors outreach progress,  
and ensures key tasks are completed on time with helpful reminders and performance insights.

> “Candace keeps the recruiting train moving—one timeline, one reminder, one result at a time.”
""")

st.header("Step 1: Recruiting Progress Overview")
current_stage = st.selectbox("Where are you in the recruiting process?", [
    "Created highlight video",
    "Started emailing coaches",
    "Attended showcases or camps",
    "Heard back from coaches",
    "Scheduled campus visits",
    "Received offers or interest"
])

st.header("Step 2: Task Completion Review")
tasks_done = st.multiselect("Which of these have you completed?", [
    "Uploaded latest film",
    "Researched target schools",
    "Emailed 10+ coaches",
    "Followed up after event",
    "Reviewed responses",
    "Updated athletic resume",
    "Scheduled academic evaluation",
    "Requested recommendation letters"
])

st.header("Step 3: Next Check-In Reminder")
reminder_interval = st.radio("How often should Candace check in?", [
    "Weekly", "Bi-weekly", "Monthly"
])

contact_method = st.selectbox("How should she remind you?", ["Email", "Text", "In-App Message"])
contact_info = st.text_input("Contact Info for Check-Ins:")

if st.button("Start Tracking with Candace"):
    st.success("✅ Candace has logged your progress and will follow up.")
    st.markdown(f"""
    **Current Stage:** {current_stage}  
    **Tasks Completed:** {', '.join(tasks_done)}  
    **Reminder Frequency:** {reminder_interval}  
    **Contact:** via {contact_method} → {contact_info}
    """)
    st.info("Candace says: Progress is a habit. Stay focused and follow through.")
    st.balloons()
