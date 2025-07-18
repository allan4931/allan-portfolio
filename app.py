
from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html', year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
