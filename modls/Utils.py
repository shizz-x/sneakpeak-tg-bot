from __future__ import annotations
import re

import validators
from urllib.parse import urlparse
import sqlite3 as sql



class Utility:
  conn: sql.Connection
  cursor: sql.Cursor

  def __init__(self) -> None:
    self.conn = sql.connect('modls/db.db')
    self.cursor = self.conn.cursor()

    self.__create_tables_if_not_exists()
  


  def add_user(self, user_id: int, referrer_id: int | None = None) -> None:
    self.cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
    db_res = self.cursor.fetchall()
    if len(db_res)==0:
      self.cursor.execute('INSERT INTO users (user_id, referrer_id, balance) VALUES (?,?,?)', 
                          (user_id, referrer_id if referrer_id is not None else 0, 0,))
      self.conn.commit()

    
  def get_referrals(self, user_id: int) -> int:


    self.cursor.execute("SELECT * FROM users WHERE referrer_id = ?", (user_id,))
    db_res = self.cursor.fetchall()
    
    return len(db_res)
  
  def get_balance(self, user_id: int) -> int:
    self.cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
    db_res = self.cursor.fetchall()

    for res in db_res:
      return res[0]


  def check_uri_exists(self, uri: str) -> bool:

    domain = self.check_url_domain(uri)
    if domain:

      self.cursor.execute("SELECT * FROM avaliable_sites")
      db_res = self.cursor.fetchall()

      for row in db_res:
        print(row)
        if row[1].__contains__(domain):
          print('-----------------------------------------')
          return True
    return False


    
  def check_url_domain(self, url:str) -> bool | str:
    # Паттерн для проверки правильности ссылки
    url = url.replace('www.', '')
    url_pattern = re.compile(r"(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}(/\S*)?")

    if url_pattern.match(url):
        # Если строка является ссылкой, возвращаем домен ссылки
        domain = re.findall(r"(?<=://)(.*?)(?=/|$)", url)
        return domain[0]
    elif re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$", url):
        # Если строка содержит только домен, возвращаем домен
        return url
    else:
        # Если строка не является ссылкой или доменом, возвращаем False
        return False


  def __create_tables_if_not_exists(self):
    self.cursor.execute(f'''
      CREATE TABLE IF NOT EXISTS avaliable_sites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain TEXT
      )
    ''')

    self.cursor.execute(f'''
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        referrer_id INTEGER,
        balance INTEGER
      )
      ''')
    
    
    self.conn.commit()