from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/double', methods=['POST'])
def double_number():
    data = request.get_json()
    number = data['number']
    result = number * 2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
  
