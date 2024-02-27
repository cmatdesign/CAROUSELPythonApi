import sqlite3

class DatabaseHandler:
    def __init__(self, db_file):
        self.db_file = db_file

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def load_items(self, item_class, table_name):
        self.connect()
        self.cursor.execute(f'SELECT * FROM `{table_name}`')
        rows = self.cursor.fetchall()
        self.disconnect()

        items = []
        for row in rows:
            item = item_class(*row)
            items.append(item)

        return items
    
    def load_from_query(self, item_class, query):
        self.connect()
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.disconnect()

        result = []
        for row in rows:
            item = item_class(*row)
            result.append(item)

        return result
    
    def load_from_query_first_or_default(self, item_class, query):
        self.connect()
        self.cursor.execute(query)
        row = self.cursor.fetchone() 
        self.disconnect()

        if row is None:
            return None

        # Create an instance of item_class using the fetched row
        item = item_class(*row)
        return item