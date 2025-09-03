#class Config:
    #MYSQL_HOST = 'localhost'
    #MYSQL_HOST = 'mysql-container'
    #MYSQL_USER = 'root'
    #MYSQL_PASSWORD = 'root'
    #MYSQL_DB = 'myflaskapp'
    #SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DB}'
    #SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

class Config:
    MYSQL_HOST = 'mysql-container'   # o 'mysql' si usas docker-compose
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'myflaskapp'
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}

