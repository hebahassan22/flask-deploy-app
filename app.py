from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello! This is my deployment pipeline test Flask app."

if __name__ == '__main__':
    # Render requires the app to run on host=0.0.0.0 and a dynamic port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
