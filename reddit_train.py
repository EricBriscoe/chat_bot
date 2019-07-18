import praw
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

reddit = praw.Reddit(
    client_id=os.environ["client_id"],
    client_secret=os.environ["client_secret"],
    user_agent="chat_bot",
    username=os.environ["username"],
    password=os.environ["password"],
)


def train(sub):
    print(reddit.read_only)
    subreddit = reddit.subreddit(sub)
    print(subreddit.display_name)
    print(subreddit.title)


if __name__ == "__main__":
    train(sub="the_donald")
