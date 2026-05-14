# A4_DSO101
# 🚀 A4_DSO101 – Deploy Your First Web App

A Flask web application deployed using **GitHub Actions** (CI/CD) and **Render** (cloud hosting).

---

## 📋 Assignment Info

| Field | Details |
|---|---|
| **Course** | DSO101 – Continuous Integration and Continuous Deployment |
| **Assignment** | IV – Deploy Your First Web App using GitHub & Render |
| **Student Name** | Sanjuck Subba |
| **Student ID** | 02240357 |
| **Program** | Bachelor of Engineering in Software Engineering (SWE) |

---

## 🌍 Live URL

> **https://a4-dso101.onrender.com**

---

## 🛠 Tools Used

- Python + Flask
- GitHub & GitHub Actions
- Render (cloud deployment)

---

## 📂 Project Structure

```
A4_DSO101/
├── app.py                        # Flask web application
├── requirements.txt              # Python dependencies
├── Procfile                      # Process file for Render
├── README.md                     # Documentation
└── .github/
    └── workflows/
        └── deploy.yml            # GitHub Actions CI/CD workflow
```

---

## 🔧 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanjucksubba/A4_DSO101.git
   cd A4_DSO101
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python3 app.py
   ```

4. Open your browser and go to: `http://localhost:10000`

---

## 🔄 CI/CD with GitHub Actions

Every time code is pushed to the `main` branch, GitHub Actions automatically:

1. Checks out the code
2. Sets up Python
3. Installs dependencies
4. Confirms code was pushed successfully

Workflow file: `.github/workflows/deploy.yml`

---

## 🌐 Deployment Steps on Render

1. Go to [https://render.com](https://render.com) and sign in with GitHub
2. Click **New → Web Service**
3. Connect the `A4_DSO101` GitHub repository
4. Set the following:
   - **Build Command:** `pip3 install -r requirements.txt`
   - **Start Command:** `python3 app.py`
5. Click **Create Web Service**
6. Wait for deployment to complete

---

## ✅ Common Errors & Fixes

| Problem | Solution |
|---|---|
| App not starting | Check start command is `python3 app.py` |
| Build failed | Check `requirements.txt` has `flask` |
| Deployment fails | Reconnect GitHub repo on Render |
| Actions not triggering | Make sure you pushed to `main` branch |
| Slow first load | Free Render instance sleeps — wait 50 seconds |