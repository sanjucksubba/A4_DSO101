from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>My DevOps App</title></head>
    <body style="font-family:Arial; text-align:center; padding:50px; background:#f0f4f8;">
        <h1>🚀 Hello DevOps!</h1>
        <p>Deployed using GitHub Actions & Render</p>
        <p style="color:gray;">CI/CD Assignment IV – DSO101</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()