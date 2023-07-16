from db import DB
from customer import Customer
from product import Product
from sales import Sales
from uuid import uuid4
import config

class Receipt:
    def __init__(self, customer:Customer):
        self.receipt_id = uuid4()
        self.products = []
        self.total = 0
        self.db = DB(config.DB_NAME, config.DB_USER, config.DB_PASSWORD, config.DB_HOST, config.DB_PORT)
        