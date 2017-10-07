import praw
import time
import os
import requests


def authenticate():
	print("Authenticating...")
	reddit = praw.Reddit('dadbot', user_agent="Dad Jokes Bot")
	print("Authenticated as {}".format(reddit.user.me()))
	return reddit


def run(reddit, comments_list):
	print("Obtaining 25 comments")

	for comment in reddit.subreddit('test').comments(limit = 25):
		if "!joke" in comment.body and comment.id not in comments_list: #and comment.author != reddit.user.me():
			print('String with \"!joke\" in comment {}'.format(comment.id))
			comment_reply = "You requested a dad joke! Here it is: \n\n"
			
			headers = {
			    'Accept': 'application/json',
			}
!joke
			quote = requests.get('https://icanhazdadjoke.com/', headers=headers).json()['joke']

			comment_reply += ">" + quote
			comment_reply += "\n\nThis quote is from [icanhazdadjoke.com](https://icanhazdadjoke.com)."

			comment.reply(comment_reply)
			print('Replied to comment {}'.format(comment.id))
			comments_list.append(comment.id)

			

	print("Sleeping for 10 seconds")
	time.sleep(10)

 
def saved_comments():
	comments_list = []

	return comments_list


def main():
	reddit = authenticate()
	comments_list = saved_comments()

	while True:
		run(reddit, comments_list)


if __name__ == '__main__':
	main()
