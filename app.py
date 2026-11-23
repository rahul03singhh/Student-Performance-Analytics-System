import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- DATABASE CONFIGURATION ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'rahul@#2003',
    'database': 'your_new_database_name'
}

def get_db_connection():
    """Opens a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print("Database connection error:", e)
        return None

# ==========================================
# MODULE 1: OVERALL DASHBOARD SUMMARY
# ==========================================
def get_dashboard_metrics(conn):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT student_id FROM students;")
    students = cursor.fetchall()
    total_students = len(students)

    cursor.execute("SELECT marks_obtained, max_marks FROM assessments;")
    assessments = cursor.fetchall()
    total_percentage = 0.0
    for row in assessments:
        score = (float(row['marks_obtained']) / float(row['max_marks'])) * 100
        total_percentage = total_percentage + score

    avg_marks = round(total_percentage / len(assessments), 2) if len(assessments) > 0 else 0.0

    cursor.execute("SELECT attended_classes, total_classes FROM attendance;")
    attendance_records = cursor.fetchall()
    total_att = 0.0
    for record in attendance_records:
        att_percent = (float(record['attended_classes']) / float(record['total_classes'])) * 100
        total_att = total_att + att_percent

    class_avg_attendance = round(total_att / len(attendance_records), 2) if len(attendance_records) > 0 else 0.0

    cursor.execute("SELECT student_id, marks_obtained, max_marks FROM assessments;")
    marks_rows = cursor.fetchall()
    student_marks = {}
    for row in marks_rows:
        sid = row['student_id']
        score = (float(row['marks_obtained']) / float(row['max_marks'])) * 100
        if sid not in student_marks:
            student_marks[sid] = []
        student_marks[sid].append(score)

    cursor.execute("SELECT student_id, attended_classes, total_classes FROM attendance;")
    att_rows = cursor.fetchall()
    student_attendance = {}
    for row in att_rows:
        sid = row['student_id']
        att_score = (float(row['attended_classes']) / float(row['total_classes'])) * 100
        if sid not in student_attendance:
            student_attendance[sid] = []
        student_attendance[sid].append(att_score)

    at_risk_count = 0
    for s in students:
        sid = s['student_id']
        my_marks = sum(student_marks[sid]) / len(student_marks[sid]) if sid in student_marks and len(student_marks[sid]) > 0 else 0.0
        my_att = sum(student_attendance[sid]) / len(student_attendance[sid]) if sid in student_attendance and len(student_attendance[sid]) > 0 else 0.0

        if my_marks < 40.0 or my_att < 75.0:
            at_risk_count = at_risk_count + 1

    cursor.close()
    return {
        "total_students": total_students,
        "class_avg_marks": avg_marks,
        "class_avg_attendance": class_avg_attendance,
        "at_risk_count": at_risk_count
    }

# ==========================================
# MODULE 2: INDIVIDUAL STUDENT DETAIL VIEW
# ==========================================
def get_student_detail(conn, student_id):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students WHERE student_id = %s;", (student_id,))
    student = cursor.fetchone()
    if not student:
        cursor.close()
        return None

    cursor.execute("SELECT subject, marks_obtained, max_marks FROM assessments WHERE student_id = %s;", (student_id,))
    marks_rows = cursor.fetchall()

    subject_marks = []
    total_score = 0.0
    for row in marks_rows:
        pct = round((float(row['marks_obtained']) / float(row['max_marks'])) * 100, 2)
        total_score = total_score + pct
        subject_marks.append({
            "subject": row['subject'],
            "marks_obtained": float(row['marks_obtained']),
            "max_marks": float(row['max_marks']),
            "percentage": pct
        })

    overall_marks_avg = round(total_score / len(marks_rows), 2) if len(marks_rows) > 0 else 0.0

    cursor.execute("SELECT subject, attended_classes, total_classes FROM attendance WHERE student_id = %s;", (student_id,))
    att_rows = cursor.fetchall()

    subject_attendance = []
    total_att_pct = 0.0
    for row in att_rows:
        pct = round((float(row['attended_classes']) / float(row['total_classes'])) * 100, 2)
        total_att_pct = total_att_pct + pct
        subject_attendance.append({
            "subject": row['subject'],
            "attended_classes": row['attended_classes'],
            "total_classes": row['total_classes'],
            "percentage": pct
        })

    overall_att_avg = round(total_att_pct / len(att_rows), 2) if len(att_rows) > 0 else 0.0

    is_at_risk = False
    reasons = []
    if overall_marks_avg < 40.0:
        is_at_risk = True
        reasons.append("Marks below 40%")
    if overall_att_avg < 75.0:
        is_at_risk = True
        reasons.append("Attendance below 75%")

    cursor.close()
    return {
        "student_info": student,
        "marks": subject_marks,
        "overall_marks_avg": overall_marks_avg,
        "attendance": subject_attendance,
        "overall_att_avg": overall_att_avg,
        "is_at_risk": is_at_risk,
        "risk_reasons": reasons
    }

# ==========================================
# MODULE 3: AT-RISK STUDENTS TABLE / LIST
# ==========================================
def get_at_risk_students(conn):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT student_id, name, department, semester FROM students;")
    students = cursor.fetchall()

    cursor.execute("SELECT student_id, marks_obtained, max_marks FROM assessments;")
    marks_rows = cursor.fetchall()
    student_marks = {}
    for row in marks_rows:
        sid = row['student_id']
        score = (float(row['marks_obtained']) / float(row['max_marks'])) * 100
        if sid not in student_marks:
            student_marks[sid] = []
        student_marks[sid].append(score)

    cursor.execute("SELECT student_id, attended_classes, total_classes FROM attendance;")
    att_rows = cursor.fetchall()
    student_attendance = {}
    for row in att_rows:
        sid = row['student_id']
        att_score = (float(row['attended_classes']) / float(row['total_classes'])) * 100
        if sid not in student_attendance:
            student_attendance[sid] = []
        student_attendance[sid].append(att_score)

    at_risk_list = []
    for s in students:
        sid = s['student_id']
        my_marks = round(sum(student_marks[sid]) / len(student_marks[sid]), 2) if sid in student_marks and len(student_marks[sid]) > 0 else 0.0
        my_att = round(sum(student_attendance[sid]) / len(student_attendance[sid]), 2) if sid in student_attendance and len(student_attendance[sid]) > 0 else 0.0

        reasons = []
        if my_marks < 40.0:
            reasons.append("Low Marks (<40%)")
        if my_att < 75.0:
            reasons.append("Low Attendance (<75%)")

        if len(reasons) > 0:
            at_risk_list.append({
                "student_id": sid,
                "name": s['name'],
                "department": s['department'],
                "semester": s['semester'],
                "avg_marks": my_marks,
                "avg_attendance": my_att,
                "reasons": ", ".join(reasons)
            })

    cursor.close()
    return at_risk_list

# ==========================================
# MODULE 4: FLASK API ENDPOINTS
# ==========================================
@app.route('/api/dashboard', methods=['GET'])
def api_dashboard():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Cannot connect to database"}), 500
    data = get_dashboard_metrics(conn)
    conn.close()
    return jsonify(data)

@app.route('/api/students/<student_id>', methods=['GET'])
def api_student_detail(student_id):
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Cannot connect to database"}), 500
    data = get_student_detail(conn, student_id)
    conn.close()
    if data is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(data)

@app.route('/api/at-risk', methods=['GET'])
def api_at_risk():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Cannot connect to database"}), 500
    data = get_at_risk_students(conn)
    conn.close()
    return jsonify(data)

# ==========================================
# FRONTEND FILE SERVING ROUTES
# ==========================================
@app.route('/')
def serve_login():
    return send_from_directory('.', 'login.html')

@app.route('/index.html')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory('.', filename)

# --- RUN FLASK SERVER ---
if __name__ == '__main__':
    print(">>> Starting Student Performance Analytics Backend...")
    app.run(debug=True, port=5000)