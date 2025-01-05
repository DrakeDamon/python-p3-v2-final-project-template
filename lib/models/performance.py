# models/performance.py
from models.__init__ import CURSOR, CONN
from datetime import datetime

class Performance:
    @classmethod 
    def create_table(cls):
        sql_create = '''
            CREATE TABLE IF NOT EXISTS performances (
                id INTEGER PRIMARY KEY,
                athlete_id INTEGER,
                test_date DATETIME,
                speed_score REAL,
                strength_score REAL,
                notes TEXT,
                FOREIGN KEY (athlete_id) REFERENCES athletes(id)
            )
            '''
        CURSOR.execute(sql_create)
        CONN.commit()

    def __init__(self, athlete_id, test_date, speed_score, strength_score, notes=None, id=None):
        self.id = id
        self.athlete_id = athlete_id
        self.test_date = test_date

        if not isinstance(speed_score, (int, float)):
            raise ValueError("Speed score must be a number")
        if speed_score < 0 or speed_score > 10:
            raise ValueError("Speed score must be between 0 and 10")
        self._speed_score = speed_score
        self.strength_score = strength_score
        self.notes = notes

    @property
    def speed_score(self):
        return self._speed_score
    
    @speed_score.setter
    def speed_score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Speed score must be a number")
        if value < 0 or value > 10:
            raise ValueError("Speed score must be between 0 and 10")
        self._speed_score = value


    @classmethod
    def create(cls, athlete_id, test_date, speed_score, strength_score, notes=None):
        """Create and save a new performance record"""
        # Convert string date to datetime if needed
        if isinstance(test_date, str):
            try:
                # Parse date string into datetime object
                test_date = datetime.strptime(test_date, '%Y-%m-%d')
            except ValueError as e:
                raise ValueError(f"Invalid date format: {e}")

        # Create instance with converted datetime
        performance = cls(athlete_id, test_date, speed_score, strength_score, notes)
        performance.save()
        return performance
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
        """Delete this performance from the database"""
        if self.id is None:
            raise ValueError("Cannot delete unsaved performance")
            
        sql = "DELETE FROM performances WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        rows_affected = CURSOR.rowcount  # Check if any rows were actually deleted
        CONN.commit()
        
        if rows_affected == 0:
            raise ValueError(f"No performance found with id {self.id}")
        
        return True

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