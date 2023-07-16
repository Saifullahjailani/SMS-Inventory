class Customer:
    def __init__(self, id, name, address, ph):
        self.id = id
        self.name = name
        self.address = address
        self.ph = ph

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
    
    def get_ph_num(self):
        return self.ph

    def push(self, db):
        insert_query = "INSERT INTO customers (name, address, ph_num) VALUES (%s, %s, %s)"
        return db.push(insert_query, (self.name, self.address, self.ph))
    
    def fetch(db, ph_num_to_find, by_num=True):
        query = "SELECT * FROM customers WHERE ph_num = %s;"
        if by_num:
            fetched_list = db.fetchall(query, ph_num_to_find)
        else:
            query = "SELECT * FROM customers WHERE name ILIKE %s LIMIT 40;"
            fetched_list = db.fetchall(query, '%'+ph_num_to_find+'%')
        return fetched_list
    
    def __repr__(self) -> str:
        return f"Customer <{self.get_id()}, {self.get_name()}, {self.get_address()}, {self.get_ph_num()}>"

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.address == other.address and self.ph == other.ph

    def __add__(self, other):
        id, name, address, ph_num = other
        self.id = id
        self.name = name
        self.address = address
        self.ph = ph_num

    def edit(self, db ,other):
        if self == other:
            return True
        else:
            self.id = other.id
            self.name = other.name
            self.address = other.address
            self.ph = other.ph
            return self._edit(db)

    def _edit(self, db):
        return db.push(
            "UPDATE customers SET name = %s, address = %s, ph_num = %s WHERE id = %s",
            (self.name, self.address, self.ph, self.id)
        )
