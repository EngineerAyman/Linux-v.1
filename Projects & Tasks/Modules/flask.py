'''
Flask Module:
The Flask module is used for creating web applications in Python.
 Here's an example code for creating a simple web server using Flask:

'''




from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()