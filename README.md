# email-spam-detection
🚀 Features
	•	🔐 Secure login authentication
	•	📧 Email spam classification (Spam / Not Spam)
	•	📊 Spam probability scoring
	•	🧠 Explainable detection logic (why an email is spam)
	•	🗂 Detection logs with timestamps
	•	📋 Model information page
	•	⚙ Settings page (extensible)
	•	🌙 Dark-mode dashboard UI
	•	🧪 Academic & viva-ready design

  
 🧠 How It Works
	•	The system analyzes email text for strong and weak spam indicators
	•	Each indicator contributes to a probability score
	•	Emails exceeding a defined threshold are classified as Spam
	•	Clean emails receive a low base probability
	•	The logic is inspired by Naive Bayes, where features (words) influence posterior probability


  🛠 Tech Stack
	•	Backend: Python, Flask
	•	Frontend: HTML, CSS
	•	Logic: Keyword-weighted probability model
	•	Version Control: Git & GitHub


📁 Project Structure
email_spam_detector/
│
├── app.py
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── logs.html
│   ├── model.html
│   └── settings.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md


⸻

🧪 Sample Test Emails

🔴 Spam Example
Urgent! Your bank account is suspended.
Click here to verify immediately and confirm OTP.

🟢 Non-Spam Example
Hello,

This email is to inform you that the project meeting
is scheduled for tomorrow at 10 AM.

Regards,
Team


🔮 Future Enhancements
	•	Integrate real Naive Bayes model using scikit-learn
	•	Database support for logs
	•	File upload for email analysis
	•	Visualization of spam probability
	•	Deployment to cloud platforms
