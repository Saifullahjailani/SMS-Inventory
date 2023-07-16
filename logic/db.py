import psycopg2


class DB:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.conn.autocommit = False
            print("Connected to the PostgreSQL database!")
            return True
        except psycopg2.Error as e:
            print(f"Error connecting to the PostgreSQL database: {e}")
            return False
    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Disconnected from the PostgreSQL database.")

    def _cursor(self):
        return self.conn.cursor()

    def fetchall(self, query, *values):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values)
            return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            return None

    def push(self, query, values):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values)
            return True
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            return False

    def exec(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return True
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            return False

    def fetchOne(self, query, *value):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, value)
            return cursor.fetchone()
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            return None

    def commit(self):
        try:
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error committing the query: {e}")
            return False

    def commit_close(self):
        try:
            self.conn.commit()
        except:
            print("Can not commit the transaction")
            return False
        finally:
            self.conn.close()
            return True

    def get_star(self, table):
        query = f"SELECT * FROM {table};"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            return None
