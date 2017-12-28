import praw 
import os
import time 
import sqlite3



def save_nominated(comment_id):
   with sqlite3.connect("database.db") as conn:
      cursor = conn.cursor()
      cursor.execute("INSERT INTO nominees (comment_id) VALUES (?)", (comment_id,))

def has_been_nominated(comment_id):
   with sqlite3.connect("database.db") as conn:
      cursor = conn.cursor()
      return cursor.execute("SELECT COUNT(*) FROM nominees WHERE comment_id = ?", (comment_id,)).fetchone()[0] > 0

def main (): 
   reddit = praw.Reddit(client_id=os.environ["CLIENTID"], 
                  client_secret=os.environ["APPSECRET"], 
                  user_agent=["Comment of the Week Bot"],
                  username=os.environ["USERNAME"],
                  password=os.environ["PASSWORD"])

   while True:
      for comment in reddit.subreddit('TheExpanseSandbox').comments(limit=10):
         if comment.body.strip().startswith('!Nominate'):
            if not has_been_nominated(comment.id):
               comment.reply("Thank you for nominating! Vote for this comment in next week's thread.")
               comment.parent().reply("This comment has been nominated for Comment of the Week! Come back and vote for it in next week's thread.")
               save_nominated(comment.id)
               print("someone has nominated {}".format(comment.parent().body))
      time.sleep(5) 
