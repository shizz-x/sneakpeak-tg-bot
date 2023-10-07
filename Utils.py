from __future__ import annotations


import sqlite3 as sql



class Utility:
  conn: sql.Connection
  cursor: sql.Cursor

  def __init__(self) -> None:
    self.conn = sql.connect('db.db')
    self.cursor = self.conn.cursor()

    self.__create_tables_if_not_exists()
    

  @staticmethod
  def check_uri_exists(self, uri: str) -> bool | None:
    
    pass

  def __create_tables_if_not_exists(self):
    self.cursor.execute(f'''
      CREATE TABLE IF NOT EXISTS avaliable_sites (
        id id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain TEXT
      )
    ''')