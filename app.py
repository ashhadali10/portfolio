from flask import Flask  
app = Flask(__name__)  

#homepage
@app.route('/')  
def home():  
    return "Hello, Worlddd! This is my DevOps Portfolio!"  
# about page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)