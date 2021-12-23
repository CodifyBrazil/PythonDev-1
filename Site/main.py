from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ola mundo'

app.run(debug=True)