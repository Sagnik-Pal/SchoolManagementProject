import streamlit as st
import json
from pathlib import Path
import plotly.express as px
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Nexus | School Management",
    page_icon=":material/school:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- Data Layer ----------------
DATABASE = "school_data.json"

def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, "r") as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    return {"students": [], "teachers": []}

def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)

def validate_email(email):
    return "@" in email and "." in email

data = load_data()

# ---------------- Modern Dark & Glassmorphism CSS ----------------
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap' rel='stylesheet'>
<style>
    /* Global Background & Font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        background: #09090b;
        color: #e4e4e7;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: rgba(10, 10, 12, 0.8);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    .css-1d391kg { padding-top: 2rem; }

    /* Typography */
    h1, h2, h3, h4 { color: #fafafa !important; letter-spacing: -0.02em; }
    .main-title {
        font-size: 3rem; font-weight: 800; letter-spacing: -0.03em;
        background: linear-gradient(90deg, #818cf8, #c084fc, #f0abfc);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle { color: #a1a1aa; font-size: 1.1rem; margin-bottom: 2rem; }
    .section-header {
        font-size: 1.2rem; font-weight: 600; color: #fafafa;
        margin: 2.5rem 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;
    }
    .section-header::before {
        content: ''; display: block; width: 4px; height: 20px;
        background: linear-gradient(180deg, #818cf8, #c084fc); border-radius: 2px;
    }

    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 24px;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
        height: 100%;
    }
    .glass-card:hover {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Stat Cards */
    .stat-value { font-size: 2.5rem; font-weight: 800; color: #fafafa; line-height: 1.2; }
    .stat-label { font-size: 0.9rem; color: #71717a; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; }
    
    /* Custom Input Styling */
    .stTextInput > div > div, .stNumberInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: white !important;
        transition: all 0.2s ease;
    }
    .stTextInput > div > div:focus-within, .stNumberInput > div > div:focus-within, .stSelectbox > div > div:focus-within {
        border-color: #818cf8 !important;
        box-shadow: 0 0 0 4px rgba(129, 140, 248, 0.1) !important;
    }
    .stTextInput label, .stNumberInput label, .stSelectbox label { color: #a1a1aa !important; font-weight: 500; }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #4f46e5, #9333ea) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4);
    }
    .stButton > button:active { transform: translateY(0); }

    /* Radio Buttons */
    div[role="radiogroup"] label {
        background: transparent;
        border: none;
        border-left: 3px solid transparent;
        border-radius: 0 8px 8px 0;
        margin-bottom: 4px;
        padding: 8px 12px;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] label:hover {
        background: rgba(255, 255, 255, 0.03);
    }
    div[role="radiogroup"] label[data-checked="true"] {
        background: rgba(255, 255, 255, 0.05);
        border-left: 3px solid #818cf8 !important;
        color: white !important;
    }
    div[role="radiogroup"] label p {
        font-weight: 500;
    }

    /* Tables & Dataframes */
    .stDataFrame { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 10px; }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.02); }
    ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.2); }

    /* Animations */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    .stApp > header, .stApp > section { animation: fadeIn 0.5s ease-out forwards; }
</style>
""", unsafe_allow_html=True)

# ---------------- UI Components ----------------
def card(body_html):
    st.markdown(f'<div class="glass-card">{body_html}</div>', unsafe_allow_html=True)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.markdown('<h1 style="font-size: 2.2rem; font-weight: 800; letter-spacing: -0.05em; margin-bottom: 2rem; color: #fafafa;">Nexus <span style="color: #818cf8;">SMS</span></h1>', unsafe_allow_html=True)
    
    menu = st.radio(
        "Navigation",
        [
            ":material/dashboard: Dashboard",
            ":material/group: Students",
            ":material/badge: Teachers",
            ":material/edit_document: Add Grades",
            ":material/person_search: Student Details",
            ":material/manage_accounts: Teacher Details"
        ],
        label_visibility="collapsed"
    )

# ---------------- Dashboard ----------------
if menu == ":material/dashboard: Dashboard":
    st.markdown('<div class="main-title">Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">A quick overview of your institution\'s performance metrics.</div>', unsafe_allow_html=True)

    # Calculate Metrics
    total_students = len(data["students"])
    total_teachers = len(data["teachers"])
    all_grades = [g for s in data["students"] for g in s["grades"].values()]
    avg_score = round(sum(all_grades) / len(all_grades), 2) if all_grades else 0.0

    # Stat Cards Row
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f'<div class="glass-card"><div class="stat-label">Total Students</div><div class="stat-value">{total_students}</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="glass-card"><div class="stat-label">Total Teachers</div><div class="stat-value">{total_teachers}</div></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="glass-card"><div class="stat-label">Avg. Grade</div><div class="stat-value">{avg_score}</div></div>', unsafe_allow_html=True)
    c4.markdown(f'<div class="glass-card"><div class="stat-label">Subjects</div><div class="stat-value">{len(set(t["subject"] for t in data["teachers"]))}</div></div>', unsafe_allow_html=True)

    # Charts Row
    st.markdown('<div class="section-header">Performance Analytics</div>', unsafe_allow_html=True)
    col_chart1, col_chart2 = st.columns([2, 1])

    with col_chart1:
        if data["students"]:
            # Prepare data for chart
            chart_data = []
            for s in data["students"]:
                grades = s["grades"]
                avg = sum(grades.values()) / len(grades) if grades else 0
                chart_data.append({"Student": s["name"], "Average": round(avg, 2)})
            df = pd.DataFrame(chart_data).sort_values(by="Average", ascending=False).head(10)
            
            fig = px.bar(df, x="Student", y="Average", 
                         template="plotly_dark",
                         color="Average",
                         color_continuous_scale=["#6366f1", "#a855f7", "#ec4899"])
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=10, r=10, t=10, b=10),
                height=350,
                xaxis_title="",
                yaxis_title="Grade",
                font=dict(color="#a1a1aa")
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No student data available for charts yet.")

    with col_chart2:
        st.markdown("##### Top 3 Performers")
        performers = []
        for s in data["students"]:
            grades = s["grades"]
            if grades:
                avg = round(sum(grades.values()) / len(grades), 2)
                performers.append((s["name"], avg))
        performers.sort(key=lambda x: x[1], reverse=True)

        if performers:
            medals = ["1.", "2.", "3."]
            for i, (name, avg) in enumerate(performers[:3]):
                st.markdown(f"""
                <div class="glass-card" style="padding: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div style="font-weight: 600; font-size: 1.1rem; color: #a1a1aa;">{medals[i]} <span style="color: #fafafa;">{name}</span></div>
                    <div style="color: #818cf8; font-weight: 700; font-size: 1.2rem;">{avg}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No grades to calculate top performers.")


# ---------------- Students Section ----------------
elif menu == ":material/group: Students":
    st.markdown('<div class="main-title">Students</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Register new students and view existing records.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">Register New Student</div>', unsafe_allow_html=True)
    
    with st.form("student_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name", placeholder="e.g. John Doe")
            email = st.text_input("Email Address", placeholder="e.g. john@school.edu")
        with c2:
            age = st.number_input("Age", min_value=5, max_value=100, step=1)
            roll_no = st.text_input("Roll Number", placeholder="e.g. STD-2023-01")
        
        submit = st.form_submit_button("Register Student", use_container_width=True)

        if submit:
            if not name or not roll_no or not email:
                st.warning("Please fill all required fields.")
            elif not validate_email(email):
                st.error("❌ Invalid email format. Must contain '@' and '.'")
            elif any(s["roll_no"] == roll_no for s in data["students"]):
                st.error(f"⚠️ Student with roll number '{roll_no}' already exists.")
            else:
                data["students"].append({"name": name, "age": int(age), "email": email, "roll_no": roll_no, "grades": {}})
                save_data(data)
                st.success(f"Student '{name}' registered successfully.")

    st.markdown('<div class="section-header">Student Directory</div>', unsafe_allow_html=True)
    if not data["students"]:
        st.info("No students registered yet.")
    else:
        # Custom HTML Table for modern look
        table_html = (
            '<table style="width:100%; border-collapse: collapse; margin-top: 10px;">'
            '<thead>'
            '<tr style="border-bottom: 1px solid rgba(255,255,255,0.1); text-align: left; color: #71717a;">'
            '<th style="padding: 12px;">Roll No</th>'
            '<th style="padding: 12px;">Name</th>'
            '<th style="padding: 12px;">Age</th>'
            '<th style="padding: 12px;">Email</th>'
            '<th style="padding: 12px;">Avg Grade</th>'
            '</tr>'
            '</thead>'
            '<tbody>'
        )
        for s in data["students"]:
            grades = s["grades"]
            avg = round(sum(grades.values()) / len(grades), 2) if grades else 0
            avg_color = "#4ade80" if avg >= 80 else "#facc15" if avg >= 50 else "#f87171" if avg > 0 else "#71717a"
            table_html += (
                '<tr style="border-bottom: 1px solid rgba(255,255,255,0.05); transition: background 0.2s;" '
                'onmouseover="this.style.backgroundColor=\'rgba(255,255,255,0.02)\'" '
                'onmouseout="this.style.backgroundColor=\'transparent\'">'
                f'<td style="padding: 12px; color: #a1a1aa;">{s["roll_no"]}</td>'
                f'<td style="padding: 12px; font-weight: 600; color: #fafafa;">{s["name"]}</td>'
                f'<td style="padding: 12px; color: #a1a1aa;">{s["age"]}</td>'
                f'<td style="padding: 12px; color: #a1a1aa;">{s["email"]}</td>'
                f'<td style="padding: 12px; font-weight: 700; color: {avg_color};">{avg}</td>'
                '</tr>'
            )
        table_html += "</tbody></table>"
        st.markdown(f'<div class="glass-card" style="padding: 0 20px;">{table_html}</div>', unsafe_allow_html=True)


# ---------------- Teachers Section ----------------
elif menu == ":material/badge: Teachers":
    st.markdown('<div class="main-title">Teachers</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Manage faculty members and their assigned subjects.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">Register New Teacher</div>', unsafe_allow_html=True)
    
    with st.form("teacher_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name", placeholder="e.g. Dr. Smith")
            email = st.text_input("Email Address", placeholder="e.g. smith@school.edu")
        with c2:
            subject = st.text_input("Subject", placeholder="e.g. Quantum Physics")
            emp_id = st.text_input("Employee ID", placeholder="e.g. EMP-001")
        
        submit = st.form_submit_button("Register Teacher", use_container_width=True)

        if submit:
            if not name or not emp_id or not email or not subject:
                st.warning("Please fill all required fields.")
            elif not validate_email(email):
                st.error("❌ Invalid email format.")
            elif any(t["emp_id"] == emp_id for t in data["teachers"]):
                st.error(f"⚠️ Teacher with Employee ID '{emp_id}' already exists.")
            else:
                data["teachers"].append({"name": name, "age": 30, "email": email, "subject": subject, "emp_id": emp_id})
                save_data(data)
                st.success(f"Teacher '{name}' registered successfully.")

    # Faculty Cards
    st.markdown('<div class="section-header">Faculty Directory</div>', unsafe_allow_html=True)
    if not data["teachers"]:
        st.info("No teachers registered yet.")
    else:
        cols = st.columns(3)
        for i, t in enumerate(data["teachers"]):
            with cols[i % 3]:
                card_html = f"""
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
                    <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #6366f1, #a855f7); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: white; flex-shrink: 0;">
                        {t['name'][0].upper()}
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1rem; color: #fafafa;">{t['name']}</div>
                        <div style="color: #818cf8; font-size: 0.9rem; font-weight: 500;">{t.get('subject', 'N/A')}</div>
                    </div>
                </div>
                <div style="margin-top: 15px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 10px;">
                    <div style="color: #71717a; font-size: 0.85rem;">📧 {t['email']}</div>
                    <div style="color: #71717a; font-size: 0.85rem; margin-top: 5px;">🆔 {t['emp_id']}</div>
                </div>
                """
                card(card_html)


# ---------------- Add Grades Section ----------------
elif menu == ":material/edit_document: Add Grades":
    st.markdown('<div class="main-title">Add Grades</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Assign marks to students for specific subjects.</div>', unsafe_allow_html=True)

    if not data["students"]:
        st.info("No students registered yet. Please register a student first.")
    else:
        c1, c2, c3 = st.columns([2, 2, 1])
        with c1:
            roll_options = [f"{s['roll_no']} ({s['name']})" for s in data["students"]]
            selected = st.selectbox("Select Student", roll_options)
            roll_no = selected.split(" (")[0]
        with c2:
            subject = st.text_input("Subject Name", placeholder="e.g. Mathematics")
        with c3:
            marks = st.number_input("Marks (0-100)", min_value=0.0, max_value=100.0, step=0.5)

        if st.button("Add Grade", use_container_width=True):
            if not subject:
                st.warning("Please enter a subject.")
            else:
                for s in data["students"]:
                    if s["roll_no"] == roll_no:
                        s["grades"][subject] = float(marks)
                        save_data(data)
                        st.success(f"Added {marks} in {subject} for {s['name']}.")
                        break

        # Current Grades Display
        st.markdown('<div class="section-header">Current Academic Standing</div>', unsafe_allow_html=True)
        for s in data["students"]:
            if s["roll_no"] == roll_no:
                if s["grades"]:
                    df = pd.DataFrame([{"Subject": k, "Marks": v} for k, v in s["grades"].items()])
                    
                    col_a, col_b = st.columns([3, 1])
                    with col_a:
                        st.dataframe(df.set_index("Subject"), use_container_width=True, height=200)
                    with col_b:
                        avg = round(sum(s["grades"].values()) / len(s["grades"]), 2)
                        st.metric("Average Score", avg)
                        st.progress(avg / 100)
                else:
                    st.info("No grades recorded for this student yet.")
                break

# ---------------- Student Details Section ----------------
elif menu == ":material/person_search: Student Details":
    st.markdown('<div class="main-title">Student Details</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">View detailed profile and academic performance.</div>', unsafe_allow_html=True)
    
    if not data["students"]:
        st.info("No students registered yet.")
    else:
        roll_options = [f"{s['roll_no']} ({s['name']})" for s in data["students"]]
        selected = st.selectbox("Select Student", roll_options)
        roll_no = selected.split(" (")[0]
        
        student = next((s for s in data["students"] if s["roll_no"] == roll_no), None)
        
        if student:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown('<div class="section-header">Profile Information</div>', unsafe_allow_html=True)
                profile_html = (
                    f'<div class="glass-card">'
                    f'<div style="display: flex; align-items: center; gap: 20px;">'
                    f'<div style="width: 80px; height: 80px; background: linear-gradient(135deg, #3b82f6, #10b981); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 800; color: white;">'
                    f'{student["name"][0].upper()}'
                    f'</div>'
                    f'<div>'
                    f'<h2 style="margin: 0; padding: 0;">{student["name"]}</h2>'
                    f'<div style="color: #a1a1aa; font-size: 1rem; margin-top: 5px;">Roll No: {student["roll_no"]}</div>'
                    f'</div>'
                    f'</div>'
                    f'<div style="margin-top: 10px;">'
                    f'<div style="color: #71717a; font-size: 0.8rem; text-transform: uppercase;">Email</div>'
                    f'<div style="color: #fafafa; margin-bottom: 10px;">{student["email"]}</div>'
                    f'<div style="color: #71717a; font-size: 0.8rem; text-transform: uppercase;">Age</div>'
                    f'<div style="color: #fafafa;">{student["age"]} years</div>'
                    f'</div>'
                    f'</div>'
                )
                st.markdown(profile_html, unsafe_allow_html=True)
                
            with col2:
                st.markdown('<div class="section-header">Academic Performance</div>', unsafe_allow_html=True)
                grades = student["grades"]
                
                if grades:
                    avg = round(sum(grades.values()) / len(grades), 2)
                    st.markdown(f'<div class="glass-card" style="padding: 15px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;"><div style="font-weight: 600; font-size: 1.1rem; color: #a1a1aa;">Average Grade</div><div style="color: #818cf8; font-weight: 800; font-size: 1.5rem;">{avg}</div></div>', unsafe_allow_html=True)
                    
                    df = pd.DataFrame([{"Subject": k, "Marks": v} for k, v in grades.items()])
                    fig = px.bar(df, x="Subject", y="Marks", 
                                 template="plotly_dark",
                                 color="Marks",
                                 color_continuous_scale=["#ef4444", "#facc15", "#4ade80"])
                    fig.update_layout(
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        margin=dict(l=10, r=10, t=30, b=10),
                        height=300,
                        yaxis_range=[0, 100]
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No grades recorded for this student.")

# ---------------- Teacher Details Section ----------------
elif menu == ":material/manage_accounts: Teacher Details":
    st.markdown('<div class="main-title">Teacher Details</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">View detailed faculty profiles.</div>', unsafe_allow_html=True)
    
    if not data["teachers"]:
        st.info("No teachers registered yet.")
    else:
        emp_options = [f"{t['emp_id']} ({t['name']})" for t in data["teachers"]]
        selected = st.selectbox("Select Teacher", emp_options)
        emp_id = selected.split(" (")[0]
        
        teacher = next((t for t in data["teachers"] if t["emp_id"] == emp_id), None)
        
        if teacher:
            st.markdown('<div class="section-header">Profile Information</div>', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 1])
            with col1:
                profile_html = (
                    f'<div class="glass-card">'
                    f'<div style="display: flex; align-items: center; gap: 20px;">'
                    f'<div style="width: 80px; height: 80px; background: linear-gradient(135deg, #f43f5e, #8b5cf6); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 800; color: white;">'
                    f'{teacher["name"][0].upper()}'
                    f'</div>'
                    f'<div>'
                    f'<h2 style="margin: 0; padding: 0;">{teacher["name"]}</h2>'
                    f'<div style="color: #a1a1aa; font-size: 1rem; margin-top: 5px;">Employee ID: {teacher["emp_id"]}</div>'
                    f'</div>'
                    f'</div>'
                    f'<div style="margin-top: 25px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px; display: flex; flex-direction: column; gap: 15px;">'
                    f'<div>'
                    f'<div style="color: #71717a; font-size: 0.8rem; text-transform: uppercase;">Subject Expertise</div>'
                    f'<div style="color: #fafafa; font-size: 1.1rem; font-weight: 500;">{teacher.get("subject", "N/A")}</div>'
                    f'</div>'
                    f'<div>'
                    f'<div style="color: #71717a; font-size: 0.8rem; text-transform: uppercase;">Contact Email</div>'
                    f'<div style="color: #fafafa;">{teacher["email"]}</div>'
                    f'</div>'
                    f'</div>'
                    f'</div>'
                )
                st.markdown(profile_html, unsafe_allow_html=True)
                
            with col2:
                st.markdown('<div class="section-header">Subject Statistics</div>', unsafe_allow_html=True)
                subject = teacher.get("subject", "")
                
                if subject and data["students"]:
                    subject_grades = []
                    for s in data["students"]:
                        if subject in s["grades"]:
                            subject_grades.append(s["grades"][subject])
                            
                    if subject_grades:
                        avg = round(sum(subject_grades) / len(subject_grades), 2)
                        subject_stats_html = (
                            f'<div class="glass-card">'
                            f'<div style="margin-bottom: 15px;">'
                            f'<div style="color: #71717a; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 5px;">Students Enrolled (Graded)</div>'
                            f'<div style="font-size: 2rem; font-weight: 700; color: #fafafa;">{len(subject_grades)}</div>'
                            f'</div>'
                            f'<div>'
                            f'<div style="color: #71717a; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 5px;">Average Subject Grade</div>'
                            f'<div style="font-size: 2.5rem; font-weight: 800; color: #818cf8;">{avg}</div>'
                            f'</div>'
                            f'</div>'
                        )
                        st.markdown(subject_stats_html, unsafe_allow_html=True)
                    else:
                        st.info(f"No grades recorded yet for {subject}.")
                else:
                    st.info("No students or subject assigned.")