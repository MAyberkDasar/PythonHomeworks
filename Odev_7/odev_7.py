from flask import Flask, render_template, jsonify, url_for
from odevv_6 import rastgeleNoktaUret

app = Flask(__name__)

@app.route('/')
def index():
    rastgeleNoktaUret()
    return render_template('index.html')

@app.route('/generate_plot', methods=['GET'])
def generate_plot():
    rastgeleNoktaUret()
    return jsonify(new_image_url=url_for('static', filename='images/plot.png'))
    

if __name__ == '__main__':
    app.run(debug=True)
