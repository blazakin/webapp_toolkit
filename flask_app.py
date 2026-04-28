from flask import Flask, request, render_template, redirect, jsonify, abort
from url_shorten import get_url, save_url
import os

app = Flask(__name__)

# --- Main page ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# --- Dashboard Pages ---
@app.route('/Ham', methods=['GET'])
def ham_dashboard():
    return render_template('dashboards/ham_dashboard.html')


# --- Tool Pages ---
@app.route('/TaskApp', methods=['GET'])
def task_app():
    return render_template('tools/task_app.html')

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



@app.route('/QR', methods=['GET'])
def qr_code():
    return render_template('tools/qr_code_gen.html')


# --- Portfolio Pages ---
@app.route('/Portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

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
