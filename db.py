import sqlite3
import re
from util import eprint
from os.path import isfile

VERSION = 0
HASH_VERSION = 1

class DatabaseException(Exception):
  pass

class Database:

  def __init__(self, path):
    self.create_mode = not isfile(path)
    # init connections
    self.connection = sqlite3.connect(path)
    self.inlining_connection = sqlite3.connect(path)
    self.inlining_connection.row_factory = lambda cursor, row: row[0]
    # create mode
    if self.create_mode:
      self.init(VERSION, HASH_VERSION)
    # version check
    self.version_check()
    if not self.has_table('benchmarks'):
      raise DatabaseException('Table benchmarks is missing in db {}, initialiization error?'.format(path))
    
  def __enter__(self):
    return self

  def __exit__(self, exception_type, exception_value, traceback):
    self.connection.close()
    self.inlining_connection.close()

  def init(self, version, hash_version):
    self.submit("CREATE TABLE IF NOT EXISTS __version (entry UNIQUE, version, hash_version)")
    self.submit("INSERT OR IGNORE INTO __version (entry, version, hash_version) VALUES (0, {}, {})".format(version, hash_version))
    self.submit("CREATE TABLE IF NOT EXISTS benchmarks (hash TEXT NOT NULL, value TEXT NOT NULL)")

  def has_table(self, name):
    return len(self.value_query("SELECT * FROM sqlite_master WHERE tbl_name = '{}'".format(name))) != 0

  def get_version(self):
    if self.has_table('__version'):
      return self.value_query("SELECT version FROM __version").pop()
    else:
      return 0

  def get_hash_version(self):
    if self.has_table('__version'):
      return self.value_query("SELECT hash_version FROM __version").pop()
    else:
      return 0

  def value_query(self, q):
    cur = self.inlining_connection.cursor()
    lst = cur.execute(q).fetchall()
    return set(lst)

  def query(self, q):
    cur = self.connection.cursor()
    return cur.execute(q).fetchall()

  def submit(self, q):
    eprint(q)
    cur = self.connection.cursor()
    cur.execute(q)
    self.connection.commit()

  def version_check(self):
    if self.get_version() != VERSION:
      raise DatabaseException("Version Mismatch. DB Version is at {} but script version is at {}".format(self.get_version(), VERSION))
    if self.get_hash_version() != HASH_VERSION:
      raise DatabaseException("Hash-Version Mismatch. DB Hash-Version is at {} but script hash-version is at {}".format(self.get_hash_version(), HASH_VERSION))