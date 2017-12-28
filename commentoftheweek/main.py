import praw 
import os
import time 

def main (): 
	reddit = praw.Reddit(client_id=os.environ["CLIENTID"], 
						client_secret=os.environ["APPSECRET"], 
						user_agent=["Comment of the Week Bot"],
						username=os.environ["USERNAME"],
						password=os.environ["PASSWORD"])

	while True:
		for comment in reddit.subreddit('TheExpanseSandbox').comments(limit=10):
			if comment.body.strip().startswith('!Nominate'):
				print("someone has nominated {}".format(comment.parent().body))
		time.sleep(5) 
