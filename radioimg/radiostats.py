#! /usr/bin/python

import urllib2
url = "http://radio.99chan.org:32578/status2.xsl"
selectedMount="/musik"
backupmount="/zutomation"
class mount:
    def __init__(self, array):
        self.MountPoint = array[0]
        self.Connections = array[1]
        self.StreamName = array[2]
        self.CurrentListeners = array[3]
        self.PeakListeners = array[4]
        self.Description = array[5]
        self.CurrentlyPlaying = array[6][3:].replace("&amp","&")
        self.Bitrate = array[7]
        self.ContentType = array[8]
        self.Genre = array[9]
        self.StreamUrl = array[10]
        self.Uptime = array [11]


    def update(self):
        
        data = urllib2.urlopen(url).readlines()[4:]
        found = False
        for lines in data[:-1]:
            if self.MountPoint in lines.split('~'):
                found = True
                selected = lines.split('~')
                break
        assert found,"The list did not contain the mount"
        self.__init__(selected)

    def wat(self):
        print '<div id="NowPlaying">'
        print ("Now Playing on lolradio:" + self.CurrentlyPlaying + " @ " + self.Bitrate + "Kbps" +
        "<br />The current dj is: " + self.Description + "<br />There are Currently: " + self.CurrentListeners + " Listeners" +
        "<br />Peak Listeners: " + self.PeakListeners)
        print "</div>"



def request(String):
    req = string
    f = file("Request.txt","rw")
    f.write(string)
    f.flush()
    f.close()

def getStatus(selectedMount):
    mountname = selectedMount
    try:
        data = urllib2.urlopen(url).readlines()[4:]
    except:
        print "Couldn't get the data."
        exit(1)
    array = []
    found = False
    
    for lines in data[:-1]: # [:-1] because there is a left over <pre> tag in the data
     
        array.append(mount(lines.split('~')))
        
        if mountname in lines.split('~'):
            found = True
            selected = lines.split('~')
            break
        elif backupmount in lines.split('~'):
            found = True
            selected = lines.split('~')
    assert found,"The list did not contain the mount"
    stats = mount(selected)

    if stats.MountPoint != mountname:
        print "Mount not found trying backup"
        return getStatus(backupmount)
    return stats
    
m = getStatus(selectedMount)







