# -*- coding: utf-8 -*-

import tweepy
from cmd import Cmd
import sys

import banner
import conf

in_encode = sys.stdin.encoding
out_encode = sys.stdout.encoding

try:
    if conf.access_token and conf.access_secret:
        default_auth = True
    else:
        default_auth = False
except:
    default_auth = False

tl_default_num = 30
tweet_tmpl = "\n[%s] : %s >> %s"

class TwCmd(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.intro = banner.twcmd_banner
        self.prompt = "Twitter >>> "
        self.auth = None
        self.api = None
        self.auth = None
        self.key = None
        self.secret = None


    def emptyline(self):
        pass


    def do_tw(self, tweet):
        try:
            if self.api:
                s = tweet.decode(in_encode).encode(out_encode)
                self.api.update_status(s)
            else:
                print "Please login using 'login' command first"

        except Exception, e:
            print "Tweet failed : ", e
            

    def do_mentions(self, dummy):
        try:
            mentions = self.api.mentions()
            mentions.reverse()
            for m in mentions:
                print (tweet_tmpl 
                       % (m.created_at, m.user.screen_name, m.text))
        except:
            pass
                

    def do_tl(self, line):
        s = line.split()
        
        try:
            num = tl_default_num
            if len(s) > 0:
                try:
                    num = int(s[0])
                except Exception, e:
                    print e
            
            timeline = self.api.home_timeline(count=num)
            timeline.reverse()
            for tw in timeline:
                print (tweet_tmpl 
                       % (tw.created_at, tw.user.screen_name, tw.text))

        except Exception, e:
            print e

    def help_tl(self):
        print "usage : tl [# of tweets]"


    def do_user(self, line):
        usernames = line.split()
        users = [tweepy.api.get_user(u) for u in usernames]
        for u in users:
            print ("\n[%s] %s (%s) : following %s  follower %s\n\t%s"
                   % (u.id, u.screen_name, u.name, u.friends_count, 
                      u.followers_count, u.description, ))


    def do_login(self, line):
        s = line.split()
        try:
            auth = tweepy.OAuthHandler(conf.consumer_key,
                                       conf.consumer_secret)

            if not default_auth:
                redirect_url = auth.get_authorization_url()
                print ("\nGet PIN code from following URL and input it\n%s\n"
                       % redirect_url)
                verifier = raw_input("input PIN code: ").strip()

                auth.get_access_token(verifier)
                self.key = auth.access_token.key
                self.secret = auth.access_token.secret

            else:
                self.key = conf.access_token
                self.secret = conf.access_secret

            auth.set_access_token(self.key, self.secret)
            self.api = tweepy.API(auth)
            print "%s logged in" % self.api.me().screen_name
            self.auth = auth

        except Exception, e:
            print e
            self.help_login()

    def help_login(self):
        print banner.help_login


if __name__ == '__main__':

    tw = TwCmd()
    tw.cmdloop()
