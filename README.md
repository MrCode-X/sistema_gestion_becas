# sistema_gestion_becas

Proyecto Django para gestionar becas. Contiene backend en `backend/` y archivos estáticos en `frontend/`.

Requisitos
- Python 3.10+ (usar el virtualenv provisto opcionalmente)

Instalación rápida (Windows / PowerShell):

```powershell
# activar virtualenv si existe
& env\Scripts\Activate.ps1

# instalar dependencias
pip install -r backend/requirements.txt

# aplicar migraciones
cd backend
python manage.py migrate

# crear superusuario (opcional)
python manage.py createsuperuser

# ejecutar servidor
python manage.py runserver
```

Notas
- El archivo de base de datos `backend/db.sqlite3` está en el `.gitignore` y fue eliminado del repo.
- Para desarrollo local, mantén tu entorno virtual activado.
# Sistema de Gestión de Becas — Instrucciones rápidas

Requisitos:
- Python 3.10+ (virtualenv recomendado)

Pasos para ejecutar en desarrollo (Windows):

1. Activar el virtualenv:

```powershell
.\env\Scripts\Activate.ps1
```

2. Instalar dependencias (si hace falta):

```powershell
pip install -r backend/requirements.txt
```

3. Migrar y crear la base de datos SQLite en desarrollo:

```powershell
cd backend
python manage.py migrate
```

4. Crear superusuario (opcional):

```powershell
python manage.py createsuperuser
```

5. Levantar servidor de desarrollo:

```powershell
python manage.py runserver 8000
```

Notas importantes:
- En `backend/becas_system/settings.py` hay un fallback a SQLite cuando `DEBUG = True`. Para usar MySQL, restaura la configuración de `DATABASES` y ajusta credenciales.
- Las apps reales están en `backend/apps/*` y las rutas del proyecto usan el prefijo `apps.` en `INSTALLED_APPS`.
- Si actualizas dependencias en el virtualenv, regenera `backend/requirements.txt` con `pip freeze > backend/requirements.txt`.

Contacto:
- Si quieres que limpie carpetas duplicadas (`usuarios` raíz vs `backend/apps/usuarios`) o haga un PR con los cambios, dime y lo hago.
