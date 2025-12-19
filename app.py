from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

USER = "admin"
PASS = "admin123"

logs = []

# Strong spam indicators (high weight)
STRONG_SPAM_WORDS = [
    "otp", "password", "lottery", "winner", "prize",
    "bank account suspended", "verify immediately",
    "click here", "free money"
]

# Weak/common indicators (low weight)
WEAK_SPAM_WORDS = [
    "urgent", "verify", "bank", "account", "click"
]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USER and request.form["password"] == PASS:
            session["user"] = USER
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    result = None
    probability = None
    reasons = []

    if request.method == "POST":
        email_text = request.form["email"].lower()

        score = 0

        # Strong spam words → big impact
        for word in STRONG_SPAM_WORDS:
            if word in email_text:
                score += 30
                reasons.append(f"Strong spam indicator detected: '{word}'")

        # Weak spam words → small impact
        for word in WEAK_SPAM_WORDS:
            if word in email_text:
                score += 5
                reasons.append(f"Common spam-related keyword found: '{word}'")

        # Base probability
        if score == 0:
            probability = 8
            result = "NOT SPAM ✅"
            reasons = ["No significant spam indicators detected"]
        else:
            probability = min(95, score + 10)
            result = "SPAM 🚨" if probability >= 50 else "NOT SPAM ✅"

        logs.append({
            "time": datetime.now().strftime("%d %b %Y %H:%M"),
            "result": result,
            "prob": probability
        })

    return render_template(
        "dashboard.html",
        result=result,
        probability=probability,
        reasons=reasons
    )

@app.route("/logs")
def detection_logs():
    if "user" not in session:
        return redirect("/")
    return render_template("logs.html", logs=logs)

@app.route("/model")
def model_info():
    if "user" not in session:
        return redirect("/")
    return render_template("model.html")

@app.route("/settings")
def settings():
    if "user" not in session:
        return redirect("/")
    return render_template("settings.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)