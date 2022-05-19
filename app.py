from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello New world!" 

def fc(x):
    return x.capitalize()

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
