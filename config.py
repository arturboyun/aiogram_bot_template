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
DB_HOST = env.str('DB_HOST', default='localhost')
DB_PORT = env.int('DB_PORT', default=3306)
DB_USER = env.str('DB_USER', default='root')
DB_PASSWORD = env.str('DB_PASSWORD', default=None)
DB_DATABASE = env.str('DB_DATABASE')

# WEBHOOK INIT
WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'
WEBHOOK_SERVER = {'host': APP_HOST, 'port': APP_PORT}
