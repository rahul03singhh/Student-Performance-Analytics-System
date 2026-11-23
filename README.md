# Student-Performance-Analytics-System
A Student Performance Analytics System is a software application that collects, processes, and visualizes academic data to help educators, students, and institutions track learning outcomes and spot trends early.


# Student Performance & At-Risk Analytics Engine

A full-stack **Python Flask** and **MySQL** web application designed for early academic risk detection and student performance tracking. Developed as a mid-term evaluation project for **CS101 - Programming in Python.

---

## Problem Statement & Motivation

* **Late Risk Identification:** Academic evaluations often occur post-examinations, leaving mentors with little time for timely intervention[cite: 2].
* **Fragmented Academic Data:** Student attendance records and marks are frequently stored in isolated silos or manual registers.
* **Early Warning System:** Automated threshold flags (`< 75%` attendance or `< 40%` marks) help identify vulnerable students early so mentors can step in proactively.

---

## Key Features & Objectives

* **Flask & MySQL Integration:** Connects a Python Flask backend with a relational MySQL database for persistent storage of student, attendance, and marks records.
* **At-Risk Filtering Logic:** Evaluates academic thresholds (`marks < 40` or `attendance < 75`) inside Flask route handlers to flag students requiring attention.
* **Dashboard & Analytics UI:** Displays live database connection status, class averages, enrollment counts, and at-risk student indicators.
* **Authentication Views:** Includes a sign-in interface (`login.html`) to gate access to student academic records.

---

## Architecture & Dataflow

1. **MySQL Database:** Stores student profiles, attendance records, and marks data.
2. **Flask REST API (`app.py`):** Connects via `mysql.connector`, runs SQL queries, applies conditional threshold checks, computes summary metrics, and returns JSON responses (`flask.jsonify`).
3. **Frontend Interface (`index.html`, `login.html`, `script.js`, CSS):** Fetches JSON payloads via the Fetch API, renders dynamic DOM elements, and updates live summary cards and status indicators.

---

## Tech Stack

* **Backend:** Python, Flask, `mysql.connector`, `flask.jsonify`.
* **Database:** MySQL.
* **Frontend:** HTML5, CSS3 (Dark Theme), JavaScript (Fetch API & DOM Manipulation).

---

## Team & Responsibilities

| Member | Roll No. | Responsibilities |
| :--- | :--- | :--- |
| **Rahul** | `26MCA022` | MySQL database schema design, backend Flask application (`app.py`), REST API endpoints, and SQL terminal verification|
| **Bhoomika** | `26MCA004` | Frontend layout (`index.html`), login view (`login.html`), dark-theme styling, and client-side DOM rendering (`script.js`) |

---

## Challenges & Learnings

* **CORS Handling:** Resolved cross-origin communication issues between the Flask backend and frontend Fetch requests.
* **Data Structuring:** Mapped MySQL query outputs into clean JSON structures without serialization errors.
* **Relational Design & Integration:** Practiced normalized relational schema design and full-stack integration between Python APIs and frontend views.

---

## Roadmap & Future Work

* **Phase 1:** Integrate predictive machine learning models (e.g., Scikit-Learn) for risk forecasting.
* **Phase 2:** Add automated email alerts for faculty mentors when students cross risk thresholds.
* **Phase 3:** Add exportable PDF performance summary reports for academic advisor
.
---

## References

* [Flask Documentation](https://flask.palletsprojects.com/).
* [MySQL Documentation](https://dev.mysql.com).
* [MDN Web Docs — Fetch API & Async JavaScript](https://developer.mozilla.org/).
