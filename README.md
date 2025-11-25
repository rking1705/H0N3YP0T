# H0N3YP0T
Vulnerable webpage designed to lure attackers to reveal IP address, system info, and attack techniques.
I created a honeypot webpage on my home lab to show understanding of Python scripting and basic web security principles.

GOAL: Returns user data to a log file, and tracks user actions.

This webpage consisted of an 'index.html', 'dahshboard.html', and 'app.py'.

Index and Dashboard HTML files were generated using AI to simulate a potentially valuable opportunity for attackers.

I decided import Flask because it handled the webpages and login functions. We will also need to import 'datetime' to track log times and 'os' to access my filesystem and write to the log file.
I created a log_event function to write to the file whenever something is tracked such as visit and login.

There are three separate Flask routes used to capture data.

1. Visit - When a user visits a website and sends a "GET" request, it logs the date/time, User-Agent, etc. 
Log Ex. "[2025-11-24 19:27:38] VISIT IP=10.0.2.X UA=Mozilla/5.0 (...) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 DETAILS=Visited login page"
2. Login - When a user submits a "POST" request it logs the attempt and records the username and password entered. This is useful to detect SQL Injections or other attacks using the input form.
Log Ex. "[2025-11-24 19:33:26] LOGIN_ATTEMPT IP=192.168.X.X UA=Mozilla/5.0 (...) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36 DETAILS=user=ADMIN, pass=PA$$W0RD"
3. Export Key - There is a button on the dashboard (user is always directed to dashboard regardless of entry) to export crypto key and this will reveal attackers with intent to steal cryptocurrency and reveal their information.


