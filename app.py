from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My DevOps App</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
                min-height: 100vh;
                color: white;
            }
            nav {
                background: rgba(255,255,255,0.1);
                padding: 15px 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                backdrop-filter: blur(10px);
            }
            nav .logo { font-size: 24px; font-weight: bold; color: #e94560; }
            nav ul { list-style: none; display: flex; gap: 30px; }
            nav ul li a { color: white; text-decoration: none; font-size: 16px; }
            nav ul li a:hover { color: #e94560; }
            .hero {
                text-align: center;
                padding: 100px 20px;
            }
            .hero h1 { font-size: 60px; margin-bottom: 20px; }
            .hero h1 span { color: #e94560; }
            .hero p { font-size: 20px; color: #aaa; margin-bottom: 40px; }
            .btn {
                background: #e94560;
                color: white;
                padding: 15px 40px;
                border: none;
                border-radius: 30px;
                font-size: 18px;
                cursor: pointer;
                text-decoration: none;
            }
            .cards {
                display: flex;
                justify-content: center;
                gap: 30px;
                padding: 60px 40px;
                flex-wrap: wrap;
            }
            .card {
                background: rgba(255,255,255,0.1);
                border-radius: 15px;
                padding: 40px 30px;
                width: 250px;
                text-align: center;
            }
            .card .icon { font-size: 50px; margin-bottom: 15px; }
            .card h3 { font-size: 22px; margin-bottom: 10px; }
            .card p { color: #aaa; }
            footer {
                text-align: center;
                padding: 30px;
                background: rgba(0,0,0,0.3);
                color: #aaa;
            }
        </style>
    </head>
    <body>
        <nav>
            <div class="logo">DevOps App</div>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="hero">
            <h1>Welcome to <span>My App</span></h1>
            <p>Deployed with GitHub Actions & Render | DSO101 Assignment IV</p>
            <a href="#" class="btn">Get Started</a>
        </div>
        <div class="cards">
            <div class="card">
                <div class="icon">🚀</div>
                <h3>CI/CD</h3>
                <p>Automated deployment using GitHub Actions</p>
            </div>
            <div class="card">
                <div class="icon">☁️</div>
                <h3>Cloud</h3>
                <p>Hosted on Render cloud platform</p>
            </div>
            <div class="card">
                <div class="icon">🐍</div>
                <h3>Python</h3>
                <p>Built with Flask web framework</p>
            </div>
        </div>
        <footer>
            <p>© 2026 Sanjuck Subba | DSO101 CI/CD Assignment</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)