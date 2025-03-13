from flask import Flask, render_template
from flask import Flask, render_template, flash, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Homepage
@app.route('/')
def home():
    return render_template('index.html')  # Use index.html for the homepage

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)