import urllib2 as ul2
import ssl
import webbrowser

def findstr(x,database):
    global loc
    global start
    global end
    loc = database.find(x)
    start = loc + len(x)+1
    newStr = str( database[start:start+50] )
    end = newStr.find('''"''') + start
    return database[start:end]

url = "https://osu.ppy.sh/beatmapsets"
req = ul2.Request(url)
protocolContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)                    #Certificate bypass
html = ul2.urlopen(req, context = protocolContext).read()               #Getting html code
beatmapList = []
currentStr = html

for i in range(10):
    title = findstr('''"title":''',currentStr)
    print(title)                                                        #Finds and Prints Beatmap Title and adds it to beatmapList
    beatmapList.append(title)
    titleEnd = end
    currentStr = currentStr[titleEnd:len(html)]                         #Updates current string we're looking at
    #---------------------------------------------------------------
    tempBmUrl = findstr('''"url":''',currentStr)                        #Url the way python pulls it from Html
    bmUrl = tempBmUrl.replace("\\","")                                  #Cleaned up url that Chrome can actually use
    print(bmUrl)
    req = ul2.Request(bmUrl)
    newBmUrl = ul2.urlopen(req,context = protocolContext).geturl()      #Certificate Bypass
    x = newBmUrl.find("#")
    dlBmUrl = newBmUrl[0:x] + '/download'                               #Forging of the download link
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(dlBmUrl)                           #Opening download link, hence downloading beatmap

print(beatmapList)                                                      #Printing titles of beatmaps
