import requests
import json
import re
import os
import sys
from twilio.rest import Client
import time 
import random
 
account_sid = ''  #Enter your Twilio SID here
auth_token = '' #Enter your Twilio Auth Token here
client = Client(account_sid, auth_token)
url = ''  #Enter livestream URL here

def getContinuationParam():
    headers = {'user-agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    src = r.text.replace('\\', '')
    with open("ytsrc.txt", "w", encoding="utf-8") as f:
        f.write(src)
    regex = r'{"liveChatRenderer":{"continuations":\[{"reloadContinuationData":{"continuation":".*?"'
    result = re.findall(regex, src)
    regexedText = result[0]
    continuationParameter = regexedText[81:-1]
    print(continuationParameter)

    while 1:
        getLiveChat(continuationParameter)
        time.sleep(30)

def getLiveChat(contParam):
    base_url = 'https://www.youtube.com/live_chat/get_live_chat'
    params = {'continuation' : contParam, 'pbj':'1'}
    headers = {'user-agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", 'Content-Type': 'application/json'}
    response = requests.get(base_url, params=params, headers=headers)

    if response:
        print('Response OK',end=' ')

    else:
        print(f'Response Failed',end=' ')

    print(f'Status Code: {response.status_code}')
    jsonresponse = response.text
    with open("ytsrc.txt", "w", encoding="utf-8") as f:
        f.write(jsonresponse)
    data = json.loads(jsonresponse)
    getMessages(data)


def getMessages(data):
    chats = []
    actions = data['response']['continuationContents']['liveChatContinuation']['actions']
    for x in actions:
        if 'addChatItemAction' in x.keys():
            item = x['addChatItemAction']['item']
            if 'liveChatTextMessageRenderer' in item.keys():
                runs = item['liveChatTextMessageRenderer']['message']['runs'][0]
                if 'text' in runs.keys():
                    chats.append(runs['text'])  
    for chat in chats:
        print(chat)
    findLink(chats)

def findLink(messages):
    for message in messages:
        if (message.find('tinyurl') != -1) or (message.find('docs.google') != -1):
            print('Attendance Link Found')
            print(message)
            notify(message)
            exit()

def notify(message):
    print(message)
    os.system('curl https://notify.run/O9RDzj1oQskxzw04 -d "Attendance link has been posted. You have 3 minutes nibba gogogogo"')
    notif = 'curl https://notify.run/O9RDzj1oQskxzw04 -d "' + message + '"'
    os.system(notif)
    ph_nos = [] #Enter a list of phone numbers to text via Twilio. Remember to include +country code
    for number in ph_nos:
        message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body= message,      
                              to= 'whatsapp:' + number 
                          )

    
getContinuationParam()
