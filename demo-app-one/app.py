from flask import Flask, render_template

app = Flask(__name__)


def read_app_config():
  app_config = {}

  with open('./config/demo-app-one', 'r') as f:
    for line in f:
      k, v = line.strip().split('=')
      app_config[k] = v

  return app_config


@app.route('/')
def display_message():

  return render_template('index.html', app_config=read_app_config())


if __name__ == '__main__':
    app.run(debug=True)
