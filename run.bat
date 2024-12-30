@echo off

if "%1" == "run" (
	echo [INFO] Running mypy and launching main.py
	mypy --explicit-package-bases .
	python main.py
	goto :EOF
)

if "%1" == "val" (
	echo [INFO] Running mypy
	mypy --explicit-package-bases .
	goto :EOF
)

if "%1" == "requirements" (
	echo [INFO] Installing requests and flask + generating requirements.txt
	pip install requests flask
	pip freeze > requirements.txt
	goto :EOF
)

if "%1" == "install" (
	echo [INFO] Installing from requirements.txt
	pip install -r requirements.txt
	goto :EOF
)

echo [ERROR] Unknown or missing parameter.
echo Usage: run.bat [run | requirements | install]
exit /b 1

REM .\.venv\Scripts\activate
REM source .venv/bin/activate
REM pip install requests flask ...
REM pip freeze > requirements.txt
