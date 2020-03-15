from flask import Flask
app = Flask(__name__)


@app.route('/position/<latitude>/<longitude>')
def latitude_longitude(latitude,longitude):
    return 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003)