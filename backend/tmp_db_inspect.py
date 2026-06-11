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
for table in ['estudiantes', 'estudiantes_estudiante', 'postulaciones', 'postulaciones_postulacion', 'programas_beca', 'usuarios_user']:
    cur.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = DATABASE() AND table_name = %s", (table,))
    exists = cur.fetchone()[0]
    print(f"TABLE {table}: exists={exists}")
    if exists:
        cur.execute("SELECT COUNT(*) FROM `%s`" % table)
        print("  rows=", cur.fetchone()[0])
        cur.execute("SHOW COLUMNS FROM `%s`" % table)
        print("  columns=", [row[0] for row in cur.fetchall()])
        print()

cur.execute("SELECT app,name FROM django_migrations WHERE app IN ('admin','auth','contenttypes','sessions','usuarios','estudiantes','postulaciones','programas') ORDER BY app,name")
print('MIGRATIONS:')
for row in cur.fetchall():
    print(row)
