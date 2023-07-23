import datetime
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
    
    def fetch(receiptID:str, db) -> list:
        query = """
            SELECT 
                p.id,
                p.name, 
                p.price, 
                s.quantity,
                s.discount, 
                s.discounted_price,
                s.discounted_price * s.quantity
            FROM 
                sales AS s
            JOIN
                products p ON p.id=s.product_id
            WHERE 
                receipt_id = %s;
            """
        return db.fetchall(query, receiptID)

    def fetch_with_customer(customer_id, db) -> list:
        query = """
            SELECT 
                s.receipt_id,
                c.name,
                c.ph_num,
                c.address,
                SUM(s.discounted_price),
                TO_CHAR(s.date_sold, 'Mon-DD-YYYY') AS sold_by
            FROM 
                sales AS s
            JOIN 
                customers c on customer_id=c.id
            WHERE
                customer_id = %s
            GROUP BY 
                s.receipt_id, c.name, c.ph_num, c.address, sold_by
            """
        return db.fetchall(query, customer_id)
    def fetch_meta(receiptID:str, db) -> list:
        query = """
            SELECT 
                s.receipt_id,
                c.name,
                c.ph_num,
                c.address,
                SUM(s.discounted_price),
                TO_CHAR(s.date_sold, 'Mon-DD-YYYY') AS sold_by
            FROM 
                sales AS s
            JOIN 
                customers c on customer_id=c.id
            WHERE
                receipt_id = %s
            GROUP BY 
                s.receipt_id, c.name, c.ph_num, c.address, sold_by
            ORDER BY 
                c.name
        """
        return db.fetchall(query, receiptID)

    def fetch_by_date(start_date:datetime, end_date:datetime, db):
        start_date_str = start_date.strftime('%Y-%m-%d %H:%M:%S')
        end_date_str = end_date.strftime('%Y-%m-%d %H:%M:%S')
        query = """
            SELECT 
                s.receipt_id,
                c.name,
                c.ph_num,
                c.address,
                SUM(s.discounted_price),
                TO_CHAR(s.date_sold, 'Mon-DD-YYYY') AS sold_by
            FROM 
                sales AS s
            JOIN 
                customers c on customer_id=c.id
            WHERE
                date_sold BETWEEN %s AND %s
            GROUP BY 
                s.receipt_id, c.name, c.ph_num, c.address, sold_by
            ORDER BY 
                c.name
        """

        return db.fetchall(query, start_date_str, end_date_str)