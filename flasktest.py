from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route('/')

def hello():
    return render_template("index2.html")

@app.route('/series')
def series():
    return render_template('series.html')

@app.route('/blogs')
def blogs():
    return "Hello this is my blog"

@app.route('/doodleAI', methods=['GET', 'POST'])
def doodle():
    return render_template("predict.html")


@app.route('/predict', methods=['GET','POST'])
def prediction():
    img_data = request.get_data()
    return "7"


if __name__ == '__main__':
    # app.run(host=os.getenv('IP', '0.0.0.0'),
    #         port=int(os.getenv('PORT', 8888)), debug=True)
    app.run(port=650,debug=True)
