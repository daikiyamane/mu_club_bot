#coding; utf-8

import os
import tweepy
import datetime

auth = tweepy.OAuthHandler(
    os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(
    os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)


def make_accounts():
    accounts = [
        "zemichan5", "xPNlCqAD93FFtUL", "wTVgZex2gX4RH8W", "sourinkai", "soccermatsudai", "snkn45th", "shogimatsudai", "prpr_MATSUYAMA", "otokojuku_matsu", "nigitatsusai", "mukeiken", "mubc_1977", "mubaseball_89", "mu_jazz_agents", "mu_LINK2014", "msgurume", "miyoshinishioka", "matudi_spochan", "matudaiguitar", "matudaiBC", "matsuyamawlax",
        "matsuyamaglee", "matsuyama_ussb4", "matsuyama_q", "matsuyama_lax",
        "matsuyama_cheer", "matsuwushu", "matsudaivys", "matsudaiski", "matsudaikyudo",
        "matsudaikarate", "matsudai_tf", "matsudai_syodo", "matsudai_src",
        "matsudai_rugby", "matsudai_rowing", "matsudai_manken", "matsudai_ld",
        "matsudai_horse", "matsudai_futsal", "matsudai_folk", "matsudai_bungei",
        "matsudai_PIER", "matsudai_CoD", "matsudaiBBS", "matsudai65yacht", "matsu_hou",
        "majidaibadoai", "m_sadou_", "karate98764", "ess20962134", "eSportsPCr6s",
        "eSportsAPEX1", "eSports79557391", "eSports45225071", "bMLCuWcO97B2aeF",
        "aidaimatsudai", "a1k1d0_m", "SymphonicWinds", "Popmtsuyama", "Mu_R89",
        "Matudai_achery", "MatsuyamaUKendo", "Matsudaisabage", "MatsudaieBASEBA",
        "Matsudai_CAFE", "MatsudaiOchiken", "Ma_VBT", "MUSC__official", "MTACT1",
        "MMD_dance", "La_soiree_", "Hawaiian_m508", "BA_matsuyamauni", "AIgaookii_gym",
        "8LjpnZSocbp7Xvp"]
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


def tweet():
    dt_now = datetime.datetime.now()
    str_dt_now = dt_now.strftime("%Y年%m月%d日 %H:%M")
    message = str("松山大学の部活・サークルのアカウントをまとめました！\n是非フォローから覗いてみて下さい{}\nこのbotはフォローしている部活やサークルの投稿をリツイートします。\nフォローしていただけると随時追加していきます{}{}\ntweet: {}\n#春から松大 #春から松山大学 #松山大学".format(
        chr(int(0x1f601)), chr(int(0x1f647)), chr(int(0x1f647)), str_dt_now))
    api.update_status(message)


retweet_favorite()
q_favo(["#春から松大", "#春から松山大学", "#松山大学"], 100)
tweet()
