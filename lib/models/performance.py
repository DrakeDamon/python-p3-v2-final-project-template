# models/performance.py
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
                speed_score FLOAT,
                strength_score FLOAT,
                notes TEXT,
                FOREIGN KEY (athlete_id) REFERENCES athletes(id)
            )
            '''
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, athlete_id, test_date, speed_score, strength_score, notes=None, id=None):
        self.id = id
        self.athlete_id = athlete_id
        self.test_date = test_date
        self.speed_score = speed_score
        self.strength_score = strength_score
        self.notes = notes

    @property
    def speed_score(self):
        return self.speed_score
    
    @speed_score.setter
    def speed_score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Speed score must be a number")
        if value < 0 or value > 10:
            raise ValueError("Speed score must be between 0 and 10")
        self.speed_score = value

    def save(self):
        sql = '''
            INSERT INTO performances (
                athlete_id, test_date, speed_score, strength_score, notes
            ) VALUES (?, ?, ?, ?, ?)
            '''
        
        CURSOR.execute(sql, (
            self.athlete_id, self.test_date, self.speed_score, 
            self.strength_score, self.notes
        ))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def update(self):
        sql = '''
            UPDATE performances
            SET test_date = ?, speed_score = ?, strength_score = ?, notes = ?
            WHERE id = ?'''
        CURSOR.execute(sql, (
            self.test_date, self.speed_score, self.strength_score, 
            self.notes, self.id
        ))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM performances WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_by_athlete_id(cls, athlete_id):
        sql = "SELECT * FROM performances WHERE athlete_id = ? ORDER BY test_date DESC"
        CURSOR.execute(sql, (athlete_id,))
        rows = CURSOR.fetchall()
        if rows:
            return [cls(
                athlete_id=row[1],
                test_date=row[2],
                speed_score=row[3],
                strength_score=row[4],
                notes=row[5],
                id=row[0]
            ) for row in rows]
        return []
    
    def get_athlete(self):
        from models.athlete import Athlete
        sql = "SELECT * FROM athletes WHERE id = ?"
        CURSOR.execute(sql, (self.athlete_id,))
        row = CURSOR.fetchone()
        if row:
            return Athlete(row[1], row[2], row[0])
        return None