class Product:
    def __init__(self, id:str, name:str, price:float):
        self.id = id
        self.name = name
        self.price = price

    def push(self, db):
         query = f"INSERT INTO products (id,name, price) VALUES (%s, %s, %s);"
         return db.push(query, (self.id, self.name, str(self.price)))

    def fetch(db, id:str):
        query = "SELECT name, price FROM products WHERE id = %s;"
        p = db.fetchOne(query, id)
        if not p:
            return Product(p[0], p[1], p[2])
        return p
     
    def get_star(db):
        all = db.get_star('products')
        return all

    def edit(self, db):
        query = "UPDATE products SET name = %s, price = %s WHERE id = %s"
        return db.push(query, (self.name,  str(self.price), self.id))



    def __repr__(self) -> str:
        return f"Product <{self.id}, {self.name}, {self.price}>"
    
