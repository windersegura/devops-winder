import flask from Flask, jsonify

app = Flask(__name__)

@app.route('/api/payment')
def payment():
    return jsonify({
        'status':'success',
        'message':'Payment processed successfull'})

@app.route('/api/health')
def health():
    return jsonify("Healthy": True)

