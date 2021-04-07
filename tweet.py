#coding; utf-8

import os
import tweepy
import datetime

auth = tweepy.OAuthHandler(
    os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(
    os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

# フォローしているアカウントをリストで返す


def make_accounts():
    text_file = open("ac.txt", "r")

    accounts = text_file.read().split()
    text_file.close()
    print(accounts)
    return accounts

# フォローしているアカウントのツイートを集める


def make_tweets(accounts, count, page):
    l = []
    for i in range(len(accounts)):
        try:
            l.append(api.user_timeline(accounts[i], count=count, page=page))
        except tweepy.TweepError:
            print("userが存在しません")
    return l

# フォローしているアカウントのツイートを随時リツイート&いいねする


def retweet_favorite():
    accounts = make_accounts()
    tweets = make_tweets(accounts, 1, 1)
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

# 任意のハッシュタグを含むツイートをいいね


def q_favo(q_list, count):
    for q in q_list:
        print("「{}」を含むツイートを{}件いいねしています。".format(q, count))
        search_results = api.search(q=q, count=count)
        for status in search_results:
            tweet_id = status.id
            try:
                api.create_favorite(tweet_id)
            except tweepy.TweepError:
                print("すでにいいねしてます")

# 任意のメッセージをツイートする


def tweet():
    dt_now = datetime.datetime.now()
    str_dt_now = dt_now.strftime("%Y年%m月%d日 %H:%M")
    message = str("松山大学の部活・サークルのアカウントをまとめました！\n是非フォローから覗いてみて下さい{}\nこのbotはフォローしている部活やサークルの投稿をリツイートします。\nフォローしていただけると随時追加していきます{}{}\ntweet: {}\n#春から松大 #春から松山大学 #松山大学".format(
        chr(int(0x1f601)), chr(int(0x1f647)), chr(int(0x1f647)), str_dt_now))
    api.update_status(message)

    message2 = str(
        "・毎日決まった投稿をしたい方\n・「＃春から松山大学」などのハッシュタグを含んだツイートをリツイートいいねしたい方\nそれ自動化しませんか？\n興味がある方はDMください！！\ntweet: {}\n#春から松大 #春から松山大学 #松山大学".format(str_dt_now))
    api.update_status(message2)

    message3 = str("松山大学生の方で情報分野に少しでも興味ある方！\nゲーム開発，アプリ開発，映像制作など自分で何か作りたい方！\nぜひDM下さい！みんなで集まって楽しく活動しましょう{}{}\ntweet: {}\n#春から松大 #春から松山大学 #松山大学".format(
        chr(int(0x1f601)), chr(int(0x1f601)), str_dt_now))
    api.update_status(message3)


retweet_favorite()
q_favo(["#春から松大", "#春から松山大学", "#松山大学"], 100)
if datetime.time(8, 00) <= datetime.datetime.now().time() and datetime.datetime.now().time() <= datetime.time(9, 0):
    tweet()
elif datetime.time(11, 00) <= datetime.datetime.now().time() and datetime.datetime.now().time() <= datetime.time(12, 0):
    tweet()
elif datetime.time(16, 00) <= datetime.datetime.now().time() and datetime.datetime.now().time() <= datetime.time(17, 0):
    tweet()
elif datetime.time(19, 00) <= datetime.datetime.now().time() and datetime.datetime.now().time() <= datetime.time(20, 0):
    tweet()
elif datetime.time(22, 00) <= datetime.datetime.now().time() and datetime.datetime.now().time() <= datetime.time(23, 0):
    tweet()
