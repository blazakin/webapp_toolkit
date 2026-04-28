from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/TaskApp', methods=['GET'])
def task_app():
    return render_template('task_app.html')

@app.route('/Portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

@app.route('/SPS24', methods=['GET'])
def sps24():
    return render_template('sps24.html')

@app.route('/Dashboards/Ham_Dashboard', methods=['GET'])
def ham_dashboard():
    return render_template('/dashboards/ham_dashboard.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)
