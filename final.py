import tweepy
import os
from keys import *
from getpass import getpass
from InstagramAPI import InstagramAPI

def tweet():
    auth=tweepy.OAuthHandler(API_key,API_secret_key)
    auth.set_access_token(access_token,access_token_secret)
    ap=tweepy.API(auth)
    #ap.update_status("hello")
    folder = 'photos'
    files = os.listdir(folder)
    for file in files:
        if(file.endswith('.jpg')):
            path = folder + '/' + file
            ap.update_with_media(path,'Happy Diwali')

def inst(username,password):
    global InstagramAPI
    InstagramAPI = InstagramAPI(username, password)
    InstagramAPI.login()
    folder = 'photos'
    files = os.listdir(folder)
    for file in files:
        if(file.endswith('.jpg')):
            path = folder + '/' + file
            caption = "photo uploaded using python script"
            InstagramAPI.uploadPhoto(path, caption=caption)





print("1.Upload to twitter")
print("2.Upload to instagram")
ch=input("enter choice")

if ch == '1' :
    print("hello twitter")
    tweet()


elif ch == '2' :
    print("hello insta")
    username = input("enter your username : ")
    password = getpass("enter your password : ")
    inst(username,password)

else:
    print("invalid")



