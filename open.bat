@echo off
echo Demarrage de l'application Alfajiri...

echo Demarrage du Backend (Django)...
start cmd /k "cd /d %~dp0Backend && call venv\Scripts\activate && python manage.py runserver"

echo Demarrage du Frontend (Next.js)...
start cmd /k "cd /d %~dp0Frontend && npm run dev"

echo Termine ! Les fenetres de commandes se sont ouvertes.
