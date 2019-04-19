from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/help.html')
def help():
    return render_template('help.html')

@app.route('/TR_Check.html')
def tr_check():
    return render_template('TR_Check.html')

@app.route('/Sanity_Check.html')
def sanity_check():
    return render_template('Sanity_Check.html')

if __name__ == '__main__':
    app.run()
