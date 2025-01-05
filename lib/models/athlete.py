# models/athlete.py
from models.__init__ import CURSOR, CONN

class Athlete:
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS athletes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT
            )'''
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, name, position, id=None):
        self.id = id
        self._name = name
        self.position = position

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        if len(value.strip()) == 0:        
            raise ValueError("Name must be a non-empty string")
        self._name = value  


    @classmethod
    def create(cls, name, position):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        sql = ''' INSERT INTO athletes (name, position)
        VALUES (?,?)'''
        CURSOR.execute(sql, (name, position))
        CONN.commit()
        return cls(name, position, CURSOR.lastrowid)
    def save(self):
        sql = '''
            INSERT INTO athletes (name, position)
            VALUES (?, ?)
            '''
        CURSOR.execute(sql, (self.name, self.position))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def find_by_name(cls, name):
        sql = '''SELECT * FROM athletes WHERE name = ?'''
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[2], row[0])
        return None
    
    def delete(self):
        sql = "DELETE FROM athletes WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = 'SELECT * FROM athletes'
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(
            name=row[1],
            position=row[2],
            id=row[0]
        ) for row in rows]
    
    def get_performances(self): 
        from models.performance import Performance  
        return Performance.get_by_athlete_id(self.id)  
    
    def update(self):
        sql = '''
            UPDATE athletes
            SET name = ?, position = ?
            WHERE id = ?'''
        CURSOR.execute(sql, (self.name, self.position, self.id))
        CONN.commit()