class Sales:
    def __init__(self, id, receipt_id, quantity, product_id, customer_id, discount=0, discounted_price=0, db=None):
        self.discounted_price = discounted_price
        self.id = id
        self.receipt_id = receipt_id
        self.quantity = quantity
        self.product_id = product_id
        self.customer_id = customer_id
        self.discount = discount
        self.db = db

    
    def sell(self):
        query = "INSERT INTO sales (receipt_id, quantity, product_id, customer_id, discount, discounted_price) VALUES (%s, %s, %s, %s,%s, %s );"
        return self.db.push(query, (self.receipt_id, self.quantity, self.product_id, self.customer_id, self.discount, self.discounted_price))
    
    def remove(self):
        query = f"DELETE FROM sales WHERE receipt_id = {self.receipt_id} AND product_id = {self.product_id};"
        return self.db.exec(query)
    
    def edit(self, quantity):
        query = f"UPDATE sales SET quantity = {quantity}WHERE receipt_id = {self.receipt_id} AND product_id = {self.product_id};"
        return self.db.exec(quantity)
    
    def fetch(self, receiptID):
        query = "SELECT * FROM sales WHERE receipt_id = %s;"
        return self.db.fetchall(query, receiptID)