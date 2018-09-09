# -*- coding: utf-8 -*-
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia, pafy
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

#aditmadzs = LineClient()
aditmadzs = LineClient(authToken='Ev5JMRiB0M2xrC7MFSt3.m7QAK9mmg/fv3Yt11op1GW.d7WQoheQcafTIi85Oeb22qEW2rOe4RRUsewcJLb147M=')
aditmadzs.log("Auth Token : " + str(aditmadzs.authToken))
channel = LineChannel(aditmadzs)
aditmadzsMid = aditmadzs.profile.mid
aditmadzs.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(aditmadzs)
call = aditmadzs

mid = aditmadzs.getProfile().mid

admin = ["uac8e3eaf1eb2a55770bf10c3b2357c33","u33ba9a93d30c1be155df24f5d4e3f583"]

KAC = [aditmadzs]
Bots = ["u33ba9a93d30c1be155df24f5d4e3f583"]
Aditmadzs = admin

welcome = []
simisimi = []
translateen = []
translatetr = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

aditmadzsProfile = aditmadzs.getProfile()
myProfile["displayName"] = aditmadzsProfile.displayName
myProfile["statusMessage"] = aditmadzsProfile.statusMessage
myProfile["pictureStatus"] = aditmadzsProfile.pictureStatus

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentiongift":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "unsend":False,
    "mention":"Di baca doang ish :(",
    "Respontag":"Im busy huh",
    "welcome":"Selamat Datang",
    "leave":"Selamat Jalan",
    "comment":"Auto like by PUY\nhttps://line.me/ti/p/~yapuy",
    "message":"Thx For Added Rinda",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))


def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Mentioning {} Members\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ All {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ Successfully ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "{} Sider".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ Total {} Siders ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ Successfully ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nInGroup: "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ Successfully ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Out Members{}\nSelamat Jalan  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nGrup Ismi : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ Successfully ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@puy "
    if mids == []:
        raise Exception("Lost Time")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Lost Time")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = aditmadzs.getAllContactIds()
        gid = aditmadzs.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\n Expired : In "+hari+"\n Version :  Premium\n Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n Runtime : \n "+bot
        aditmadzs.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpMessage = " " "          // HELPER //      " + "\n" + \
                  " " "1) " + key + " Rinda Help\n" + \
                  " " "2) " + key + " Rinda Help group\n" + \
                  " " "3) " + key + " Rinda bye\n" + \
                  " " "4) " + key + " About Rinda\n" + \
                  "    // Proceed To Auto Translate //     " + "\n\n" + \
                  " " "          // AUTO TERJEMAH //      " + "\n" + \
                  " " "1) " + key + "Terjemah arab*on/off\n" + \
                  " " "2) " + key + "Terjemah english*on/off\n" + \
                  " " "3) " + key + "Terjemah indo*on/off\n" + \
                  "    // Proceed To Public Command //     " + "\n\n" + \
                  " " "          // ALL CAN USED [ MEDIA ] //      " + "\n" + \
                    " " "1) " + key + " Asking [query]" + "\n" + \
                    " " "2) " + key + " Hasil Dari [query]/[contoh : Hasil dari 22x22]" + "\n" + \
                    " " "3) " + key + " Timezone [query]" + "\n" + \
                    " " "4) " + key + " Smule [query]" + "\n" + \
                    " " "5) " + key + " Bitcoin" + "\n" + \
                    " " "6) " + key + " Twitter [query]" + "\n" + \
                    " " "6) " + key + " alquran: [surah]" + "\n" + \
                    " " "7) " + key + " Memelist" + "\n" + \
                    " " "7) " + key + " Playlist [artist]" + "\n" + \
                    " " "8) " + key + " Randomlose" + "\n" + \
                    " " "9) " + key + " Playstore [query]" + "\n" + \
                    " " "10) " + key + " Rinda get Motivation" + "\n" + \
                    " " "11) " + key + " Rinda get Suggestion to [query]" + "\n" + \
                    " " "12) " + key + " Rinda get devianart [query]" + "\n" + \
                    " " "13) " + key + " Rinda get Image [query]" + "\n" + \
                    " " "14) " + key + " Rinda get Quotes" + "\n" + \
                    " " "15) " + key + " Rinda get 1Cak" + "\n" + \
                    " " "16) " + key + " Rinda get video [query]" + "\n" + \
                    " " "17) " + key + " Rinda get Wikipedia [query]" + "\n" + \
                    " " "18) " + key + " Rinda memelist" + "\n" + \
                    " " "19) " + key + " Rinda getmeme dwight*Hei*Rin" + "\n" + \
                    " " "20) " + key + " Rinda get lockscreen [query]" + "\n" + \
                    " " "21) " + key + " Rinda get creepypasta" + "\n" + \
                    " " "22) " + key + " Rinda get gif [query]" + "\n" + \
                  "    // Ended Command //     " + "\n\n" + \
                  "   Use < " + key + " > For the Prefix" + "\n" + \
                  "    <Creator : @!>"
    return helpMessage

def helpgroup():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpGroup =   "    Helper      " + "\n" + \
                  " " + key2 +" " + "\n" + \
                  " " + "\n" + \
                  "        Help Bot " + "\n" + \
                  "          Menu " + "\n" + \
                  " " + key + "Gift: Mid korban Jumlah \n" + \
                  " " + key + "Spam: Mid korban Jumlah \n" + \
                  "   Use < " + key + " > For the Prefix" + "\n" + \
                  "   <Creator : @!>"
    return helpGroup

def helpgroups():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpGroups =  " " "< Helper Group >" + "\n" + \
                  " " "1) " + key + "Mentioning\n" + \
                  " " "2) " + key + "Rinda bye\n" + \
                  " " "3) " + key + "Ginfo\n" + \
                  " " "4) " + key + "Bukaqr\n" + \
                  " " "5) " + key + "tutupqr\n" + \
                  " " "6) " + key + "Url grup\n" + \
                  " " "8) " + key + "Rinda grouplist\n" + \
                  " " "9) " + key + "Rinda groupinfo [numb]\n" + \
                  " " "10) " + key + "Rinda get memberlist to [numb]\n" + \
                  " " "11) " + key + "Rinda get reader on/off\n" + \
                  " " "12) " + key + "Rinda get readers\n" + \
                  " " "14) " + key + "Changegp\n" + \
                  "  Use < " + key + " > For the Prefix" + "\n" + \
                  "  <Creator : @!>"
    return helpGroups
    
def helpstaff():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpStaff =   "         < Staff Only >     " + "\n" + \
                  " " "1) " + key + "Rinda Pause" + "\n" + \
                  " " "2) " + key + "Rinda Comeon" + "\n" + \
                  " " "3) " + key + "Rinda update" + "\n" + \
                  " " "4) " + key + "Rinda Status" + "\n" + \
                  " " "5) " + key + "Rinda Runtime" + "\n" + \
                  " " "6) " + key + "Rinda Remove chat" + "\n" + \
                  " " "7) " + key + "Changenamecreator:Nama\n" + \
                  " " "8) " + key + "Resetnamecreator\n" + \
                  " " "9) " + key + "Rinda + admin:on\n" + \
                  " " "10) " + key + "Rinda - admin @\n" + \
                  " " "11) " + key + "Rinda + admin @\n" + \
                  " " "12) " + key + "Rinda refresh admin\n" + \
                  " " "13) " + key + "Rinda adminlist\n" + \
                  " " "14) " + key + "Rinda setspamtag:\n" + \
                  " " "15) " + key + "Rinda setspamcall:\n" + \
                  " " "16) " + key + "Rinda spamtag @\n" + \
                  " " "17) " + key + "Rinda spamcall\n" + \
                  " " "18) " + key + "Rinda look sidermsg\n" + \
                  " " "19) " + key + "Rinda look spammsg\n" + \
                  " " "20) " + key + "Rinda look autoreplymsg\n" + \
                  " " "21) " + key + "Rinda look responmsg\n" + \
                  " " "22) " + key + "Rinda look welcomemsg\n" + \
                  " " "23) " + key + "Rinda look leavemsg\n" + \
                  " " "24) " + key + "Rinda Set sidermsg:\n" + \
                  " " "25) " + key + "Rinda Set spammsg:\n" + \
                  " " "26) " + key + "Rinda Set pesanmsg:\n" + \
                  " " "27) " + key + "Rinda Set responmsg:\n" + \
                  " " "28) " + key + "Rinda Set welcomemsg:\n" + \
                  " " "29) " + key + "Rinda Set leavemsg:\n" + \
                  " " "30) " + key + "Rindabc:\n" + \
                  " " "31) " + key + "Setprefix [query]\n" + \
                  " " "32) " + key + "Myprefix\n" + \
                  " " "33) " + key + "Resetprefix\n" + \
                  " " "34) " + key + "Changedp\n" + \
                  " " "35) " + key + "Rejecting\n\n" + \
                  "  Use < " + key + " > For the Prefix" + "\n" + \
                  "  <Creator : @!>"
    return helpStaff
    
def helpsett():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpSettingg =     "         < Rinda Settings >     " + "\n" + \
                       " " "1) " + key + "Rinda Help\n" + \
                       " " "2) " + key + "Rinda unsendmsg on/off\n" + \
                       " " "3) " + key + "Rinda Joinqr on/off\n" + \
                       " " "4) " + key + "Sticker on/off\n" + \
                       " " "5) " + key + "Respon on/off\n" + \
                       " " "6) " + key + "Respongift on/off\n" + \
                       " " "7) " + key + "Getinfo on/off\n" + \
                       " " "8) " + key + "Autojoin on/off\n" + \
                       " " "9) " + key + "Autoadd on/off\n" + \
                       " " "10) " + key + "Welcomemsg on/off\n" + \
                       " " "11) " + key + "Simi on/off\n" + \
                       " " "12) " + key + "Autoleave on/off\n\n" + \
                       "  Use < " + key + " > For the Prefix" + "\n" + \
                       "  <Creator : @!>"
    return helpSettingg
    
def helpremote():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpRemote =       " " "< Remote Control >" + "\n\n" + \
                       " " "1) " + key + " Rinda grouplist" + "\n" + \
                       " " "2) " + key + " Rinda groupinfo [numb of groups]" + "\n" + \
                       " " "3) " + key + " Rinda get Memberlist to [num of groups]" + "\n" + \
                       " " "4) " + key + " Rinda Mention to [number of groups]" + "\n" + \
                       " " "5) " + key + " Rinda leave to [number of groups]" + "\n" + \
                       " " "6) " + key + " Rinda crash to [number of groups]" + "\n" + \
                       " " "7) " + key + " Rinda bukaqr to [number of groups]" + "\n" + \
                       " " "8) " + key + " Rinda tutupqr to [number of groups]" + "\n\n" + \
                       "  Use < " + key + " > For the Prefix" + "\n" + \
                       "  <Creator : @!>"
    return helpRemote
    
groupParam = ""
def SiriGetOut(targ):
    aditmadzs.kickoutFromGroup(groupParam,[targ])
    #ar1.kickoutFromGroup(groupParam,[targ])
    #ar2.kickoutFromGroup(groupParam,[targ])
def byuh(targ):
    random.choice(KAC).kickoutFromGroup(groupParam,[targ])
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        aditmadzs.leaveGroup(op.param1)
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Thx for Invited Rinda to Group!\nPerintah < Rinda help >\nInGroup <" +str(ginfo.name) + ">")
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Thx for Invited Rinda to Group!\nPerintah < Rinda help >\nInGroup <" +str(ginfo.name) + ">")

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 19:
            if op.param1 in setting["protectionkick"]:
                if op.param2 not in settings["admin"]:
                    try:
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        aditmadzs.findAndAddContactsByMid(op.param3)
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 not in wait["blacklist"]:
                        wait["blacklist"].append(op.param2)
                    else:
                        pass
                
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in admin:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        aditmadzs.sendMessage(op.param1, wait["message"])

        if op.type == 55:
            try:
                if op.param1 in Setmain["ADITMADZSreadPoint"]:
                   if op.param2 in Setmain["ADITMADZSreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ADITMADZSreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = aditmadzs.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = aditmadzs.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        aditmadzs.sendImageWithURL(op.param1, image)


        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = aditmadzs.getGroup(at)
                                ariftj = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  " Gambar Dihapus \n Pengirim : "
                                ret_ = "  Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n  Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ariftj.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ariftj.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                ariftj = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  " Pesan Dihapus \n"
                                ret_ += "  Pengirim : {}".format(str(ariftj.displayName))
                                ret_ += "\n  Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n  Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n  Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                ariftj = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  " [*Pesan Stiker Ditarik*]\n"
                                ret_ += " <Pengirim : {}".format(str(ariftj.displayName)) + ">"
                                ret_ += "\n  <Nama Grup : {}".format(str(ginfo.name)) + ">"
                                ret_ += "\n  <Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"]))) + ">"
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://leert.corrykalam.gq/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               aditmadzs.sendMessage(msg.to, str(data["answer"]))
                   except Exception as error:
                       pass

               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, wait["Respontag"])
                           aditmadzs.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               #if 'MENTION' in msg.contentMetadata.keys() != None:
               #  if wait["Mentiongift"] == True:
               #    name = re.findall(r'@(\w+)', msg.text)
               #    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
               #    mentionees = mention['MENTIONEES']
               #    for mention in mentionees:
               #         if mention ['M'] in Bots:
               #            idth = ["ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
               #            plihth = random.choice(idth)
               #            jenis = ["5","6","7","8"]
               #            plihjenis = random.choice(jenis)
               #            aditmadzs.sendMessage(msg.to, "Rinda here kak (^) Ketik Rinda help untuk Perintah")
               #            aditmadzs.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
               #            break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, "Hm?")
                           #aditmadzs.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"Sticker ID\n STKID : " + msg.contentMetadata["STKID"] + "\n STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n STKVER : " + msg.contentMetadata["STKVER"]+ "\n\nLink Sticker" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : \n" + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}

            if msg.contentType == 1:
                    path = aditmadzs.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Picture Below',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n Sticker Url : line://shop/detail/{}".format(pkg_id)
                   #ret_ += "\n• Sticker ID : {}".format(stk_id)
                   #ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   #ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   #ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = aditmadzs.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nLink Sticker" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        aditmadzs.sendMessage(msg.to,"Dia udah menjadi admin Rindaaaaaa")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan dia menjadi admin Rinda.")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dia dari admin Rinda kak")
                    else:
                        wait["delladmin"] = True
                        aditmadzs.sendMessage(msg.to,"Dia bukan admin rinda kak")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = aditmadzs.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            aditmadzs.sendMessage(msg.to, "Berhasil mengganti avatar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = aditmadzs.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     aditmadzs.updateGroupPicture(msg.to, path)
                     aditmadzs.sendMessage(msg.to, "Group Picture has been Changed")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ADITMADZSfoto"]:
                            path = aditmadzs.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][mid]
                            aditmadzs.updateProfilePicture(path)
                            aditmadzs.sendMessage(msg.to,"Display Picture has been Changed")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        aditmadzs.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "rinda help":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               helpMessage = help()
                               #aditmadzs.sendMessage(msg.to, str(helpMessage))
                               poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                               #creator = aditmadzs.getContact(poey)
                               sendMentions(msg.to, str(helpMessage), [poey])

                        if cmd == "rinda comeon":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                aditmadzs.sendMessage(msg.to, "Rinda aktif kembali")

                        elif cmd == "rinda pause":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                aditmadzs.sendMessage(msg.to, "Rinda diberhentikan sementara")

                        elif cmd == "rinda help remote":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                               helpRemote = helpremote()
                               #aditmadzs.sendMessage(msg.to, str(helpRemote))
                               sendMentions(msg.to, str(helpRemote), [poey])
                               
                        elif cmd == "rinda help sett":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                               helpSettingg = helpsett()
                               #aditmadzs.sendMessage(msg.to, str(helpSettingg))
                               sendMentions(msg.to, str(helpSettingg), [poey])
                               
                        elif cmd == "rinda help staff":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                               helpStaff = helpstaff()
                               #aditmadzs.sendMessage(msg.to, str(helpStaff))
                               sendMentions(msg.to, str(helpStaff), [poey])
                               
                        elif cmd == "rinda help group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                               helpGroups = helpgroups()
                               #aditmadzs.sendMessage(msg.to, str(helpGroups))
                               sendMentions(msg.to, str(helpGroups), [poey])

                        elif cmd.startswith("about rinda"):
                            try:
                                arr = []
                                Ownerz = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = aditmadzs.getContact(Ownerz)
                                contact = aditmadzs.getContact(aditmadzsMid)
                                grouplist = aditmadzs.getGroupIdsJoined()
                                contactlist = aditmadzs.getAllContactIds()
                                blockedlist = aditmadzs.getBlockedContactIds()
                                ret_ = " "
                                ret_ += " Bot Name : {}".format(contact.displayName)
                                ret_ += "\n  In Groups : {}".format(str(len(grouplist)))
                                ret_ += "\n  Friends : {}".format(str(len(contactlist)))
                                ret_ += "\n  Blocked Account : {}".format(str(len(blockedlist)))                                    
                                #ret_ += "\n  [ About Selfbot ]"
                                #ret_ += "\n  Version : Premium"
                                #ret_ += "\n  Creator : {}".format(creator.displayName)
                                #ret_ += "\n  Creator : @x".format(Owner)
                                aditmadzs.sendMessage(to, str(ret_))
                                #puy.sendMessage(to, " Read Text Below ")
                                sendMentions(msg.to, "< About Rinda >\n\nThe Beginning of this Bot Comes from Helloworld, I'm just Reworked This!\n\nOf Course Special Thanks To HelloWorld, And the Friends Around Me!\n\n*Creator : @!", [Ownerz])
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))                               
                               
                        if cmd == "rinda unsendmsg on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")

                        if cmd == "rinda unsendmsg off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")

                        elif cmd == "rinda status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = " < S T A T U S >\n\n"
                                if wait["unsend"] == True: md+=" [*Unsend Actived*]\n"
                                else: md+=" [*Unsend Unactived*]\n"
                                if wait["sticker"] == True: md+=" [*StickerInfo Actived*]\n"
                                else: md+=" [*StickerInfo Unactived*]\n"
                                if wait["contact"] == True: md+=" [*GetInfo Actived*]\n"
                                else: md+=" [*GetInfo Unactived*]\n"
                                if wait["Mentionkick"] == True: md+=" [*Mentionkick Actived*]\n"
                                else: md+=" [*Mentionkick Unactived*]\n"
                                if wait["detectMention"] == True: md+=" [*Autoreplytag Actived*]\n"
                                else: md+=" [*Autoreplytag Unactived*]\n"
                                if wait["Mentiongift"] == True: md+=" [*Mentiongift Actived*]\n"
                                else: md+=" [*Mentiongift Unactived*]\n"
                                if wait["autoJoin"] == True: md+=" [*AutoJoin Actived*]\n"
                                else: md+=" [*AutoJoin Unactived*]\n"
                                if settings["autoJoinTicket"] == True: md+=" [*JoinQR Actived*]\n"
                                else: md+=" [*JoinQR Unactived*]\n"
                                if msg.to in simisimi: md+=" [*Simisimi Actived*]\n"
                                else: md+=" [*Simisimi Unactived*]\n"
                                if wait["autoAdd"] == True: md+=" [*AutoaddMsg Actived*]\n"
                                else: md+=" [*AutoaddMsg Unactived*]\n"
                                if msg.to in welcome: md+=" [*WelcomeMsg Actived*]\n"
                                else: md+=" [*WelcomeMsg Unactived*]\n"
                                if wait["autoLeave"] == True: md+=" [*LeaveMsg Actived*]\n"
                                else: md+=" [*LeaveMsg Unactived*]\n"
                                aditmadzs.sendMessage(msg.to, md+"\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n<"+ datetime.strftime(timeNow,'%H:%M:%S')+">\n")

                        elif cmd == "status autoterjemah":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = " < Status Terjemahan >\n\n"
                                if msg.to in translateen: md+=" English Actived\n"
                                else: md+=" English Unactived\n"
                                if msg.to in translateid: md+=" Indonesia Actived\n"
                                else: md+=" Indonesia Unactived\n"
                                if msg.to in translatear: md+=" Arab Actived\n"
                                else: md+=" Arab Unactived\n"
                                aditmadzs.sendMessage(msg.to, md+"\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "rinda creator" or text.lower() == 'creatorr':
                            #if msg._from in admin:
                                #aditmadzs.sendMessage(msg.to,"Creator Bot")
                                ma = ""
                                for i in admin:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about rindaaa" or cmd == "informasiii":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               sendMention(msg.to, sender, "Bot Name : Rinda\n")
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "meee" or text.lower() == 'meeee':
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               aditmadzs.sendMessage1(msg)

                        elif text.lower() == "mymid":
                               aditmadzs.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, " Nama : "+str(mi.displayName)+"\n Mid : " +key1+"\n Status Msg"+str(mi.statusMessage))
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(aditmadzs.getContact(key1)):
                                   aditmadzs.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   aditmadzs.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif cmd.startswith("stealname "):
                          if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = aditmadzs.getContact(ls)
                                      aditmadzs.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)

                        elif cmd.startswith("stealbio "):
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = aditmadzs.getContact(ls)
                                      aditmadzs.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)

                        elif cmd.startswith("stealpicture "):
                            if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line-cdn.net/" + aditmadzs.getContact(ls).pictureStatus
                                        aditmadzs.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("stealcover "):
                            if msg._from in admin:
                                if line != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = aditmadzs.getProfileCoverURL(ls)
                                            aditmadzs.sendImageWithURL(msg.to, str(path))
                        elif cmd.startswith("stealvideoprofile "):
                            if msg._from in admin:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            contact = aditmadzs.getContact(target)
                                            path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                            aditmadzs.sendVideoWithURL(msg.to, path)
                                        except Exception as e:
                                            pass

                        elif cmd.startswith("mycopy "):
                            if msg._from in admin:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        for mention in mentionees:
                                            contact = mention["M"]
                                            break
                                        try:
                                            aditmadzs.cloneContactProfile(contact)
                                            aditmadzs.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                        except:
                                            aditmadzs.sendMessage(msg.to, "Gagal clone member")

                        elif cmd.startswith("mybackup"):
                            if msg._from in admin:
                                try:
                                    aditmadzsProfile.displayName = str(myProfile["displayName"])
                                    aditmadzsProfile.statusMessage = str(myProfile["statusMessage"])
                                    aditmadzsProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    aditmadzs.updateProfileAttribute(8, aditmadzsProfile.pictureStatus)
                                    aditmadzs.updateProfile(aditmadzsProfile)
                                    aditmadzs.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                            aditmadzs.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = aditmadzs.getGroupIdsJoined()
                               for group in saya:
                                   aditmadzs.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "myprefix":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Mykey\nSetkey " + str(Setmain["keyCommand"]) + " ")

                        elif cmd.startswith("setprefix "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   aditmadzs.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   aditmadzs.sendMessage(msg.to, "Setkey diterapkan menjadi {}".format(str(key).lower()))

                        elif text.lower() == "resetprefix":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               aditmadzs.sendMessage(msg.to, "Prefix Berhasil diupdate")

                        elif cmd.startswith("changenamecreator: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   aditmadzs.sendMessage(msg.to, "Gagal mengganti nama creator")
                               else:
                                   Setmain["namecreator"] = str(key).lower()
                                   aditmadzs.sendMessage(msg.to, "Nama creator diterapkan menjadi {}".format(str(key).lower()))

                        elif text.lower() == "resetnamecreator":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["namecreator"] = "NADYA_AR"
                               aditmadzs.sendMessage(msg.to, "Nama creator berhasil diupdate")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["restartPoint"] = msg.to
                               aditmadzs.sendMessage(msg.to, "Tunggu sebentar...")
                               time.sleep(3)
                               aditmadzs.sendMessage(msg.to, "3...")
                               time.sleep(2)
                               aditmadzs.sendMessage(msg.to, "2...")
                               time.sleep(2)
                               aditmadzs.sendMessage(msg.to, "1...")
                               time.sleep(2)
                               aditmadzs.sendMessage(msg.to, "Restart Sukses...")
                               restartBot()

                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               aditmadzs.sendMessage(msg.to,bot)

                        elif cmd == "ginfo":
                          #if msg._from in admin:
                            try:
                                G = aditmadzs.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                aditmadzs.sendMessage(msg.to, " BOT Grup Info\n\n Nama Group : {}".format(G.name)+ "\n ID Group : {}".format(G.id)+ "\n Pembuat : {}".format(G.creator.displayName)+ "\n Waktu Dibuat : {}".format(str(timeCreated))+ "\n Jumlah Member : {}".format(str(len(G.members)))+ "\n Jumlah Pending : {}".format(gPending)+ "\n Group Qr : {}".format(gQr)+ "\n Group Ticket : {}".format(gTicket))
                                aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          #if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " BOT Grup Info\n"
                                ret_ += "\n  Nama Group : {}".format(G.name)
                                ret_ += "\n  ID Group : {}".format(G.id)
                                ret_ += "\n  Pembuat : {}".format(gCreator)
                                ret_ += "\n  Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n  Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n  Jumlah Pending : {}".format(gPending)
                                ret_ += "\n  Group Qr : {}".format(gQr)
                                ret_ += "\n  Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                aditmadzs.sendMessage(to, str(ret_))
                            except:
                                pass
## RINDA SC ##

                        elif cmd.startswith("instainfo: "):
                            #query = cmd.replace("instainfo: ","")
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                tj = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = " < Instagram Info > \n\n"
                                details = "\n\n< Ava Below >"
                                aditmadzs.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                aditmadzs.sendImageWithURL(msg.to, tj)
                            except Exception as njer:
                                #aditmadzs.sendMessage(msg.to, " Wikipedia Search < " + query + " > ")
                                aditmadzs.sendMessage(msg.to, str(njer))
                                #aditmadzs.sendMessage(msg.to, " Wikipedia Search < " + query + " > " + str(e))
                                
                        elif 'rinda search id: ' in msg.text:
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = aditmadzs.findContactsByUserid(msgs)
                              if True:
                                  aditmadzs.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                
                        elif cmd.startswith("rinda setspamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ADITMADZSlimit"] = num
                                aditmadzs.sendMessage(msg.to,"Jumlah Spamtag telah diterapkan menjadi <" +strnum + ">")

                        elif cmd.startswith("rinda setspamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                aditmadzs.sendMessage(msg.to,"Jumlah Spamcall telah diterapkan menjadi <" +strnum + ">")

                        elif cmd.startswith("rinda spamtag "):
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ADITMADZSlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                aditmadzs.sendMessage1(msg)
                                            except Exception as e:
                                                aditmadzs.sendMessage(msg.to,str(e))
                                    else:
                                        aditmadzs.sendMessage(msg.to,"Jumlah melebihi 1000")

                        elif cmd == "rinda spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                aditmadzs.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        aditmadzs.sendMessage(msg.to,str(e))
                                else:
                                    aditmadzs.sendMessage(msg.to,"Jumlah melebihi batas")                                
                                
                        elif cmd.startswith("rinda get lirik "):
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("*")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = " [ List Lirik ] "
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  [ Total {} Lagu ]".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n{}Lirik {}*nomor".format(str(),str(search))
                                    ret_ += "\n {}Playlist {}*nomor ".format(str(),str(search))
                                    PUY.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        PUY.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass                                
                                
                        elif cmd.startswith("alquran:"):
                            #if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    with requests.session() as web:
                                        r = requests.get("http://api.alquran.cloud/surah/{}/ar.alafasy".format(str(search)))
                                        data = r.text
                                        data = json.loads(data)
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]))
                                        for quran in data["data"]["ayahs"]:
                                            no += 1
                                            ret_ += "\n{}. {}".format(str(no),quran["text"])
                                        aditmadzs.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                     pass
                                
                        elif cmd.startswith("rinda bye"):
                            heij = aditmadzs.getGroupIdsJoined()
                            #G = aditmadzs.getGroup(heij)
                            #aditmadzs.sendMessage(to, "Gbye {}".format(str(G.name)))
                            aditmadzs.sendMessage(to, "Gbye")
                            #aditmadzs.getGroupIdsJoined()
                            aditmadzs.leaveGroup(to)
                                
                        elif cmd.startswith("rinda get wikipedia "):
                            query = cmd.replace("rinda get wikipedia ","")
                            try:
                                sep = msg.text.split(" ")
                                wiki = msg.text.replace(sep[0] + " ","")
                                wikipedia.set_lang("id")
                                pesan=" Judul <"
                                pesan+=wikipedia.page(wiki).title + ">"
                                pesan+="\n\n Teks : "
                                pesan+=wikipedia.summary(wiki, sentences=1)
                                pesan+="\n\n [Alamat url] "+wikipedia.page(wiki).url
                                pesan+="\n"
                                aditmadzs.sendMessage(to, pesan)
                            except:
                                    try:
                                        pesan="Teks terlalu panjang, Klik url untuk lebih lengkap\n"
                                        pesan+=wikipedia.page(wiki).url
                                        #aditmadzs.sendMessage(to, pesan)
                                        aditmadzs.sendMessage(to, " Wikipedia Search < " + query + " >  " + pesan)
                                    except Exception as e:
                                        #aditmadzs.sendMessage(to, "Wikipedia [ " + query + " ] " + str(e))
                                        aditmadzs.sendMessage(msg.to, " Wikipedia Search < " + query + " > " + str(e))
                        elif cmd.startswith("vidcall"):
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  group = aditmadzs.getGroup(to)
                                  for mention in mentionees:
                                       if mention["M"] not in lists:
                                           lists.append(mention["M"])
                                  for ls in lists:
                                      for var in range(0,50):                                         
                                          aditmadzs.acquireGroupCallRoute(to)                                            
                                          members = [ls for ls in lists]
                                          aditmadzs.inviteIntoGroupCall(to, contactIds=members)
                                      try:
                                          aditmadzs.sendMessage(to,"Ready to Vidcall in Private chat with "+aditmadzs.getContact(ls).displayName)
                                      except Exception as error:
                                          logError(error)
                                
                        elif cmd.startswith("randomlose"):
                            group = aditmadzs.getGroup(to)
                            try:
                                members = [mem.mid for mem in group.members]
                            except:
                                members = [mem.mid for mem in group.members]
                            message = random.choice(members)
                            sendMentions(to, "< RandomLoseMem >\n\n• The Loser is :", [sender])
                            aditmadzs.sendContact(to, message)
                                
                        elif cmd.startswith("rinda getmeme "):
                            query = cmd.replace("rinda getmeme ","")
                            #data = r.text
                            #data = json.loads(data)
                            meme = query.split('*')
                            meme = meme[0].replace(' ','_')
                            atas = query.split('*')
                            atas = atas[1].replace(' ','_')
                            bawah = query.split('*')
                            bawah = bawah[2].replace(' ','_')
                            memes = 'https://memegen.link/'+meme+'/'+atas+'/'+bawah+'.jpg'
                            aditmadzs.sendMessage(msg.to, "Search Meme < " + query + " >")
                            aditmadzs.sendImageWithURL(msg.to, memes)                                
                                
                        elif cmd == 'memelist':
                            aditmadzs.sendMessage(to,"10 Guy = tenguy\nAfraid to Ask Andy = afraid\nAn Older Code Sir, But It Checks Out = older\nAncient Aliens Guy = aag\nAt Least You Tried = tried\nBaby Insanity Wolf = biw\nBad Luck Brian = blb\nBut That's None of My Business = kermit\nButthurt Dweller = bd\nCaptain Hindsight = ch\nComic Book Guy = cbg\nCondescending Wonka = wonka\nConfession Bear = cb\nConspiracy Keanu = keanu\nDating Site Murderer = dsm\nDo It Live! = live\nDo You Want Ants? = ants\nDoge = doge\nDrake Always On Beat = alwaysonbeat\nErmahgerd = ermg\nFirst World Problems = fwp\nForever Alone = fa\nFoul Bachelor Frog = fbf\nFuck Me, Right? = fmr\nFuturama Fry = fry\nGood Guy Greg = ggg\nHipster Barista = hipster\nI Can Has Cheezburger? = icanhas\nI Feel Like I'm Taking Crazy Pills = crazypills\nI Immediately Regret This Decision! = regret\nI Should Buy a Boat Cat = boat\nI Would Be So Happy = sohappy\nI am the Captain Now = captain\nInigo Montoya = inigo\nInsanity Wolf = iw\nIt's A Trap! = ackbar\nIt's Happening = happening\nIt's Simple, Kill the Batman = joker\nJony Ive Redesigns Things = ive\nLaughing Lizard = ll\nMatrix Morpheus = morpheus\nMilk Was a Bad Choice = badchoice\nMinor Mistake Marvin = mmm\nNothing To Do Here = jetpack\nOh, Is That What We're Going to Do Today? = red\nOne Does Not Simply Walk into Mordor = mordor\nOprah You Get a Car = oprah\nOverlay Attached Girlfriend = oag\nPepperidge Farm Remembers = remembers\nPhilosoraptor = philosoraptor\nProbably Not a Good Idea = jw\nSad Barack Obama = sad-obama\nSad Bill Clinton = sad-clinton\nSad Frog / Feels Bad Man = sadfrog\nSad George Bush = sad-bush\nSad Joe Biden = sad-biden\nSad John Boehner = sad-boehner\nSarcastic Bear = sarcasticbear\nSchrute Facts = dwight\nScumbag Brain =  sb\nScumbag Steve = ss\nSealed Fate = sf\nSee? Nobody Cares = dodgson\nShut Up and Take My Money! = money\nSo Hot Right Now = sohot\nSocially Awesome Awkward Penguin = awesome-awkward\nSocially Awesome Penguin = awesome\nSocially Awkward Awesome Penguin = awkward-awesome\nSocially Awkward Penguin = wkward\nStop Trying to Make Fetch Happen = fetch\nSuccess Kid = success\nSuper Cool Ski Instructor = ki\nThat Would Be Great = officespace\nThe Most Interesting Man in the World = interesting\nThe Rent Is Too Damn High = toohigh\nThis is Bull, Shark = bs\nWhy Not Both? = Both\nWinter is coming = winter\nX all the Y = xy\nX, X Everywhere = buzz\nXzibit Yo Dawg = yodawg\nY U NO Guy = yuno\nY'all Got Any More of Them = yallgot\nYou Should Feel Bad = bad\nYou Sit on a Throne of Lies = elf\nYou Were the Chosen One! = chosen\n\nUsage : Rinda getmeme sohot*Hello*Rin")                                
                                
                        elif cmd.startswith("rinda get quotes"):
                            r=requests.get("https://talaikis.com/api/quotes/random")
                            data=r.text
                            data=json.loads(data)
                            hasil = "  [ Search Random Quote ]\n\n"
                            hasil += "Genre : " +str(data["cat"])
                            hasil += "\n\n" +str(data["quote"])
                            hasil += "\n\n From : " +str(data["author"])+ " "
                            aditmadzs.sendMessage(msg.to, str(hasil))                                
                                
                        elif cmd.startswith("rinda get video "):
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl=("https://www.youtube.com" + results['href'])
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = " < Video Search >\n"
                                    hasil += "\n [Judul] : {}".format(str(vid.title))
                                    hasil += "\n [Nama channel] : {}".format(str(vid.author))
                                    hasil += "\n [Durasi vidio] : " + str(vid.duration) + " Quality : " + s.quality + " "
                                    hasil += "\n [Nilai] : " + str(vid.rating)
                                    hasil += "\n [Penonton] : " + str(vid.viewcount) + "x"
                                    hasil += "\n [Published] : " + str(vid.published)
                                    hasil += "\n [Pencarian : Youtube]"
                                    hasil += "\n\n Video Below"
                                aditmadzs.sendMessage(msg.to,hasil)
                                aditmadzs.sendVideoWithURL(msg.to,vin)
                                print("[YOUTUBE]MP4 Succes")
                            except Exception as e:
                                aditmadzs.sendMessage(to, str(e))                                
                                
                        elif cmd.startswith("asking "):
                            query = cmd.replace("asking ","")
                            #kata = cmd.replace("asking ", "")
                            sch = query.replace(" ","+")
                            with requests.session() as web:
                               urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                               r = web.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                               data = r.text
                               data = json.loads(data)
                               url = data["shorturl"]
                               ret_ = "\n"
                               ret_ += " => Link : {}".format(str(url))
                               #aditmadzs.sendMessage(to, str(ret_))
                               aditmadzs.sendMessage(msg.to, "Question is < " + query + " > " + str(ret_))

                        elif cmd.startswith("rinda tutupqr to"):
                          if msg._from in admin:
                            number = cmd.replace("rinda tutupqr to","")
                            groups = aditmadzs.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = True
                                    aditmadzs.updateGroup(G)
                                except:
                                    G.preventedJoinByTicket = True
                                    aditmadzs.updateGroup(G)
                                aditmadzs.sendMessage(to, "Closing Qr\nInGroup : <" + G.name + ">")
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))
                  
                        elif cmd.startswith("rinda bukaqr to"):
                          if msg._from in admin:
                            number = cmd.replace("rinda bukaqr to","")
                            groups = aditmadzs.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    aditmadzs.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    aditmadzs.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                aditmadzs.sendMessage(to, "Opening Qr\nInGroup : <" + G.name + ">\n  Url : " + gurl)
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))
                               
                        elif cmd.startswith("rinda crash to"):
                          if msg._from in admin:
                            number = cmd.replace("rinda crash to","")
                            groups = aditmadzs.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    aditmadzs.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                except:
                                    aditmadzs.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                aditmadzs.sendMessage(to, "Send Crash To Group : " + G.name)
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))                               
                               
                        elif cmd.startswith("rinda leave to"):
                          if msg._from in admin:
                            number = cmd.replace("rinda leave to","")
                            groups = aditmadzs.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    #aditmadzs.sendMessage(to, "Gbye")
                                    aditmadzs.leaveGroup(G.id)
                                except:
                                    #aditmadzs.sendMessage(to, "Gbye")
                                    aditmadzs.leaveGroup(G.id)
                                aditmadzs.sendMessage(to, "Leave To Group : " + G.name)
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))
                               
                        elif cmd == "rinda grouplist":
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = "   [ Group List ]"
                            no = 0
                            for gid in groups:
                                group = aditmadzs.getGroup(gid)
                                no += 1
                                ret_ += "\n{}. {} = {} Members".format(str(no), str(group.name), str(len(group.members)))
                            ret_ += "\n   [ Total {} Groups ]".format(str(len(groups)))
                            aditmadzs.sendMessage(to, str(ret_))
                               
                        elif cmd.startswith("rinda groupinfo "):
                            #if msg._from in admin:
                            number = cmd.replace("rinda groupinfo ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                path = "http://dl.profile.line-cdn.net/" + G.pictureStatus
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " < Group Info > \n"
                                ret_ += "\n Nama Group : {}".format(G.name)
                                ret_ += "\n ID Group : \n{}".format(G.id)
                                ret_ += "\n Pembuat Grup : {}".format(gCreator)
                                ret_ += "\n Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n Jumlah Pending : {}".format(gPending)
                                ret_ += "\n Group Qr : {}".format(gQr)
                                ret_ += "\n Group Ticket : {}".format(gTicket)
                                ret_ += "\n\n < Kontak Pembuat dibawah >"
                                aditmadzs.sendImageWithURL(to, path)
                                aditmadzs.sendMessage(to, str(ret_))
                                aditmadzs.sendContact(to, G.creator.mid)
                            except:
                                pass                               
                               
                        elif cmd.startswith("rinda get memberlist to"):
                            #if msg._from in admin:
                            number = cmd.replace("rinda get memberlist to","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                no = 0
                                ret_ = " < Member List >\n"
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " + str(no) + ". " + mem.displayName
                                aditmadzs.sendMessage(to,"Member in Group : \n"+ str(G.name) + "\n\n" + ret_ + "\n\nTotal ada %i Members" % len(G.members))
                            except: 
                                pass                               
                               
                        elif cmd.startswith("rinda mention to"):
                            #if msg._from in Owner:
                            number = cmd.replace("rinda mention to","")
                            groups = aditmadzs.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    contact = [mem.mid for mem in G.members]
                                    text = "Mentioning To %i Members\n" %len(contact)
                                    no = 1
                                    for mid in contact:
                                        text += "\n{}. @!           ".format(str(no))
                                        no = (no+1)
                                    text += "\n\nInGroup : {}".format(str(G.name))
                                    sendMentions(group, text, contact)
                                except:
                                    contact = [mem.mid for mem in G.members]
                                    text = "Mentioning To %i Members\n" %len(contact)
                                    no = 1
                                    for mid in contact:
                                        text += "\n{}. @!           ".format(str(no))
                                        no = (no+1)
                                    text += "\n\nInGroup : {}".format(str(G.name))
                                    sendMentions(group, text, contact)
                                aditmadzs.sendMessage(to, "Send Mention To Group : " + G.name)
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))
                               
                        elif cmd.startswith("twitter "):
                            query = cmd.replace("twitter ","")
                            b = urllib.parse.quote(query)
                            aditmadzs.sendMessage(to, "https://www.twitter.com/"+query)
                            
                        elif cmd.startswith("playstore "):
                            query = cmd.replace("playstore ","")
                            aditmadzs.sendMessage(to, "< Search Playstore : "+query+" >\nhttps://play.google.com/store/search?q="+query)
                            
                        elif cmd.startswith("github "):
                            query = cmd.replace("github ","")
                            b = urllib.parse.quote(query)
                            aditmadzs.sendMessage(to, " " + b + "\nhttps://github.com/search?utf8=?&q="+query)
                            
                        elif cmd.startswith("rinda get image "):
                            try:
                                query = cmd.replace("rinda get image ","")
                                #search = cmd.replace("rinda image ","")
                                r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(query))
                                data = r.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    aditmadzs.sendMessage(to, " Search Image < " + query + " >")
                                    aditmadzs.sendImageWithURL(to, str(path))
                            except Exception as error:
                                 logError(error)
                                 var= traceback.print_tb(error.__traceback__)
                                 aditmadzs.sendMessage(to,str(var))
                            
                        elif cmd.startswith("rinda get devianart "):
                            query = cmd.replace("rinda get devianart ","")
                            try:
                                search = cmd.replace("rinda get devianart ","")
                                r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                data = r.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    aditmadzs.sendMessage(msg.to, "Search Image < " + query + " >")
                                    aditmadzs.sendImageWithURL(to, str(path))
                            except Exception as error:
                                 logError(error)
                                 var= traceback.print_tb(error.__traceback__)
                                 aditmadzs.sendMessage(to,str(var))
                            
                        elif cmd.startswith("rinda get suggestion to "):
                            query = cmd.replace("rinda get suggestion to ","")
                            puy1 = requests.get("http://api.ntcorp.us/se/v1/?q={}".format(urllib.parse.quote(query)))
                            data=puy1.text
                            data=json.loads(data)
                            no = 0
                            ret_ = "\n"
                            anu = data["result"]["suggestions"]
                            for s in anu:
                                hmm = s
                                no += 1
                                ret_ += "\n" + str(no) + ") " + "{}\n".format(str(hmm))
                            aditmadzs.sendMessage(msg.to, " This is Suggestion to < " + query + " >  " + str(ret_))
                            
                        elif cmd.startswith("rinda get gif "):
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("*")
                            search = str(count[0])
                            r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="+str(search))
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "       < Gifs Menu >\n"
                                for aa in data["results"]:
                                    no += 1
                                    hasil += "\n" + str(no) + ") " + str(aa["title"])
                                    ret_ = "\n\nRinda {}*number".format(str(search))
                                aditmadzs.sendMessage(to,hasil+ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["results"][num - 1]
                                    c = str(b["id"])
                                    hasil = " Gif ID : "+str(c)
                                    hasil += ""
                                    aditmadzs.sendMessage(msg.to,hasil)
                                    dl = str(b["media"][0]["loopedmp4"]["url"])
                                    aditmadzs.sendVideoWithURL(msg.to,dl)
                                except Exception as e:
                                    aditmadzs.sendMessage(to," "+str(e))
                            
                        elif cmd.startswith("rinda get lockscreen "):
                            #if msg._from in admin:
                            query = cmd.replace("rinda get lockscreen ","")
                            cond = query.split("*")
                            search = str(cond[0])
                            result = requests.get("https://api.eater.tech/wallp/{}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = "[ Lockscreen Search ]\n"
                                for sam in data["result"]:
                                    num += 1
                                    ret_ += "\n{}. {}".format(str(num),str(sam["judul"]))
                                ret_ += "\n\nMore : Rinda get lockscreen {}*(number) to Details.".format(str(search))
                                aditmadzs.sendMessage(to, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["result"]):
                                    sam = data["result"][num - 1]
                                    result = requests.get("https://api.eater.tech/wallp/{}".format(str(search)))
                                    data = result.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        aditmadzs.sendImageWithURL(to, str(sam["link"]))
                            
                        elif cmd.startswith("rinda get 1cak"):
                            r=requests.get("http://api-1cak.herokuapp.com/random")
                            data=r.text
                            data=json.loads(data)
                            hasil = "< 1CAK Result >"
                            hasil += "\n\n  Judul : \n " + str(data["title"])
                            hasil += " \n\n  ID : " +str(data["id"])
                            hasil += "\n  URL : " + str(data["url"])
                            hasil += "\n  Rates : " + str(data["votes"])
                            hasil += "\n  Nsfw : " + str(data["nsfw"])
                            image = str(data["img"])
                            #puy.sendImageWithURL(msg.to, str(image))
                            aditmadzs.sendMessage(msg.to, str(hasil))
                            
                        elif cmd.startswith("square"):
                            number = cmd.replace("square","")
                            squares = aditmadzs.getJoinedSquares().squares
                            ret_ = " Square \n"
                            try:
                                square = squares[int(number)-1]
                                path = "http://dl.profile.line-cdn.net/" + square.profileImageObsHash
                                ret_ += "\n1. Name : {}".format(str(square.name))
                                ret_ += "\n2. Description: {}".format(str(square.desc))
                                ret_ += "\n3. ID Square : {}".format(str(square.mid))
                                ret_ += "\n4. Link : {}".format(str(square.invitationURL))
                                aditmadzs.sendImageWithURL(to, path)
                                aditmadzs.sendMessage(to, str(ret_))
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))                            
                            
                        elif cmd.startswith("rindabc: "):
                            if msg._from in admin:
                              sep = text.split(" ")
                              pesan = text.replace(sep[0] + " ","")
                              saya = aditmadzs.getGroupIdsJoined()
                              for group in saya:
                                 aditmadzs.sendMessage(group,"" + str(pesan))                            
                            
                        elif cmd.startswith("bitcoin"):
                            puy1 = requests.get("https://xeonwz.herokuapp.com/bitcoin.api")
                            data=puy1.text
                            data=json.loads(data)
                            hasilnya = "< Bitcoin >\n" 
                            hasilnya += "\n Price : " +str(data["btc"])
                            hasilnya += "\n Expensive : " +str(data["high"])
                            hasilnya += "\n Cheap : " +str(data["low"])
                            aditmadzs.sendMessage(msg.to, str(hasilnya))                            
                            
                        elif cmd.startswith("rinda get creepypasta"):
                            r=requests.get("http://hipsterjesus.com/api")
                            data=r.text
                            data=json.loads(data)
                            hasil = " < Creepypasta > \n\n" 
                            hasil += str(data["text"])
                            aditmadzs.sendMessage(msg.to, str(hasil))

                        elif cmd.startswith("rinda get motivation"):
                            puy1 = requests.get("https://talaikis.com/api/quotes/random")
                            data=puy1.text
                            data=json.loads(data)
                            aditmadzs.sendMessage(to, " < Motivation > \n" + str(data["quote"]))
                            
                        elif cmd.startswith("hasil dari "):
                            query = cmd.replace("hasil dari ","")
                            puy1 = requests.get("https://www.calcatraz.com/calculator/api?c={}".format(urllib.parse.quote(query)))
                            data=puy1.text
                            data=json.loads(data)
                            aditmadzs.sendMessage(msg.to, query + " Hasilnya " + str(data))
                            
                        elif cmd.startswith("timezone "):
                            try:
                                query = cmd.replace("timezone ","")
                                #search = cmd.replace("timezone ","")
                                r = requests.get("https://time.siswadi.com/geozone/{}".format(urllib.parse.quote(query)))
                                data=r.text
                                data=json.loads(data)
                                ret_ = "\n"
                                ret_ += "\n Latitude : |" +str(data["data"]["latitude"]) + "|"
                                ret_ += "\n Longitude : |" +str(data["data"]["longitude"]) + "|"
                                ret_ += "\n Address : |" +str(data["data"]["address"]) + "|"
                                ret_ += "\n Country : |" +str(data["data"]["country"]) + "|"
                                #puy.sendMessage(to, str(ret_))
                                aditmadzs.sendMessage(to, " < Timezone " + query + " >" + str(ret_))
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))
                                
                        elif cmd.startswith("rinda get imageart "):
                            try:                                   
                                search = cmd.replace("rinda get imageart ","")
                                puy1 = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                data = puy1.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    aditmadzs.sendMessage(to,"Image in #%s From #%s." %(str(a),str(b)))
                                    aditmadzs.sendImageWithURL(to, str(path))
                                    log.info("Art #%s from #%s." %(str(a),str(b)))                                    
                            except Exception as error:
                                logError(error)
                                traceback.print_tb(error.__traceback__)                                
## RINDA SC ##

                        elif cmd.startswith("rinda get playlist "):
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("*")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "[ List Lagu ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  [ {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nFor Details Ketik \n{}Rinda get lirik {}*nomor".format(str(),str(search))
                                    ret_ += "\n{}Rinda get lirik {}*nomor ".format(str(),str(search))
                                    aditmadzs.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "[ Detail Musik ]"
                                            ret_ += "\n Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n Size : {}".format(str(data["result"]["size"]))
                                            #ret_ += "\n Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n<Audio Below>"
                                            aditmadzs.sendMessage(msg.to, str(ret_))
                                            aditmadzs.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass

                        elif cmd.startswith("infomem "):
                          #if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " " "+ str(no) + ". " + mem.displayName
                                aditmadzs.sendMessage(to," Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except:
                                pass

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getAllContactIds()
                               for i in gid:
                                   G = aditmadzs.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += " " + str(a) + ". " +G.displayName+ "\n"
                               aditmadzs.sendMessage(msg.to," [ FRIEND LIST ]\n\n"+ma+"\n[ Total"+str(len(gid))+"Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getGroupIdsJoined()
                               for i in gid:
                                   G = aditmadzs.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += " " + str(a) + ". " +G.name+ "\n"
                               aditmadzs.sendMessage(msg.to,"[ GROUP LIST ]\n\n"+ma+"?\n[ Total?"+str(len(gid))+"Groups ]")

                        elif cmd == "bukaqr":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                if msg.toType == 2:
                                   X = aditmadzs.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   aditmadzs.updateGroup(X)
                                   aditmadzs.sendMessage(msg.to, "Url Opened")

                        elif cmd == "tutupqr":
                          #if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = aditmadzs.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   aditmadzs.updateGroup(X)
                                   aditmadzs.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                if msg.toType == 2:
                                   x = aditmadzs.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      aditmadzs.updateGroup(x)
                                   gurl = aditmadzs.reissueGroupTicket(msg.to)
                                   aditmadzs.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "spaminvid":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                dan = msg.text.split("|")
                                userid = dan[1]
                                namagrup = dan[2]
                                jumlah = int(dan[3])
                                grups = aditmadzs.groups
                                tgb = aditmadzs.findContactsByUserid(userid)
                                if jumlah <= 10:
                                    for var in range(0,jumlah):
                                        try:
                                            aditmadzs.createGroup(str(namagrup), [tgb.mid])
                                            for i in grups:
                                                grup = aditmadzs.getGroup(i)
                                                if grup.name == namagrup:
                                                    aditmadzs.inviteIntoGroup(grup.id, [tgb.mid])
                                                    aditmadzs.leaveGroup(grup.id)
                                                    sendMentions(msg.to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                        except Exception as Nigga:
                                            aditmadzs.sendMessage(msg.to, str(Nigga))
                                else:
                                    sendMentions(msg.to, "@! Whoops", [sender])

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = aditmadzs.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      aditmadzs.rejectGroupInvitation(gid)
                                  aditmadzs.sendMessage(to, "{} undangan grup tertolak".format(str(len(ginvited))))
                              else:
                                  aditmadzs.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                aditmadzs.sendMessage(msg.to,"Sent a Picture")

                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][mid] = True
                                aditmadzs.sendMessage(msg.to,"Sent a Picture")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = aditmadzs.getProfile()
                                profile.displayName = string
                                aditmadzs.updateProfile(profile)
                                aditmadzs.sendMessage(msg.to,"Nama diterapkan menjadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "mentioning" or text.lower() == 'bbb':
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               group = aditmadzs.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 100:
                                   mentionMembers(msg.to, nama)
                               if jml > 100 and jml < 200:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 200 and jml < 300:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 300 and jml < 400:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 400 and jml < 500:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, 399):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (400, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)

                        elif cmd == 'mentioninggr':
                            group = aditmadzs.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@! \n'
                                aditmadzs.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                aditmadzs.sendMessage(to, "Total {} Mention".format(str(len(nama))))

                        elif cmd == 'mentioningg':
                            gname = aditmadzs.getGroup(msg.to)
                            local = [contact.mid for contact in gname.members]
                            try:
                                lur = len(local)//20
                                for fu in range(lur+1):
                                    hdc = u''
                                    sell=0
                                    com=[]
                                    for rid in gname.members[fu*20 : (fu+1)*20]:
                                        com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                        sell += 7
                                        hdc += u'@A_RFU\n'
                                        atas = '\n InGroup < {} > '.format(str(gname.name))
                                        atas += '\n Mentioned to < {} > Members'.format(str(len(local)))
                                    aditmadzs.sendMessage(msg.to, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))

                        elif cmd == 'mentioningga':
                            gname = aditmadzs.getGroup(msg.to)
                            local = [contact.mid for contact in gname.members]
                            try:
                                arrData = ""
                                textx = "Mentioning {} Members\n\n  [ Mention ]\n1. ".format(str(len(local)))
                                arr = []
                                no = 1
                                num = 2
                                #lur = len(local)//20
                                #for fu in range(lur+1):
                                for i in mid:
                                    mention = "@x\n"
                                    slen = str(len(textx))
                                    elen = str(len(textx) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':i}
                                    arr.append(arrData)
                                    textx += mention
                                    if no < len(mid):
                                        no += 1
                                        textx += "%i. " % (num)
                                        num=(num+1)
                                    else:
                                        try:
                                            no = "\n[ All {} ]".format(str(aditmadzs.getGroup(to).name))
                                        except:
                                            no = "\n[ Successfully ]"
                                aditmadzs.sendMessage(msg.to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            except Exception as error:
                                aditmadzs.sendMessage(msg.to, "[ INFO ] Error :\n" + str(error))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"Rinda Admins\n\n"+mb+"\nAda%sAdmin" %(str(len(admin))))

                        elif cmd == "rinda bye":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                aditmadzs.sendMessage(msg.to, "Bye"+str(G.name))
                                aditmadzs.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = aditmadzs.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = aditmadzs.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = aditmadzs.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                aditmadzs.sendMessage(msg.to, "BOT Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               start = time.time()
                               aditmadzs.sendMessage(msg.to, "Wait...")
                               elapsed_time = time.time() - start
                               aditmadzs.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "rinda get reader on":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ADITMADZSreadPoint'][msg.to] = msg_id
                                 Setmain['ADITMADZSreadMember'][msg.to] = {}
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil dinyalakan\n\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "rinda get reader off":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ADITMADZSreadPoint'][msg.to]
                                 del Setmain['ADITMADZSreadMember'][msg.to]
                                 aditmadzs.sendMessage(msg.to, "Getreader berhasil dimatikan\n\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "rinda get readers":
                          #if msg._from in admin:
                            if msg.to in Setmain['ADITMADZSreadPoint']:
                                if Setmain['ADITMADZSreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ADITMADZSreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ {} Reader ]\n\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(aditmadzs.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n* "+ datetime.strftime(timeNow,'%H:%M:%S')+"* "
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        aditmadzs.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ADITMADZSreadPoint'][msg.to]
                                        del Setmain['ADITMADZSreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ADITMADZSreadPoint'][msg.to] = msg.id
                                    Setmain['ADITMADZSreadMember'][msg.to] = {}
                                else:
                                    aditmadzs.sendMessage(msg.to, "Tidak ada satupun")
                            else:
                                aditmadzs.sendMessage(msg.to, "Getreader status is Unactived")

                        elif cmd == "rinda get sider on":
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  aditmadzs.sendMessage(msg.to, "Get sider has been Actived\n\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n      [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "rinda get sider off":
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  aditmadzs.sendMessage(msg.to, "Get sider has been Unactived\n\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n      [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  aditmadzs.sendMessage(msg.to, "Sudak tidak aktif")

## RINDA SC 2##
                        elif cmd.startswith("musik: "):
                          #if msg._from in admin:
                            try:
                                search = msg.text.replace("musik: ","")
                                r = requests.get("https://farzain.com/api/joox.php?apikey=VBbUElsjMS84rXUO7wRlIwjFm&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = " Hasil Musik \n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                aditmadzs.sendImageWithURL(msg.to, str(data["gambar"]))
                                aditmadzs.sendMessage(msg.to, str(hasil))
                                aditmadzs.sendMessage(msg.to, "Downloading...")
                                aditmadzs.sendMessage(msg.to, " Result MP3 ")
                                aditmadzs.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                aditmadzs.sendMessage(msg.to, " Result M4A ")
                                aditmadzs.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                aditmadzs.sendMessage(msg.to, str(data["lirik"]))
                                aditmadzs.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	aditmadzs.sendMessage(msg.to, " Result Error \n" + str(error))

                        elif cmd.startswith("acaratv: "):
                          #if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                channel = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=al11241519&id="+channel)
                                data = r.text
                                data = json.loads(data)
                                aditmadzs.sendMessage(msg.to, "Acara TV Di "+channel+ ":\n" + str(data["url"]))
                            except Exception as error:
                            	pass

                        elif cmd.startswith("cl-telp: "):
                          #if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                nohp = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://apisora.herokuapp.com/prank/call/?no={}")
                                aditmadzs.sendMessage(msg.to, " cl Telepon \n Status : Success!!!\n No Tujuan : "+nohp)
                            except Exception as error:
                                pass

                        elif cmd.startswith("cl-sms: "):
                         # if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                nohp = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/cl.php?id="+nohp+"&type=1")
                                aditmadzs.sendMessage(msg.to, " cl Sms \n Status : Success!!!\n No Tujuan : "+nohp)
                            except Exception as error:
                                pass

                        elif cmd.startswith("cl call: "):
                          #if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = msg.text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/cl/call/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = " Prangked Telpon "
                            ret_ += "\n Status : {}".format(str(data["status"]))
                            ret_ += "\n Tujuan "+str(data["result"])
                            aditmadzs.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("ytmp4: "):
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n  Author : ' + str(vid.author)
                                    durasi = '\n  Duration : ' + str(vid.duration)
                                    suka = '\n  Likes : ' + str(vid.likes)
                                    rating = '\n  Rating : ' + str(vid.rating)
                                    deskripsi = '\n  Deskripsi : ' + str(vid.description)
                                aditmadzs.sendVideoWithURL(msg.to, me)
                                aditmadzs.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n  Author : ' + str(vid.author)
                                    durasi = '\n  Duration : ' + str(vid.duration)
                                    suka = '\n  Likes : ' + str(vid.likes)
                                    rating = '\n  Rating : ' + str(vid.rating)
                                    deskripsi = '\n  Deskripsi : ' + str(vid.description)
                                aditmadzs.sendImageWithURL(msg.to, me)
                                aditmadzs.sendAudioWithURL(msg.to, shi)
                                aditmadzs.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to,str(e))

                        elif cmd.startswith("cekig:"):
                            #if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHtJIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = " [ Profile Instagram ]"
                                        ret_ += "\n  Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n  Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n  Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n  URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n  Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n  Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n  Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n [ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        aditmadzs.sendMessage(to, str(ret_))
                                        aditmadzs.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          #if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            aditmadzs.sendMessage(msg.to," I N F O R M A S I \n\n"+" Date Of Birth : "+lahir+"\n Age : "+usia+"\n Ultah : "+ultah+"\n Zodiak : "+zodiak)

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, str(Setmain["ADITMADZSmessage1"]))
                                      
#=======================================================  RINDA SC 2 FINISHED =============================================================#
#=======================================================      SETTINGS   ==================================================================#
                        elif 'Simi ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    aditmadzs.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)

                        elif 'Terjemah english*' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('Terjemah english*','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs2 = "Auto Translate Has been Turned On"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Auto Translate To Eng has been Actived\nInGroup < " +str(ginfo.name) + " >"
                                  aditmadzs.sendMessage(msg.to, "" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Auto Translate To Eng has been Unactived\nInGroup < " +str(ginfo.name) + " >"
                                    else:
                                         msgs2 = "Auto Translate Has been Turned Off"
                                    aditmadzs.sendMessage(msg.to, "" + msgs)
                        elif 'Terjemah indo*' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('Terjemah indo*','')
                              if spl == 'on':
                                  if msg.to in translateid:
                                       msgs2 = "Auto Translate Has been Turned On"
                                  else:
                                       translateid.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Auto Translate To Indo has been Actived\nInGroup < " +str(ginfo.name) + " >"
                                  aditmadzs.sendMessage(msg.to, "" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateid:
                                         translateid.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Auto Translate To Indo has been Unactived\nInGroup < " +str(ginfo.name) + " >"
                                    else:
                                         msgs2 = "Auto Translate Has been Turned Off"
                                    aditmadzs.sendMessage(msg.to, "" + msgs)

                        elif 'Terjemah arab*' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Terjemah arab*','')
                              if spl == 'on':
                                  if msg.to in translatear:
                                       msgs2 = "Auto Translate Has been Turned On"
                                  else:
                                       translatear.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Auto Translate To Arab has been Actived\nInGroup < " +str(ginfo.name) + " >"
                                  aditmadzs.sendMessage(msg.to, "" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatear:
                                         translatear.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Auto Translate To Arab has been Unactived\nInGroup < " +str(ginfo.name) + " >"
                                    else:
                                         msgs2 = "Auto Translate Has been Turned Off"
                                    aditmadzs.sendMessage(msg.to, "" + msgs)
#=======================================================  SETTINGS FINISHED ===============================================================#
#=======================================================  PROTECTION ===============================================================#
                        elif 'Welcomemsg ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcomemsg ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Message berhasil diaktifkan"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Welcome Message has been Actived InGroup <" +str(ginfo.name) + ">"
                                  aditmadzs.sendMessage(msg.to, "" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Welcome Message has been Unactived InGroup <" +str(ginfo.name) + ">"
                                    else:
                                         msgs = "Welcome Message has been Unactived"
                                    aditmadzs.sendMessage(msg.to, "" + msgs)
                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                            aditmadzs.kickoutFromGroup(msg.to,[target])
                                       except:
                                           pass

                        elif ("Selam canim" in msg.text):
                            if wait["selfbot"] == True:
                                if msg.toType == 2:
                                    if msg._from in admin:
                                        #print "ok"
                                        _name = msg.text.replace("Selam canim","")
                                gs = aditmadzs.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    aditmadzs.sendText(msg.to,"Error")
                                else:
                                    for target in targets:
                                        try:
                                            aditmadzs.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                            aditmadzs.sendText(msg.to,"Done")
                        elif text.lower() == 'fuck@sirichan':
                            if msg._from in admin:
                                gs = aditmadzs.getGroup(msg.to)
                            gs = aditmadzs.getGroup(msg.to)
                            gs = aditmadzs.getGroup(msg.to)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko"," ","0","1","2","3","4","5","6","7","8","9"])]
                            if sirilist != []:
                                groupParam = msg.to
                                try:
                                    p = Pool(40)
                                    p.map(SiriGetOut,sirilist)
                                    p.close()
                                except:
                                    p.close()
                        elif text.lower() == 'nukedz':
                          if msg._from in admin:
                            if msg.toType == 2:
                                gs = aditmadzs.getGroup(msg.to)
                                #gs = ar1.getGroup(msg.to)
                                #gs = ar2.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    aditmadzs.sendText(msg.to,"kayak nya limit")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[aditmadzs]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        elif text.lower() == 'brokenz':
                            if msg._from in admin:
                                if msg.toType == 2:
                                    gs = aditmadzs.getGroup(msg.to)
                                gs.preventedJoinByTicket = False
                                aditmadzs.updateGroup(gs)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                aditmadzs.acceptGroupInvitationByTicket(msg.to,Ticket)
                                aditmadzs.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.1)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    aditmadzs.sendText(msg.to,"DRAG KICK OUT BYE")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[aditmadzs,aditmadzs,aditmadzs]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        elif msg.text in ['rinda cancel invitation']:
                            if msg.toType == 2:
                                #if msg._from in admin:
                                group = aditmadzs.getGroup(msg.to)

                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                    aditmadzs.cancelGroupInvitation(msg.to,[_mid])

                        elif msg.text in ["Gcancelall"]:
                            if msg._from in admin:
                                gid = aditmadzs.getGroupIdsInvited()
                                for i in gid:
                                    aditmadzs.rejectGroupInvitation(i)
                            if wait["lang"] == "JP":
                                aditmadzs.sendText(msg.to,"Success menolak semua undangan")
                            else:
                                aditmadzs.sendText(msg.to,"He declined all invitations")
#=======================================================  PROTECTION ===============================================================#
#=======================================================  ADMIN  ===============================================================#
                        elif ("Rinda+admin " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Rinda-admin " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   #if target not in Aditmadzs:
                                       try:
                                           admin.remove(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "rinda+admin:on" or text.lower() == 'rindaaddadmin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                aditmadzs.sendMessage(msg.to,"Sent a Contact")

                        elif cmd == "rinda-admin:on" or text.lower() == 'admin:remove':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                aditmadzs.sendMessage(msg.to,"Sent a Contact")

                        elif cmd == "rinda refresh admin" or text.lower() == 'refreshhh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                aditmadzs.sendMessage(msg.to,"Admin has been Refreshed")

                        elif cmd == "admin contact" or text.lower() == 'virüssz':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': 'sezer'}, contentType=13)
#=======================================================  ADMIN FINISHED ===============================================================#
#=======================================================  ON/OFF ===============================================================#
                        elif cmd == "rinda mentionkick on" or text.lower() == 'notagg on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                aditmadzs.sendMessage(msg.to,"Mentionkick has been Actived")

                        elif cmd == "rinda mentionkick off" or text.lower() == 'notagg off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                aditmadzs.sendMessage(msg.to,"Mentionkick has been Unactived")

                        elif cmd == "rinda getinfo on" or text.lower() == 'contactt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                aditmadzs.sendMessage(msg.to,"Getinfo has been Actived")

                        elif cmd == "rinda pro on" or text.lower() == 'rindapro':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                setting["protectionkick"] = True
                                aditmadzs.sendMessage(msg.to,"Rinda protect admin already on")
                                
                        elif cmd == "rinda pro off" or text.lower() == 'rindaproff':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                setting["protectionkick"] = False
                                aditmadzs.sendMessage(msg.to,"Rinda protect admin already off")
                                
                        elif cmd == "rinda getinfo off" or text.lower() == 'contactt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                aditmadzs.sendMessage(msg.to,"Getinfo has been Unactived")

                        elif cmd == "rinda autoreply on" or text.lower() == 'responn on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                aditmadzs.sendMessage(msg.to,"Auto reply has been Actived")

                        elif cmd == "rinda autoreply off" or text.lower() == 'responn off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                aditmadzs.sendMessage(msg.to,"Auto reply has been Unactived")

                        elif cmd == "rinda mentiongift on" or text.lower() == 'respongiftt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                aditmadzs.sendMessage(msg.to,"Mentiongift has been Actived")

                        elif cmd == "rinda mentiongift off" or text.lower() == 'respongiftt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                aditmadzs.sendMessage(msg.to,"Mentiongift has been Unactived")

                        elif cmd == "rinda autojoin on" or text.lower() == 'autojoinn on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                aditmadzs.sendMessage(msg.to,"Autojoin Set to On")

                        elif cmd == "rinda autojoin off" or text.lower() == 'autojoinn off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                aditmadzs.sendMessage(msg.to,"Autojoin Set to Off")

                        elif cmd == "rinda autoleave on" or text.lower() == 'autoleavee on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                aditmadzs.sendMessage(msg.to,"Autoleave Set to On")

                        elif cmd == "rinda autoleave off" or text.lower() == 'autoleavee off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                aditmadzs.sendMessage(msg.to,"Autoleave Set to Off")

                        elif cmd == "rinda autoadd on" or text.lower() == 'autoaddd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                aditmadzs.sendMessage(msg.to,"Autoadd Set to On")

                        elif cmd == "rinda autoadd off" or text.lower() == 'autoaddd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                aditmadzs.sendMessage(msg.to,"Autoadd Set to Off")

                        elif cmd == "rinda stickerinfo on" or text.lower() == 'stickerr on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                aditmadzs.sendMessage(msg.to,"StickerInfo Set to On")

                        elif cmd == "rinda stickerinfo off" or text.lower() == 'stickerr off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                aditmadzs.sendMessage(msg.to,"StickerInfo Set to Off")

                        elif cmd == "rinda joinqr on" or text.lower() == 'jointickett on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Join QR Set to On")

                        elif cmd == "rinda joinqr off" or text.lower() == 'jointickett off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Join QR Set to Off")
#=======================================================  ON/OFF FINISHED ===============================================================#
#=======================================================  SET/CHANGES ===============================================================#
                        elif 'Rinda set addedmsg: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Rinda set addedmsg: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal menerapkan Added Message")
                              else:
                                  wait["message"] = spl
                                  aditmadzs.sendMessage(msg.to, "Added Message diterapkan menjadi\n<{}>".format(str(spl)))

                        elif 'Rinda set welcomemsg: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Rinda set welcomemsg: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal menerapkan Welcome Members Message")
                              else:
                                  wait["welcome"] = spl
                                  aditmadzs.sendMessage(msg.to, "Rinda Welcome Members Message diterapkan menjadi\n<{}>".format(str(spl)))

                        elif 'Rinda set leavemsg: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Rinda set leavemsg: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal menerapkan LeaveMember Message")
                              else:
                                  wait["leave"] = spl
                                  aditmadzs.sendMessage(msg.to, "Rinda Leave Members Message diterapkan menjadi\n<{}>".format(str(spl)))

                        elif 'Rinda set autoreplymsg: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Rinda set autoreplymsg: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal menerapkan Autoreply Message")
                              else:
                                  wait["Respontag"] = spl
                                  aditmadzs.sendMessage(msg.to, "Rinda Reply Message diterapkan menjadi\n<{}>".format(str(spl)))

                        elif 'Rinda set spammsg: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Rinda set spammsg: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal menerapkan Spam Message")
                              else:
                                  Setmain["ADITMADZSmessage1"] = spl
                                  aditmadzs.sendMessage(msg.to, "Rinda Spam Message diterapkan menjadi\n<{}>".format(str(spl)))

                        elif 'Rinda set sidermsg: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Rinda set sidermsg: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal menerapkan Sider Message")
                              else:
                                  wait["mention"] = spl
                                  aditmadzs.sendMessage(msg.to, "Sider Message diterapkan menjadi\n< {} >".format(str(spl)))

                        elif text.lower() == "rinda look addedmsg":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Addedmsg yang diterapkan :\n <" + str(wait["message"]) + ">")

                        elif text.lower() == "rinda look welcomemsg":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Welcome Message yang diterpkan :\n <" + str(wait["welcome"]) + ">")

                        elif text.lower() == "rinda look leavemsg":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Leave Message yang diterapkan :\n <" + str(wait["leave"]) + ">")

                        elif text.lower() == "rinda look responmsg":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Respon Message yang diterapkan :\n <" + str(wait["Respontag"]) + ">")

                        elif text.lower() == "rinda look spammsg":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Spam Message yang diterapkan :\n <" + str(Setmain["ADITMADZSmessage1"]) + ">")

                        elif text.lower() == "rinda look sidermsg":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Sider Message yang diterapkan :\n <" + str(wait["mention"]) + ">")
#=======================================================  SET/CHANGES FINISHED ===========================================================#
#============================================================  QR JOINING ===========================================================#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     aditmadzs.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)
#=======================================================  QR JOINING FINISHED ===========================================================#

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
