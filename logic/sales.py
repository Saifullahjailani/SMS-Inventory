from db import DB


class Sales:
    def __init__(self, id, date_sold, receipt_id, quantity, product_id, customer_id, discount=0,db:DB=None):
        self.id = id
        self.date_sold = date_sold
        self.receipt_id = receipt_id
        self.quantity = quantity
        self.product_id = product_id
        self.customer_id = customer_id
        self.discount = discount
        self.db = db

    
    def sell(self):
        query = "INSERT INTO sales (receipt_id, quantity, product_id, customer_id, discount) VALUES (%s, %s, %s, %s,%f );"
        return self.db.push(query, self.receipt_id, self.quantity, self.product_id, self.customer_id, self.discount)
    
    def remove(self):
        query = f"DELETE FROM sales WHERE receipt_id = {self.receipt_id} AND product_id = {self.product_id};"
        return self.db.exec(query)
    
    def edit(self, quantity):
        query = f"UPDATE sales SET quantity = {quantity}WHERE receipt_id = {self.receipt_id} AND product_id = {self.product_id};"
        return self.db.exec(quantity)
    
    def fetch(self, receiptID):
        query = "SELECT * FROM sales WHERE receipt_id = %s;"
        return [Sales(x[0], x[1], x[2], x[3], x[4],x[5],x[6]) for x in self.db.fetchall(query, receiptID)]