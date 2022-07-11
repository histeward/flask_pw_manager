from flask import Flask, render_template,url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)
@app.route('/s', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        return "hello mate"
    else:
        return render_te
        mplate('index.html')



if __name__ == "__main__":
    app.run(debug=True)