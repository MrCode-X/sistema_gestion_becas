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
cur.execute('DROP TABLE IF EXISTS estudiantes_estudiante')
connection.commit()
print('Dropped table estudiantes_estudiante if it existed')
