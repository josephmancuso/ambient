from masonite.environment import LoadEnvironment, env
from masoniteorm.connections import ConnectionResolver

"""
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
"""

LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""

DATABASES = {
    'default': env('DB_CONNECTION', 'sqlite'),
    'sqlite': {
        'driver': 'sqlite',
        'database': env('SQLITE_DB_DATABASE', 'masonite.db'),
        'log_queries': env('DB_LOG'),
        'prefix': ''
    },
    'mysql': {
        'driver': 'mysql',
        'host': env('DB_HOST'),
        'database': env('DB_DATABASE'),
        'port': env('DB_PORT'),
        'user': env('DB_USERNAME'),
        'password': env('DB_PASSWORD'),
        'log_queries': env('DB_LOG'),
    },
    'postgres': {
        'driver': 'postgres',
        'host': env('DB_HOST'),
        'database': env('DB_DATABASE'),
        'port': env('DB_PORT'),
        'user': env('DB_USERNAME'),
        'password': env('DB_PASSWORD'),
        'log_queries': env('DB_LOG'),
    },
}


DB = ConnectionResolver().set_connection_details(DATABASES)