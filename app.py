# Ryan King
# Honeypot app
# Hosts fake website and collects user data
from flask import Flask, request, render_template
# Flask creates the webpages & handles logins
# Request reads the attacker IP, User-Agent, Form data, etc.
# Render template loads the html files from templates folder
import datetime
import os
# OS Needed to view and add to log file on system

app = Flask(__name__)
# Initializes the webserver

LOG_FILE = "honeypot.log"

def log_event(event_type, details):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        ip = request.remote_addr
        ua = request.headers.get("User-Agent")
        f.write(f"{timestamp} {event_type} IP={ip} UA={ua} DETAILS={details}\n")
# Will log events including time, attacker IP, User-Agent, event type, and extra details

@app.route("/", methods=["GET"])
def home():
    log_event("VISIT", "Visited login page")
    return render_template("login.html")
# This runs the home function when a user visits "/".
# Logs event and returns the login.html file

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    log_event("LOGIN_ATTEMPT", f"user={username}, pass={password}")
    return render_template("dashboard.html")
# This runs the login function when a user posts to "/login".
# It retreives the username and password entered and logs the attempt, it then returns the user to the dashboard.
# This will simulate a "success" to the attacker to further investigate motives and attack strategies

@app.route("/exportkey", methods=["GET"])
def exportkey():
    log_event("KEY_EXPORT_ATTEMPT", "Attacker tried to export fake private key")
    return "PRIVATE KEY: 4f7a8c9b28deadbeef123fakekey=="
# We will allow a function to "export" the key, however, this will log the attacker and send a fake key

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()
# If ia honeypot.log file doesnt exist, it will create one.
app.run(host="0.0.0.0", port=5000)
# host="0.0.0.0" makes the webserver accessible from my LAN
# port=5000 is Flask defaut port
