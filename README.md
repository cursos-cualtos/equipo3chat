# equipo3chat
Chat del equipo 3

## Librerías de python instaladas
- `python -m pip install flask`
- `python -m pip install requests`
- `python -m pip install pymongo`
- `python -m pip install ibm_watson`
- `python -m pip install cloudant`

## Comandos utilizados en la carpeta raíz
- `python -m venv .`
- `Scripts\activate.bat`

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
