from flask import Flask, request, jsonify 
import requests 
app = Flask(__name__)

@app.route('/forward_request', methods=['POST'])
def forward_request():
    try:
        url = request.json.get('url')
        headers = request.json.get('headers', {})
        data = request.json.get('data', {})
        method = request.json.get('method', 'GET')

        response = requests.request(method, url, headers=headers, data=data)
        
        return jsonify({
            'response_text': response.text,
            'status_code': response.status_code,
        })
    except:
        print("Ok...")

if __name__ == '__main__':
    app.run(debug=False)
