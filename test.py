import praw
import moon
import json
from userpw import *

# tickerimg = imggen.imggen()

#reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
#                     username=username, password=password,
#                     user_agent=user_agent)

#print(reddit.user.me())
#sub = reddit.subreddit('cryptocurrencymoons')

# print(sub.title)
# ss = sub.stylesheet()
# print(ss.stylesheet)

#moons = moon.getmoons()
#print(moons)
#total = moon.gettotal()
#print(total["distribution"]["totalAvailable"])

one = "one"
if 'one' in locals():
    print("One Exists")

if 'two' in locals():
    print("Two Exists")
else:
    print("Two Does Not Exist")

#with open('cachedmoons.json', 'r') as f:
#    j = json.load(f)
#print(j)

#moondata = moon.getmoons()

#if j != moondata:
#    print("NO")
#else:
#    print("YES")

#try:
#    with open('top10.txt', 'r') as top10:
#        f.write("{} - successfully got ticker data\n".format(str(datetime.now())))
#    cmcdata = cmc.getcmc()
#    cmctext = ''
#    for i in cmcdata["data"]:
#        print(i["id"], i["slug"])
#        cmctext += "{0}. **{1} ({2}) - ${3:.2f}B - ${4:.2f}**\n".format(i["cmc_rank"], i["name"], i["symbol"], float(i["quote"]["USD"]["market_cap"])/1e9, float(i["quote"]["USD"]["price"]))
#    cmctext = cmctext[:-1]
#    print(cmctext)
#    with open('pyticker.log', 'a') as f:
#        f.write("{} - successfully got ticker data\n".format(str(datetime.now())))
#except:
#    print("Failed")

#rankings = '>| **TOP 10 USERS** | **MOONS** | **RANK** |\n>| :--- | ---: | ---: |\n'
#for i in moons:
#    print(i)
#    rankings += "> | u/{0} | {1} | {2} |\n".format(i["userName"], int(round(float(i["score"])/1e18, 0)), i["position"])
#print(rankings)
#totalmoons = ">**MOONS**\n>\n>| {0} |\n>| :--- |\n>| Total |".format(f"{int(round(float(total['distribution']['totalAvailable']))/1e18):,}")
#print(totalmoons)


# settings = praw.models.reddit.subreddit.SubredditModeration(sub).settings()
# sidebar_contents = settings['description']
# print (sidebar_contents)
# sub.stylesheet.upload("ticker", "img/temp/ticker.png")
# sub.stylesheet.update(stylesheettext)
