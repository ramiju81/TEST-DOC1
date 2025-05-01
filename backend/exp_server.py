from flask import Flask

app = Flask(__name__)

@app.route('/')
def experiment():
    return "Response from Experimental Server"

if __name__ == '__main__':    
    app.run(host='0.0.0.0',port=5000)