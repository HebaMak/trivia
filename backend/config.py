import os
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# Database URI
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_NAME_TEST = os.getenv('DB_NAME_TEST')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}@{DB_HOST}/{DB_NAME}'

SQLALCHEMY_DATABASE_URI_TEST = f'postgresql://{DB_USER}@{DB_HOST}/{DB_NAME_TEST}'


SQLALCHEMY_TRACK_MODIFICATIONS = False