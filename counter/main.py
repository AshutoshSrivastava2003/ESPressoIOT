from flask import Flask, redirect, url_for, request, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html', num=10)

if __name__ == '__main__':
    app.run(debug=True)    
