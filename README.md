* create virtual environment, activate and install requirements

```bash
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

* run

```bash
cp .env.example .env
export FLASK_APP=main.py FLASK_DEBUG=1 TEMPLATES_AUTO_RELOAD=1; flask run -h 0.0.0.0 -p 5000


python -m flask --app main run
```

## Links

* [SQLite Viewer for VSCode](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)
* [SQLAlchemy basic Relationships](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
* [SQLAlchemy ORM tutorial](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
