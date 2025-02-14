from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    percentage = data.get("percentage")
    print(f"Received percentage: {percentage}")

    return jsonify({"message": f"Received percentage: {percentage}%", "status": "success"})

# Vercel requires this function
def handler(event, context):
    return app(event, context)