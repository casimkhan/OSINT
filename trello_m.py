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

## Function will take username and return URL list of boards
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
        for i in range(countm,1,-1):
                mem_url = (meminf[i]['shortUrl'])
                url_list.append(mem_url)
        return url_list

if __name__ == "__main__":


        parser = argparse.ArgumentParser(description="This Program will find all possible members of trello boards and Iterating each member to find further board URL")
        parser.add_argument("--url", type=str, help="Trello board url")
        args = parser.parse_args()

        url_in = args.url
 ## Your Trello API Key and API Token
        apikey = 'YOUR API KEY'
        apitoken = 'Your token'
        mem_list = []
        memurl_list = []
        uname = urlpar(url_in,apikey,apitoken)
        for y in range(len(uname)):
                print('User Name: %s' % uname[y])
                url_list_m = memboard(uname[y],apikey,apitoken)
                for x in range(len(url_list_m)):
                        if url_list_m[x] not in memurl_list:
                                print('New URL : %s' % url_list_m[x])
                                memurl_list.append(url_list_m[x])
 
        print('Total Public board URLs found: %d' % len(set(memurl_list)))
