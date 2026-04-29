from flask import Flask, request, render_template, redirect, jsonify, abort
from url_shorten import get_url, save_url
from qr_code import make_qr
import os

app = Flask(__name__)

# --- Main page ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# --- Dashboard Pages ---
@app.route('/ham', methods=['GET'])
@app.route('/Ham', methods=['GET'])
def ham_dashboard():
    return render_template('dashboards/ham_dashboard.html')


# --- Tool Pages ---
@app.route('/taskapp', methods=['GET'])
@app.route('/TaskApp', methods=['GET'])
def task_app():
    return render_template('tools/task_app.html')

@app.route('/s/<string:key>', methods=['GET', 'POST'])
@app.route('/S/<string:key>', methods=['GET', 'POST'])
def url_expand(key=None):
    if request.method != 'POST':
        if key is None:
            return render_template('tools/url_shortener.html')
        else:
            try:
                new_url = get_url(key)
                return redirect(new_url)
            except KeyError:
                abort(404)
    else:
        recv_key = request.get_json()['key']
        recv_url = request.get_json()['url']
        try:
            save_url(recv_key, recv_url)
            return jsonify({"status": "success", "received": recv_key}), 200
        except KeyError:
            return jsonify({"status": "key_taken", "received": recv_key}), 200
        except ValueError:
            return jsonify({"status": "too_many_keys", "received": recv_key}), 200

@app.route('/s', methods=['GET', 'POST'])        
@app.route('/S', methods=['GET', 'POST'])
def url_shortener():
    if request.method == 'GET':
        return render_template('tools/url_shortener.html')
    else:
        recv_key = request.get_json()['key']
        recv_url = request.get_json()['url']
        try:
            save_url(recv_key, recv_url)
            return jsonify({"status": "success", "received": recv_key}), 200
        except KeyError:
            return jsonify({"status": "key_taken", "received": recv_key}), 200
        except ValueError:
            return jsonify({"status": "too_many_keys", "received": recv_key}), 200


@app.route('/qr', methods=['GET', 'POST'])
@app.route('/QR', methods=['GET', 'POST'])
def qr_code():
    if request.method == 'GET':
        return render_template('tools/qr_code_gen.html')
    else:
        recv_data = request.get_json()['qr_data']
        qr_data = make_qr(recv_data)
        return jsonify({"status": "success", "qr_data": qr_data}), 200


# --- Portfolio Pages ---
@app.route('/portfolio', methods=['GET'])
@app.route('/Portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

@app.route('/sps24', methods=['GET'])
@app.route('/SPS24', methods=['GET'])
def sps24():
    return render_template('sps24.html')

# --- Error Pages ---
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    if 'PYTHONANYWHERE_DOMAIN' not in os.environ:
        app.run(debug=True)
