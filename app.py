from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '0'
    return resp

if __name__ == '__main__':
    app.run(debug=False)
