import urllib2 as ul2
import ssl


url = "https://osu.ppy.sh/beatmapsets"
req = ul2.Request(url)

protocolContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) #Certificate bypass

html = ul2.urlopen(req, context = protocolContext).read() #Getting html code


beatmapList = []
currentStr = html
for i in range(10):
    titleLoc = currentStr.find('''"title":''')

    titleStart = titleLoc+9
    newStr = str( currentStr[titleStart:titleLoc+50] )
    titleEnd = newStr.find('''"''') + titleStart

    title = currentStr[titleStart:titleEnd]
    print(title)
    beatmapList.append(title)
    currentStr = currentStr[titleEnd:len(html)]

    
print(beatmapList)                                      #Printing titles of beatmaps

        

