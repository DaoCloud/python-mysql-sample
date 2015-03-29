import os
import flask
import MySQLdb

application = flask.Flask(__name__)
application.debug = True

@application.route('/')
def hello_world():
  storage = Storage()
  storage.populate()
  score = storage.score()
  return "Hello world, %d!" % score

class Storage():
  def __init__(self):
    self.db = MySQLdb.connect(      
      user = os.getenv('MYSQL_USERNAME', 'root'),
      passwd = os.getenv('MYSQL_PASSWORD', ''),
      db = os.getenv('MYSQL_INSTANCE_NAME', 'daocloud'),
      host = os.getenv('MYSQL_PORT_3306_TCP_ADDR', 'localhost'),
      port = int(os.getenv('MYSQL_PORT_3306_TCP_PORT', '3306'))
      )

    cur = self.db.cursor()
    cur.execute("DROP TABLE IF EXISTS scores")
    cur.execute("CREATE TABLE scores(score INT)")

  def populate(self):
    cur = self.db.cursor()
    cur.execute("INSERT INTO scores(score) VALUES(1234)")

  def score(self):
    cur = self.db.cursor()
    cur.execute("SELECT * FROM scores")
    row = cur.fetchone()
    return row[0]

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=3000)
