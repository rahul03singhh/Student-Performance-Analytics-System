// Simple authentication handler for student evaluation
document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const usernameInput = document.getElementById("username").value.trim();
    const passwordInput = document.getElementById("password").value.trim();
    const errorMsg = document.getElementById("loginError");

    // Standard demo credentials
    if (usernameInput === "admin" && passwordInput === "admin123") {
        localStorage.setItem("isLoggedIn", "true");
        window.location.href = "index.html";
    } else {
        errorMsg.style.display = "block";
    }
});