from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/append', methods=['POST'])
def append_string():
    data = request.get_json()
    received_string = data['string']
    appended_string = "[This is received in Kafka]" + received_string
    return jsonify({'output': appended_string})

if __name__ == '__main__':
    app.run()
