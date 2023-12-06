import os

DB_NAME = "coursify_database.db"
PARAMS = {
    'SECRET_KEY': os.environ['CO_SECRET_KEY'],
    'DB_URI': f'sqlite:///{DB_NAME}',
    'TOKEN': os.environ['CO_TOKEN']
}