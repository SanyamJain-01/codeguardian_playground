import sqlite3
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def get_user(name):
    """Retrieve user records matching the given name."""
    conn = sqlite3.connect("db")
    return conn.execute("SELECT * FROM users WHERE name = ?", (name,))

def run(cmd):
    """Execute a command without using a shell."""
    if isinstance(cmd, str):
        args = cmd.split()
    else:
        args = cmd
    return subprocess.call(args, shell=False)

logging.info("test")