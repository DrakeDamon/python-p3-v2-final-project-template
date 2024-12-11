from models.__init__ import CURSOR, CONN
from datetime import datetime

class Performance:
    @classmethod 
    def create_table(cls):
      sql = '''
          CREATE TABLE IF NOT EXISTS performances (
              id INTEGER PRIMARY KEY,
              athlete_id INTEGER,
              test_date DATE,
              forty_yard FLOAT,
              vertical_jump FLOAT,
              agility_time FLOAT,
              flexibility_score FLOAT,
              strength_score FLOAT,
              notes TEXT,
              FOREIGN KEY (athlete_id) REFERENCES athletes(id)
          )
          '''
      CURSOR.execute(sql)
      CONN.commit()

    def __init__(self, athlete_id, test_date, forty_yard, vertical_jump, 
                 agility_time, flexibility_score, strength_score, notes=None, id=None):  # Made notes optional
        self.id = id
        self.athlete_id = athlete_id
        self.test_date = test_date
        self.forty_yard = forty_yard
        self.vertical_jump = vertical_jump
        self.agility_time = agility_time
        self.flexibility_score = flexibility_score
        self.strength_score = strength_score
        self.notes = notes

    @property
    def forty_yard(self):
        return self._forty_yard  # Changed to _forty_yard
    
    @forty_yard.setter
    def forty_yard(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("40-yard dash time must be a number")
        if value < 3.0 or value > 6.0:
            raise ValueError("40-yard dash time seems unrealistic")
        self._forty_yard = value  # Changed to _forty_yard

    def save(self):
        sql = '''
            INSERT INTO performances (
                athlete_id, test_date, forty_yard, vertical_jump,
                agility_time, flexibility_score, strength_score, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
        
        CURSOR.execute(sql, (
            self.athlete_id, self.test_date, self.forty_yard, 
            self.vertical_jump, self.agility_time, self.flexibility_score, 
            self.strength_score, self.notes
        ))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        sql = "DELETE FROM performances WHERE id = ?"  # Removed extra space
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_by_athlete_id(cls, athlete_id):
        sql = "SELECT * FROM performances WHERE athlete_id = ? ORDER BY test_date DESC"
        CURSOR.execute(sql, (athlete_id,))
        return [cls(*row) for row in CURSOR.fetchall()]
    
    def get_athlete(self):
        from models.athlete import Athlete
        sql = "SELECT * FROM athletes WHERE id = ?"  # Changed to athletes table
        CURSOR.execute(sql, (self.athlete_id,))  # Changed to athlete_id
        row = CURSOR.fetchone()
        if row:
            return Athlete(*row)
        return None