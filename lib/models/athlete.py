from models.__init__ import CURSOR, CONN

class Athlete:
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS athletes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            height FLOAT,
            weight FLOAT,
            position TEXT
            )'''  # Removed extra comma
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, name, height, weight, position, id=None):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.position = position

    @property
    def name(self):
        return self._name  # Changed to _name to avoid infinite recursion
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value  # Changed to _name
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def height(self):
        return self._height  # Changed to _height
    
    @height.setter
    def height(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._height = value  # Changed to _height
        else:
            raise ValueError("Height must be a positive number")

    def save(self):
        sql = '''
            INSERT INTO athletes (name, height, weight, position)
            VALUES (?, ?, ?, ?)
            '''
        CURSOR.execute(sql, (self.name, self.height, self.weight, self.position))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def find_by_name(cls, name):
        sql = '''SELECT * FROM athletes WHERE name = ?'''
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None
    
    def delete(self):
        sql = "DELETE FROM athletes WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = 'SELECT * FROM athletes'  # Fixed FFROM typo
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]
    
    def get_performances(self):  # Changed name to match Performance class
        from models.performance import Performance  # Capitalized Performance
        return Performance.get_by_athlete_id(self.id)  # Using the Performance class method
    
    def update(self):
        sql = '''
            UPDATE athletes
            SET name = ?, height = ?, weight = ?, position = ?
            WHERE id = ?'''
        CURSOR.execute(sql, (self.name, self.height, self.weight, self.position, self.id))
        CONN.commit()