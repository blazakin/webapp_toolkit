# from flask import Flask
# import bleach
# import os

# base_path = os.path.dirname(os.path.realpath(__file__))

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello world!'


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/TaskApp', methods=['GET'])
def task_app():
    return render_template('task_app.html')

if __name__ == '__main__':
    app.run(debug=True)
