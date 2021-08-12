import moon
import praw
import json
import re
from datetime import datetime
from userpw import *

#### Gets Moon Ranking Data and Converts to Reddit Sidebar Formatting ####
try:
    moondata = moon.getmoons()
    moontext = '>| **TOP 10 USERS** | **MOONS** | **RANK** |\n>| :--- | ---: | ---: |\n'
    for i in moondata:
        moontext += "> | u/{0} | {1} | #{2} |\n".format(i["userName"], int(float(i["score"])/1e18), i["position"])
    with open('pyticker.log', 'a') as f:
        f.write("{} - successfully got moon rankings data\n".format(str(datetime.now())))
except:
    with open('pyticker.log', 'a') as f:
        f.write("{} - failed to get moon rankings data\n".format(str(datetime.now())))
 
#### Gets Moon Total Data and Converts to Reddit Sidebar Formatting #### 
try:
    totaldata = moon.gettotal()
    totalmoons = ">**MOONS**\n>\n>| {0} |\n>| :--- |\n>| Total |".format(f"{int(round(float(totaldata['distribution']['totalAvailable']))/1e18):,}")
    with open('pyticker.log', 'a') as f:
        f.write("{} - successfully got moon total data\n".format(str(datetime.now())))
except:
    with open('pyticker.log', 'a') as f:
        f.write("{} - failed to get moon total data\n".format(str(datetime.now())))
        
try:

    #### Logs into Reddit Using userpw.py ###
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                         username=username, password=password,
                         user_agent=user_agent)   
                         
    #### Grabs Subreddit Sidebar Contents ####
    sub = reddit.subreddit('cryptocurrencymoons')
    settings = praw.models.reddit.subreddit.SubredditModeration(sub).settings()
    sidebar_contents = settings['description']
    
    #### Loads Last Version of Moon Rankings Data ####
    try:    
        with open('oldmoons.json') as oldm:
            oldmoons = json.loads(oldm)
    except:
        with open('pyticker.log', 'a') as f:
            f.write("{} - old moon data does not exist\n".format(str(datetime.now())))
            
    #### Checks to see if Old Data is different from New Data, or if Old Data didnt exist ####
    if 'oldmoons' not in locals() or oldmoons != moondata:
    
        #### Updates Rankings if Old Data is different from New Data, or if Old Data didnt exist ####
        print("Updating Rankings")
        if len(moontext) > 30:
            sidebar_contents = re.sub(r'(\>\| \*\*TOP 10 USERS.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+)', moontext, sidebar_contents)
            praw.models.reddit.subreddit.SubredditModeration(sub).update(description=sidebar_contents)
            with open ('oldmoons.json', 'w') as moonout:
                json.dump(moondata, moonout)
            with open('pyticker.log', 'a') as f:
                f.write("{} - successfully updated reddit with moon rankings\n".format(str(datetime.now())))
        else:
            with open('pyticker.log', 'a') as f:
                f.write("{} - failed because moontext too short\n".format(str(datetime.now())))
                
    #### If Old Data matches New Data, update skips ####
    else:
        print("Rankings Matched")



    #### Loads Last Version of Moon Total Data ####        
    try:    
        with open('oldtotal.json') as oldt:
            oldtotal = json.loads(oldt)
    except:
        with open('pyticker.log', 'a') as f:
            f.write("{} - old total data does not exist\n".format(str(datetime.now())))
            
    #### Checks to see if Old Data is different from New Data, or if Old Data didnt exist ####            
    if 'oldtotal' not in locals() or oldtotal != totaldata:
    
        #### Updates Rankings if Old Data is different from New Data, or if Old Data didnt exist ####
        print("Updating Total")
        if len(totalmoons) > 30:
            sidebar_contents = re.sub(r'(\>\*\*MOONS.+\n.+\n.+\n.+\n.+)', totalmoons, sidebar_contents)
            praw.models.reddit.subreddit.SubredditModeration(sub).update(description=sidebar_contents)
            with open ('oldtotal.json', 'w') as totalout:
                json.dump(totaldata, totalout)
            with open('pyticker.log', 'a') as f:
                f.write("{} - successfully updated reddit with moon total\n".format(str(datetime.now())))
        else:
            with open('pyticker.log', 'a') as f:
                f.write("{} - failed because totalmoons too short\n".format(str(datetime.now())))
                
    #### If Old Data matches New Data, update skips ####
    else:
        print("Totals Matched")
            
            
except:
    with open('pyticker.log', 'a') as f:
        f.write("{} - failed to update reddit\n".format(str(datetime.now())))
