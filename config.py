from envparse import env

env.read_envfile()

# BOT
TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')
SKIP_UPDATES = env.bool('SKIP_UPDATES')
LOGFILE = env.str('LOGFILE')

OWNER_ID = env.int('OWNER_ID')

# APP
APP_HOST = env.str('APP_HOST', default='localhost')
APP_PORT = env.int('APP_PORT', default=5000)

# REDIS
REDIS_HOST = env.str('REDIS_HOST', default='localhost')
REDIS_PORT = env.int('REDIS_PORT', default=6379)

# WEBHOOK
WEBHOOK_USE = env.bool('WEBHOOK_USE')
WEBHOOK_HOST = env.str('WEBHOOK_HOST')
WEBHOOK_PATH = env.str('WEBHOOK_PATH')
WEBHOOK_PORT = env.int('WEBHOOK_PORT')

# DATABASE
POSTGRES_HOST = env.str('POSTGRES_HOST', default='localhost')
POSTGRES_PORT = env.int('DB_PORT', default=5432)
POSTGRES_USER = env.str('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD', default=None)
POSTGRES_DB = env.str('POSTGRES_DB')

# WEBHOOK INIT
WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'
WEBHOOK_SERVER = {'host': APP_HOST, 'port': APP_PORT}
