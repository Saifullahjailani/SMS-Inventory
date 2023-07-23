# DB_NAME = 'postgres'
# DB_USER = 'postgres'
# DB_PASSWORD = 'admin'
# DB_HOST = 'localhost'
# DB_PORT = 5432
#
# RECEIPT_PATH = ""

import configparser
import os

CWD = os.getcwd()
CONFIG_PATH = os.path.join(CWD, 'config.ini')
DB_SECTION = 'DB Parameters'
RECEIPT_SECTION = 'Receipt Parameters'


class Configuration:
    def __init__(self, db_name: str, db_user: str, db_pass: str, db_host: str, db_port: str, rec_path: str):
        self._db_name: str = db_name
        self._db_user: str = db_user
        self._db_password: str = db_pass
        self._db_host: str = db_host
        self._db_port: int = int(db_port)
        self._receipt_path: str = rec_path

    @property
    def db_name(self):
        return self._db_name

    @property
    def db_user(self):
        return self._db_user

    @property
    def db_password(self):
        return self._db_password

    @property
    def db_host(self):
        return self._db_host

    @property
    def db_port(self):
        return self._db_port

    @property
    def receipts_dir(self):
        return self._receipt_path

    def write(self):
        config = configparser.ConfigParser()
        config.add_section(DB_SECTION)
        config.set(DB_SECTION, 'name', self._db_name)
        config.set(DB_SECTION, 'user', self._db_user)
        config.set(DB_SECTION, 'host', self._db_host)
        config.set(DB_SECTION, 'password', self._db_password)
        config.set(DB_SECTION, 'port', str(self._db_port))
        config.add_section(RECEIPT_SECTION)
        config.set(RECEIPT_SECTION, 'receipts_dir', self._receipt_path)

        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)


def read() -> Configuration | None:
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    if DB_SECTION in config and RECEIPT_SECTION in config:
        return Configuration(config[DB_SECTION]['name'],
                             config[DB_SECTION]['user'],
                             config[DB_SECTION]['password'],
                             config[DB_SECTION]['host'],
                             config[DB_SECTION]['port'],
                             config[RECEIPT_SECTION]['receipts_dir'])
    return None
