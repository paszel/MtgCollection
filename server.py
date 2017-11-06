from flask import Flask, render_template, redirect, request
from api import get_cards

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def index():
    result = [] # get_cards()
    
    return render_template('cards.html',cards=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234, debug=True)