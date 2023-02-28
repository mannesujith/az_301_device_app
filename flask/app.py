from time import sleep
from flask import Flask
from flask_restful_swagger_2 import Api
from urls import pages
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

api = Api(app, api_spec_url='/api/swagger',
          schemes=['http'], base_path='',
          title='AZ_301', description='AZ_301 DEVICE APIS')
pages(api)

@app.route('/logs')
def stream():
    def generate():
        with open('logs.log') as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')



if __name__ == '__main__':
    app.run()