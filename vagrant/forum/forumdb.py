# "Database code" for the DB Forum.

import datetime
import psycopg2

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  return c.fetchall()
  db.close()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, datetime.datetime.now()))


