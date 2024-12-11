# lib/models/__init__.py
import sqlite3

CONN = sqlite3.connect('athlete_tracker.db')
CURSOR = CONN.cursor()
