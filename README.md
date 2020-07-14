# equipo3chat
Chat del equipo 3

## Comandos utilizados en la carpeta raíz
- `python -m venv .`
- `Scripts\activate.bat`
- `python -m pip install flask requests`
- `python -m pip install pymongo`

## Iniciar las apps con 3 consolas diferentes 
- Frontend
    - `set FLASK_APP=frontend\app.py`
    - `flask run --port=5000`

- Autenticación
    - `set FLASK_APP=authentication\app.py`
    - `flask run --port=5001`

- Mensajes
    - `set FLASK_APP=messages\app.py`
    - `flask run --port=5002`
