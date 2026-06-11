import os
import sys
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'becas_system.settings')
sys.path.insert(0, os.getcwd())
import django

django.setup()
from django.db import connection

cur = connection.cursor()
cur.execute('SHOW TABLES')
tables = [row[0] for row in cur.fetchall()]
print('TABLES:', tables)

cur.execute("SELECT app,name FROM django_migrations WHERE app IN ('admin','auth','contenttypes','sessions','usuarios','estudiantes','postulaciones','programas') ORDER BY app,name")
migs = cur.fetchall()
print('MIGRATIONS:')
for row in migs:
    print(row)
