from flask import Flask  
app = Flask(__name__)  

@app.route('/')  
def home():  
    return "Hello, World! This is my DevOps Portfolio!"  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)   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