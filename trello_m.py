#!/usr/bin/python3

import argparse
import sys
import urllib.parse
import requests
import json
import os

## Function will take trello board URL and return member list on board
def urlpar(url_in,apikey,apitoken):

        if url_in is None:
                print("Please provide url ", file=sys.stderr)
                sys.exit(-1)

        value = urllib.parse.urlsplit(url_in)
        if (value.path.split('/')[1]) is 'b':
                print('Public board')
                boardid = (value.path.split('/')[2])
        else:
                print('Private board')

        url_main = "https://api.trello.com/1/boards/" + boardid + "/members"

        query = {
                'key': apikey,
                'token': apitoken
        }

        response = requests.get(url=url_main, params=query)

        data = response.json()


        user_list = []

        countu = ((len(data)) - 1 )

        for i in range(countu,0,-1):
                user_name = (data[i]['username'])
                user_list.append(user_name)
        return user_list

def memboard(memname,apikey,apitoken):
        url_member = "https://api.trello.com/1/members/" + memname + "/boards"
        query = {
                'key': apikey,
                'token': apitoken
        }

        response1 = requests.get(url=url_member, params=query)
        meminf = response1.json()
        url_list = []
        countm = ((len(meminf)) - 1 )
        for i in range(countm,0,-1):
                mem_url = (meminf[i]['shortUrl'])
                url_list.append(mem_url)
        return url_list

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="This Program will find all the possible boards by Iterating each member from URL")
        parser.add_argument("--url", type=str, help="Trello board url")
        args = parser.parse_args()

        url_in = args.url
        apikey = '251ca555a6d608bf1194663049e85976'
        apitoken = 'e691835a2c788c9ac224c1445e4752e847e607aed3cc79e299d68b0721968a5e'
        memurl_list = []
        uname = urlpar(url_in,apikey,apitoken)
        for y in range(len(uname)):
                print('User Name: %s' % uname[y])
                json_body = memboard(uname[y],apikey,apitoken)
                for x in range(len(json_body)):
                        print('URL: %s' % json_body[x])
                        memurl_list.append(json_body[x])
        print(len(set(memurl_list)))
