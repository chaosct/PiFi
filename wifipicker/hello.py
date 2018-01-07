from subprocess import run
import shelve
from wifi import Cell
from flask import Flask, escape, request
app = Flask(__name__)

passwords = shelve.open('saved_pw')

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/aps')
def AP_list():
    run(['sudo','iwlist','wlan0','scan'])
    html = []
    html.append('<html><head><title>WiFi Setup</title></head><body>')
    html.append('<ul>')
    for ap in Cell.all('wlan0'):
        html.append('<li><a href="/ap/{0}">{0}</a></li>'.format(escape(ap.ssid)))
    html.append('</ul>')
    html.append('</body></html>')
    return "\n".join(html)

@app.route('/ap/<apname>')
def connect_ap(apname):
    html = []
    html.append('<html><head><title>Connect AP</title></head><body>')
    html.append('<h1>Connecting to {}</h1>'.format(escape(apname)))
    pw = passwords.get(apname,'')
    html.append('<form action="/ap/{apname}/connect" method="post"><input type="password" name="PW" value="{pw}"><br><input type="submit" value="Connect"></form>'.format(pw=escape(pw),apname=escape(apname)))
    html.append('</body></html>')
    return "\n".join(html)

@app.route('/ap/<apname>/connect', methods=['POST'])
def connect_ap_now(apname):
    passwords[apname]=request.form.get('PW','')
    passwords.sync()
    return "Done"
