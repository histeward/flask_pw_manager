from flask import Flask, render_template, url_for, request, redirect

#instantiating the app and flask knows what to look for
app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET']) #root page
@app.route('/home', methods = ['POST', 'GET' ])
def index():
    if request.method == 'POST':
        return "hello mate"
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
 