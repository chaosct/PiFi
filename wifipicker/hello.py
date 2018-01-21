from subprocess import run, PIPE
import shelve
from wifi import Cell
from flask import Flask, escape, request, render_template, jsonify
app = Flask(__name__)

passwords = shelve.open('saved_pw')

@app.route("/")
def hello():
    cells = AP_list()
    return render_template('ap_list.html', cells=cells)

def AP_list():
    run(['sudo','iwlist','wlan0','scan'], stdout=PIPE)
    cells = [vars(c) for c in Cell.all('wlan0')]
    return sorted(cells, key=lambda c: c['quality'], reverse=True)

@app.route('/aps')
def aps():
    return jsonify({'APs':AP_list()})

@app.route('/ap/<apname>')
def connect_ap(apname):
    pw = passwords.get(apname,'')
    return render_template('ap_connect.html',apname=apname,pw=pw)

@app.route('/ap/<apname>/connect', methods=['POST'])
def connect_ap_now(apname):
    passwords[apname]=request.form.get('PW','')
    passwords.sync()
    return "Done"

