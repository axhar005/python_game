# -- Variables --
VENV = .venv
PY = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# -- Règles "Phony" (pas de fichier cible) --
.PHONY: help venv run requirements install clean

# -- Tâche par défaut : Affiche l'aide
help:
	@echo "Usage :"
	@echo "  make venv          Crée l'environnement virtuel (.venv)"
	@echo "  make run           Exécute mypy et lance main.py"
	@echo "  make requirements  Installe requests et flask puis génère requirements.txt"
	@echo "  make install       Installe depuis requirements.txt"
	@echo "  make clean         Supprime l'environnement virtuel (.venv)"

# -- Crée l'environnement virtuel si besoin --
venv:
	@echo "[INFO] Création de l'environnement virtuel dans $(VENV)"
	@test -d $(VENV) || python3 -m venv $(VENV)
	@echo "[INFO] Environnement virtuel prêt."

# -- Exécute mypy et main.py --
run: venv
	@echo "[INFO] Exécution de mypy et lancement de main.py"
	@$(PY) -m mypy --explicit-package-bases .
	@$(PY) main.py

# -- Installe requests + flask puis génère requirements.txt --
requirements: venv
	@echo "[INFO] Installation de requests et flask + génération de requirements.txt"
	@$(PIP) install requests flask
	@$(PIP) freeze > requirements.txt
	@echo "[INFO] Fichier requirements.txt généré."

# -- Installe depuis requirements.txt --
install: venv
	@echo "[INFO] Installation à partir de requirements.txt"
	@$(PIP) install -r requirements.txt

# -- Nettoyage : supprime .venv --
clean:
	@echo "[INFO] Suppression de l'environnement virtuel $(VENV)"
	rm -rf $(VENV)
