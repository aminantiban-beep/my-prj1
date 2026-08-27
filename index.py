from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": "I aM HaMa DeV WeB"
    })

# للتشغيل المحلي فقط
if __name__ == '__main__':
    app.run()