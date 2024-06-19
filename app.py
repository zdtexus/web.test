from flask import Flask, render_template
import threading
import webbrowser

app = Flask(__name__)

def open_browser():
    webbrowser.open('http://localhost:5000')

@app.route('/')
def index():

    return render_template('    index.html')

def run_server():
    app.run(debug=False)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    open_browser()
