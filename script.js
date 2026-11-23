// Check authentication
if (localStorage.getItem("isLoggedIn") !== "true") {
    window.location.href = "login.html";
}

document.addEventListener("DOMContentLoaded", function() {
    // Logout handler
    const logoutBtn = document.getElementById("logoutBtn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", function() {
            localStorage.removeItem("isLoggedIn");
            window.location.href = "login.html";
        });
    }

    // ===============================
    // PAGE NAVIGATION
    // ===============================
    const buttons = document.querySelectorAll(".nav-btn");
    const pages = document.querySelectorAll(".page");

    function showPage(pageName) {
        pages.forEach(function(page) {
            page.classList.remove("active");
        });

        buttons.forEach(function(button) {
            button.classList.remove("active");
        });

        const selectedPage = document.getElementById(pageName);
        const selectedButton = document.querySelector('[data-page="' + pageName + '"]');

        if (selectedPage) {
            selectedPage.classList.add("active");
        }

        if (selectedButton) {
            selectedButton.classList.add("active");
        }

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }

    buttons.forEach(function(button) {
        button.addEventListener("click", function() {
            const pageName = button.getAttribute("data-page");
            if (pageName) {
                showPage(pageName);
            }
        });
    });

    const startButton = document.getElementById("startMonitoring");
    if (startButton) {
        startButton.addEventListener("click", function() {
            showPage("monitor");
        });
    }

    // ===============================
    // FETCH DATA FROM PYTHON FLASK BACKEND
    // ===============================

    // 1. Fetch Summary Metrics
    function loadDashboardMetrics() {
        fetch("http://127.0.0.1:5000/api/dashboard")
            .then(function(res) {
                return res.json();
            })
            .then(function(data) {
                // Cards
                document.getElementById("cpuValue").textContent = data.class_avg_marks + "%";
                document.getElementById("ramValue").textContent = data.class_avg_attendance + "%";
                document.getElementById("diskValue").textContent = data.total_students;
                document.getElementById("networkValue").textContent = data.at_risk_count;

                // Progress bars
                document.getElementById("cpuBar").style.width = data.class_avg_marks + "%";
                document.getElementById("ramBar").style.width = data.class_avg_attendance + "%";

                // Analytics chart bars
                const chartMarks = document.getElementById("chartMarksBar");
                const chartAtt = document.getElementById("chartAttBar");
                if (chartMarks) chartMarks.style.height = data.class_avg_marks + "%";
                if (chartAtt) chartAtt.style.height = data.class_avg_attendance + "%";

                // Status label
                const status = document.getElementById("systemStatus");
                if (data.at_risk_count > 0) {
                    status.textContent = "Attention Needed";
                    status.style.color = "#ffaa50";
                } else {
                    status.textContent = "Healthy";
                    status.style.color = "#65ff96";
                }
            })
            .catch(function(err) {
                console.log("Could not load metrics", err);
            });
    }

    // 2. Fetch At-Risk Student Table
    function loadAtRiskStudents() {
        fetch("http://127.0.0.1:5000/api/at-risk")
            .then(function(res) {
                return res.json();
            })
            .then(function(list) {
                const container = document.getElementById("atRiskContainer");
                if (!container) return;
                container.innerHTML = "";

                if (list.length === 0) {
                    container.innerHTML = "<div class='monitor-card'><span>All Safe</span><strong>0 Students</strong><p>No students meet at-risk criteria.</p></div>";
                    return;
                }

                list.forEach(function(student) {
                    const card = document.createElement("div");
                    card.className = "monitor-card";
                    card.innerHTML = `
                        <span>ID: ${student.student_id} | ${student.department} (Sem ${student.semester})</span>
                        <strong style="color: #ff6565;">${student.name}</strong>
                        <p>Avg Marks: ${student.avg_marks}% | Avg Attendance: ${student.avg_attendance}%</p>
                        <p style="color: #ffaa50; margin-top: 5px;">Flag: ${student.reasons}</p>
                    `;
                    container.appendChild(card);
                });
            })
            .catch(function(err) {
                console.log("Error loading at risk records", err);
            });
    }

    // 3. Search Individual Student Detail
    const lookupBtn = document.getElementById("lookupBtn");
    if (lookupBtn) {
        lookupBtn.addEventListener("click", function() {
            const idInput = document.getElementById("lookupId").value.trim();
            if (!idInput) {
                alert("Please enter a student ID");
                return;
            }

            fetch("http://127.0.0.1:5000/api/students/" + idInput)
                .then(function(res) {
                    if (!res.ok) throw new Error("Not found");
                    return res.json();
                })
                .then(function(data) {
                    document.getElementById("detName").textContent = data.student_info.name + " (" + data.student_info.student_id + ")";
                    document.getElementById("detDept").textContent = data.student_info.department + " - Sem " + data.student_info.semester;
                    document.getElementById("detMarks").textContent = data.overall_marks_avg + "%";
                    document.getElementById("detAtt").textContent = data.overall_att_avg + "%";

                    const riskElem = document.getElementById("detRisk");
                    if (data.is_at_risk) {
                        riskElem.textContent = "AT RISK";
                        riskElem.style.color = "#ff6565";
                        document.getElementById("detReasons").textContent = data.risk_reasons.join(", ");
                    } else {
                        riskElem.textContent = "SAFE";
                        riskElem.style.color = "#65ff96";
                        document.getElementById("detReasons").textContent = "Meets all criteria";
                    }
                })
                .catch(function() {
                    alert("Student ID not found in portal database.");
                });
        });
    }

    // Refresh button re-loads data
    const refreshButton = document.getElementById("refreshData");
    if (refreshButton) {
        refreshButton.addEventListener("click", function() {
            loadDashboardMetrics();
            loadAtRiskStudents();
        });
    }

    // ===============================
    // INITIAL LOAD
    // ===============================
    showPage("dashboard");
    loadDashboardMetrics();
    loadAtRiskStudents();
});