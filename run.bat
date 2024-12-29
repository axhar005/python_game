@echo off

if "%1" == "run" (
	echo [INFO] Exécution de mypy et lancement de main.py
	mypy --explicit-package-bases .
	python main.py
	goto :EOF
)

if "%1" == "requirements" (
	echo [INFO] Installation de requests et flask + génération requirements.txt
	pip install requests flask
	pip freeze > requirements.txt
	goto :EOF
)

if "%1" == "install" (
	echo [INFO] Installation à partir de requirements.txt
	pip install -r requirements.txt
	goto :EOF
)

echo [ERREUR] Paramètre inconnu ou manquant.
echo Utilisation : run.bat [run | requirements | install]
exit /b 1

REM .\.venv\Scripts\activate
REM source .venv/bin/activate
REM pip install requests flask ...
REM pip freeze > requirements.txt
