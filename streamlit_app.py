# CAREER READINESS PREDICTION

st.divider()

st.header("🎯 Career Readiness Prediction")

if st.button("Check My Career Readiness"):

    total_score = (python + sql + excel + powerbi) / 4

    if total_score >= 75:
        st.success("Job Ready! 🏆")

    elif total_score >= 50:
        st.info("Almost Ready! Keep Improving! 👍")

    else:
        st.warning("Needs More Training! 📚")

    st.metric("Career Readiness Score", f"{total_score:.1f}%")import streamlit as st

st.set_page_config(
    page_title="Skill Gap Analyzer",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Personal Skill Gap Analyzer")

st.write(
    "Discover your skills and build your career roadmap!"
)

st.divider()

st.header("👨‍🎓 Student Details")

name = st.text_input("Enter Your Name")

career = st.selectbox(
    "Select Your Dream Career",
    ["Data Analyst", "Data Scientist",
     "AI Engineer", "Business Analyst"]
)
st.divider()

st.header("📊 Skill Assessment")

python = st.slider("Python", 0, 100, 30)
sql = st.slider("SQL", 0, 100, 40)
excel = st.slider("Excel", 0, 100, 20)
powerbi = st.slider("Power BI", 0, 100, 10)

if st.button("Analyze My Skills 🚀"):

    st.subheader("Your Skill Analysis")

    skills = {
        "Python": python,
        "SQL": sql,
        "Excel": excel,
        "Power BI": powerbi
    }

    required = {
        "Python": 80,
        "SQL": 90,
        "Excel": 80,
        "Power BI": 80
    }

    average = sum(skills.values()) / 4

    st.metric("Overall Skill Score", f"{average:.1f}%")