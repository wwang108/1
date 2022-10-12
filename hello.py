from flask import Flask
import netifaces as ni
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']

app = Flask(__name__)

@app.route("/track")
def trackme():
    return ""

app.run(host=ip)
