from envparse import Env

env = Env()

APP_PORT = env.int['APP_PORT']

DB_URL = env.str('DB_URL', default='postgresql+asyncpg://postgres:postgres@localhost:5432/postgres')
