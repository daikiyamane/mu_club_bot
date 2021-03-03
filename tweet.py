#coding; utf-8

import os
import tweepy

auth = tweepy.OAuthHandler(
    os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(
    os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)


def make_accounts():
    accounts = ["YNe19999"]
    return accounts


def make_tweets(accounts, count, page):
    l = []
    for i in range(len(accounts)):
        try:
            l.append(api.user_timeline(accounts[i], count=count, page=page))
        except tweepy.TweepError:
            print("userが存在しません")
    return l


def retweet_favorite():
    accounts = make_accounts()
    tweets = make_tweets(accounts, 5, 1)
    for tweet in tweets:
        for t in tweet:
            try:
                api.retweet(t.id)
            except tweepy.TweepError:
                print("すでにリツイートしてます")
            try:
                api.create_favorite(t.id)
            except tweepy.TweepError:
                print("すでにいいねしてます")


retweet_favorite()
