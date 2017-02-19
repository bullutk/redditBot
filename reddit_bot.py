import praw
import config
import time

def bot_login():
	print "logging in..."
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "sokonx's bull comment responder v0.1")
	print "Logged in!!"

	return r

def run_bot(r):
	print "obtaining comments..."
	for comment in r.subreddit('test').comments(limit=50):
		if "Ari" in comment.body:
			print ("string found!!")
			comment.reply("Ari is the coolest!!")
			print "comment has been posted!"

	print "sleeping for 10 seconds"
	time.sleep(10)

while True:
	r = bot_login()
	run_bot(r)