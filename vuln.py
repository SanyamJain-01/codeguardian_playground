import sqlite3, subprocess
def get_user(name):
    return sqlite3.connect("db").execute("SELECT * FROM users WHERE name = '%s'" % name)
def run(cmd):
    return subprocess.call(cmd, shell=True)
