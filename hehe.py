# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

#puy = LINE()
puy = LINE("EwuhZA80qfu0xweF11r3.Ri4/RX6YPvDWVXddSJv8mW.HRsSRNLX3CsPphvlDT/Faa55haNUr2qw7CmW8SYAZt8=")
#EwuhZA80qfu0xweF11r3.Ri4/RX6YPvDWVXddSJv8mW.HRsSRNLX3CsPphvlDT/Faa55haNUr2qw7CmW8SYAZt8= #IOSIPAD
#EwQwIzlS11Z27NBxeWe3.Ri4/RX6YPvDWVXddSJv8mW.sHMeFhhrCB4eDVPAPF0LwxKxJH6SNTYvtBO2uXW9bnE= #CHROME
#puy = LINE("Email","Password")
puy.log("Auth Token : " + str(puy.authToken))
channelToken = puy.getChannelResult()
puy.log("Channel Token : " + str(channelToken))

puyMID = puy.profile.mid
puyProfile = puy.getProfile()
lineSettings = puy.getSettings()
oepoll = OEPoll(puy)

offbot = []
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)

#PUYWAIT = {
#    "readMember":{},
#    "readPoint":{},
#    "readTime":{},
#    "ROM":{}
#}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

PuyCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

setTime = {}
setTime = read['readTime']
mulai = time.time()
msg_dict = {}

myProfile["displayName"] = puyProfile.displayName
myProfile["statusMessage"] = puyProfile.statusMessage
myProfile["pictureStatus"] = puyProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ RESTART NOTIFY ] MEMULAI ULANG BOT")
    backupData()
#    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    

def summon(to):
    try:
        arrData = ""
        ginfo = puy.getGroup(to)
        textx = "    Mention Members\n\n•1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "•{}. ".format(str(no))
            else:
                textx += "\nTotal: {} members".format(str(len(mid)))
        puy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink },0)
    except Exception as error:
        puy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def logError(text):
    puy.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        puy.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

Helpz ="""    「 Commands 」
Gsteal
Psteal"""

Profilez ="""    「 ProfileSteal 」
Type: Steal Profile

  1. Picture
  2. Bio
  3. Cover
  4. VidProfile
  5. MID
  6. Contact

Penggunaan: Psteal 「nomor」 「Mention」
Contoh: Psteal 1 @"""

Gprofilez ="""    「 GroupSteal 」
Type: Steal Group Information

  1. Foto Grup
  2. Nama Grup
  3. Pembuat Grup
  4. Anggota Grup
  5. Url
  6. ID Grup

Penggunaan: Gsteal 「nomor」
Contoh: Gsteal 1"""

Remotez ="""    「 RemoteCmd 」
Type: Remote Controls Command

 1. Bukaqr
 2. Tutupqr
 3. Crash
 4. Leave
 5. Groupinfo
 6. Mention
 7. Memberinfo

Penggunaan: Cmd to 「nomor grup」
Contoh: Urlon to 21"""
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Hening :(")
            return
        if op.type == 5:
            print ("[ 5 ] Ada yg add")
            if settings["autoAdd"] == True:
                puy.sendMessage(op.param1, "{} Thx for add me!".format(str(puy.getContact(op.param1).displayName)))
        if op.type == 13:
            print ("[ 13 ] Ada yg Invite Grup")
            group = puy.getGroup(op.param1)
            if settings["autoJoin"] == True:
                puy.acceptGroupInvitation(op.param1)

        if op.type == 24:
            print ("[ 24 ] Keluar Grup")
            if settings["autoLeave"] == True:
                puy.leaveRoom(op.param1)
        if op.type == 25:
            print ("[ 25 ] Mengirim Pesan")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != puy.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'help':
                    #helpMessage = helpmessage()
                    puy.sendMessage(to, str(Helpz))
                    #puy.sendContact(to, "u14f64e139a3817afaabe27d237afb36b")

                if text.lower() == 'psteal':
                    #helpMessage = helpmessage()
                    puy.sendMessage(to, str(Profilez))
                    #puy.sendContact(to, "u14f64e139a3817afaabe27d237afb36b")

                if text.lower() == 'gsteal':
                    #helpMessage = helpmessage()
                    puy.sendMessage(to, str(Gprofilez))
                    #puy.sendContact(to, "u14f64e139a3817afaabe27d237afb36b")

                if text.lower() == 'rcontrol':
                    #helpMessage = helpmessage()
                    puy.sendMessage(to, str(Remotez))
                    #puy.sendContact(to, "u14f64e139a3817afaabe27d237afb36b")
#==============================================================================#

###################### RANDOM ##########################
                elif msg.text.lower().startswith("say "):
                            if "MENTION" in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention['M'] not in lists:
                                        lists.append(mention['M'])
                                for ls in lists:
                                    contact = puy.getContact(ls)
                                hh = text.split(" ")
                                hh = text.replace(hh[0]+" "," ")
                                hh = hh.split('*')
                                txt = str(hh[0])
                                xz = text.replace(text.split(":")[0]+" "," ")
                                #print(xz)
                                puy.sendMessage(to, (txt),contentMetadata={"MSG_SENDER_NAME":"{}".format(contact.displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)})

                elif text.lower() == 'outvps':
                                #puy.mentionWithRFU(to,user,"!Exit","")
                                puy.sendMessage(to, 'Berhasil mematikan bot')
                                print ("BOT OFF")
                                exit(1)

                elif msg.text.lower().startswith("tolak undangan"):
                                ginvited = puy.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        puy.rejectGroupInvitation(gid)
                                    puy.sendMessage(to, "Berhasil menolak {} Undangan Grup".format(str(len(ginvited))))
                                else:
                                    puy.sendMessage(to, "Tidak ada undangan")

                elif msg.text.lower().startswith("url on"):
                                if msg.toType == 2:
                                    group = puy.getGroup(to)
                                    group.preventedJoinByTicket = False
                                    puy.updateGroup(group)

                elif msg.text.lower().startswith("url off"):
                                if msg.toType == 2:
                                    group = puy.getGroup(to)
                                    group.preventedJoinByTicket = True
                                    puy.updateGroup(group)

                elif text.lower() == "glist":
                            groups = puy.getGroupIdsJoined()
                            ret_ = "      「 Group List 」"
                            no = 0
                            for gid in groups:
                                group = puy.getGroup(gid)
                                no += 1
                                ret_ += "\n{}. {} = {} Members".format(str(no), str(group.name), str(len(group.members)))
                            ret_ += "\n   「 {} Groups 」".format(str(len(groups)))
                            puy.sendMessage(to, str(ret_))

                elif text.lower() == "byeme":
                    ginfo = puy.getGroup(to)
                    puy.sendMessage(to, "dadah {}".format(str(ginfo.name)))
                    puy.leaveGroup(to)
                    print ("Anda Keluar Grup")

                elif msg.text.lower().startswith("urlon to"):
                            number = text.replace("urlon to","")
                            groups = puy.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = puy.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    puy.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    puy.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(G.id)))
                                puy.sendMessage(to, "Opening Qr\nInGroup : <" + G.name + ">\n  Url : " + gurl)
                            except Exception as error:
                                puy.sendMessage(to, str(error))

                elif msg.text.lower().startswith("urloff to"):
                            number = text.replace("urloff to","")
                            groups = puy.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = puy.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = True
                                    puy.updateGroup(G)
                                except:
                                    G.preventedJoinByTicket = True
                                    puy.updateGroup(G)
                                puy.sendMessage(to, "Closing Qr\nInGroup : <" + G.name + ">")
                            except Exception as error:
                                puy.sendMessage(to, str(error))

                elif msg.text.lower().startswith("crash to"):
                            number = text.replace("crash to","")
                            groups = puy.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = puy.getGroup(group)
                                try:
                                    puy.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                except:
                                    puy.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                puy.sendMessage(to, "Send Crash To Group : " + G.name)
                            except Exception as error:
                                puy.sendMessage(to, str(error))

                elif msg.text.lower().startswith("leave to"):
                            number = text.replace("leave to","")
                            groups = puy.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = puy.getGroup(group)
                                try:
                                    #puy.sendMessage(to, "Gbye")
                                    puy.leaveGroup(G.id)
                                except:
                                    #puy.sendMessage(to, "Gbye")
                                    puy.leaveGroup(G.id)
                                puy.sendMessage(to, "Leave To Group : " + G.name)
                            except Exception as error:
                                puy.sendMessage(to, str(error))

                elif msg.text.lower().startswith("ginfo to "):
                            number = text.replace("ginfo to ","")
                            groups = puy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = puy.getGroup(group)
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
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "    Group Info\n"
                                ret_ += "\n Nama Group : {}".format(G.name)
                                ret_ += "\n ID Group : \n{}".format(G.id)
                                ret_ += "\n Pembuat Grup : {}".format(gCreator)
                                ret_ += "\n Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n Jumlah Pending : {}".format(gPending)
                                ret_ += "\n Group Qr : {}".format(gQr)
                                ret_ += "\n Group Ticket : {}".format(gTicket)
                                ret_ += "\n\n  Kontak Pembuat dibawah:"
                                puy.sendImageWithURL(to, path)
                                puy.sendMessage(to, str(ret_))
                                puy.sendContact(to, G.creator.mid)
                            except:
                                pass

                elif msg.text.lower().startswith("mention to"):
                            number = text.replace("mention to","")
                            groups = puy.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = puy.getGroup(group)
                                try:
                                    contact = [mem.mid for mem in G.members]
                                    text = "Mentioning To %i Members\n" %len(contact)
                                    no = 1
                                    for mid in contact:
                                        text += "\n{}. @x".format(str(no))
                                        no = (no+1)
                                    text += "\n\nInGroup : {}".format(str(G.name))
                                    sendMessageWithMention(group, text, contact)
                                except:
                                    contact = [mem.mid for mem in G.members]
                                    text = "Mentioning To %i Members\n" %len(contact)
                                    no = 1
                                    for mid in contact:
                                        text += "\n{}. @x".format(str(no))
                                        no = (no+1)
                                    text += "\n\nInGroup : {}".format(str(G.name))
                                    sendMessageWithMention(group, text, contact)
                                puy.sendText(to, "Send Mention To Group : " + G.name)
                            except Exception as error:
                                puy.sendMessage(to, str(error))

                elif msg.text.lower().startswith("memlist to"):
                            number = text.replace("memlist to","")
                            groups = puy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = puy.getGroup(group)
                                no = 0
                                ret_ = " < Member List >\n"
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " + str(no) + ". " + mem.displayName
                                puy.sendMessage(to,"Member in Group : \n"+ str(G.name) + "\n\n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                elif text.lower() == "Grouplist":
                            groups = puy.getGroupIdsJoined()
                            ret_ = "   [ Group List ]"
                            no = 0
                            for gid in groups:
                                group = puy.getGroup(gid)
                                no += 1
                                ret_ += "\n{}. {} = {} Members".format(str(no), str(group.name), str(len(group.members)))
                            ret_ += "\n   [ Total {} Groups ]".format(str(len(groups)))
                            puy.sendMessage(to, str(ret_))

                elif msg.text.lower().startswith("unsendme "):
                    args = text.replace("unsendme ","")
                    mes = 0
                    #try:
                    #    mes = int(args[1])
                    #except:
                    #    mes = 1
                    M = puy.talk.getRecentMessagesV2(to, 999)
                    MId = []
                    for ind,i in enumerate(M):
                        if ind == 0:
                            pass
                        else:
                            if i._from == puy.profile.mid:
                                MId.append(i.id)
                                if len(MId) == mes:
                                    break
                    def unsMes(id):
                        puy.unsendMessage(id)
                    for i in MId:
                        thread1 = threading.Thread(target=unsMes, args=(i,))
                        thread1.start()
                        thread1.join()
                    puy.sendMessage(to, ' 「 Unsend 」\nSukses mengurungkan {} Pesan.'.format(len(MId)))
                    print ("Unsend All Chat")
###################### RANDOM ##########################
                elif text.lower() == "mute":
                 if to not in offbot:
                  contact = puy.getContact(sender)
                  puy.sendMessage(to, "Puy diberhentikan sementara di ruangan {}".format(puy.getGroup(to).name))
                  offbot.append(to)
                  print (to)
                 else:
                  puy.sendMessage(to, "Puy Telah dimatikan di ruangan {}".format(puy.getGroup(to).name))
                  #print ("Muted in {}").format(puy.getGroup(to).name)

                elif text.lower() == "unmute":
                 if to in offbot:
                  offbot.remove(to)
                  contact = puy.getContact(sender)
                  puy.sendMessage(to, "Puy dihidupkan kembali di ruangan {}".format(puy.getGroup(to).name))
                  print (to)
                 else:
                  puy.sendMessage(to, "Puy Telah dihidupkan di ruangan {}".format(puy.getGroup(to).name))
                  #print ("UnMuted in {}").format(puy.getGroup(to).name)
                if to in offbot:
                 return

                elif text.lower() == 'speed':
                    start = time.time()
                    puy.sendMessage("u1916721a836d0e456c291abb7ed4a499", ' ') #.format(str(contact.displayName))
                    elapsed_time = time.time() - start
                    puy.sendMessage(to,format(str(elapsed_time)))
                    #print (to,"Speed sender in group {}").format(puy.getGroup(to).name)
                elif text.lower() == 'rerun':
                    puy.sendMessage(to, "Memulai ulang bot...")
                    time.sleep(0.5)
                    puy.sendMessage(to, "Berhasil Memulai ulang bot.")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    puy.sendMessage(to, "{}".format(str(runtime)))
                elif text.lower() == 'puylist':
                    try:
                        arr = []
                        owner = "u1916721a836d0e456c291abb7ed4a499"
                        creator = puy.getContact(owner)
                        contact = puy.getContact(puyMID)
                        grouplist = puy.getGroupIdsJoined()
                        contactlist = puy.getAllContactIds()
                        blockedlist = puy.getBlockedContactIds()
                        #ret_ = ""
                        #ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ = "Jumlah Teman : {}".format(str(len(contactlist)))
                        ret_ += "\nJumlah grup : {}".format(str(len(grouplist)))
                        ret_ += "\nJumlah akun terblokir : {}".format(str(len(blockedlist)))
                        #ret_ += "\n{}".format(creator.displayName)
                        #ret_ += "\n p̢͎ͣ̕u̢̩̫͟y̮̯ͬ͜"
                        puy.sendMessage(to, str(ret_))
                    except Exception as e:
                        puy.sendMessage(msg.to, str(e))
#### STEAL PROFILE ####
                elif msg.text.lower().startswith("psteal 1 "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + puy.getContact(ls).pictureStatus
                            puy.sendImageWithURL(to, str(path))

                elif msg.text.lower().startswith("psteal 2 "):
                    try:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                          names = re.findall(r'@(\w+)', text)
                          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                          mentionees = mention['MENTIONEES']
                          lists = []
                          for mention in mentionees:
                              if mention["M"] not in lists:
                                  lists.append(mention["M"])
                          for ls in lists:
                              contact = puy.getContact(ls)
                              puy.sendMessage(to, "   「 ProfileSteal 」\nStatus Message:\n" + contact.statusMessage)
                    except:
                          puy.sendMessage(to, "Status kosong")

                elif msg.text.lower().startswith("psteal 3 "):
                    #if msg._from in admin:
                        #if line != None:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = puy.getProfileCoverURL(ls)
                                    puy.sendImageWithURL(to, str(path))
                elif msg.text.lower().startswith("psteal 4 "):
                    #if msg._from in admin:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                try:
                                    contact = puy.getContact(target)
                                    path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                    puy.sendVideoWithURL(to, path)
                                except Exception as e:
                                    pass

                elif msg.text.lower().startswith("psteal 5 "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "   「 ProfileSteal 」"
                        for ls in lists:
                            contact = puy.getContact(ls)
                            #ret_ += "\nMid:\n{}".format(str(ls))
                            ret_ += "\n{} Mid:".format(contact.displayName) + "\n{}".format(str(ls))
                        puy.sendMessage(to, str(ret_))
                        #puy.sendContact(to, contact.mid)

                elif msg.text.lower().startswith("psteal 6 "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "   「 ProfileSteal 」"
                        for ls in lists:
                            contact = puy.getContact(ls)
                            #ret_ += "\nMid:\n{}".format(str(ls))
                            ret_ += "\nDisplay Name : {}".format(contact.displayName)
                        puy.sendMessage(to, str(ret_))
                        puy.sendContact(to, contact.mid)
### STEAL PROFILE ###

### GROUP PROFILE ###
                elif msg.text.lower().startswith("gsteal 1"):
                                group = puy.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(group.id)))
                                cuki = "Below"
                                #cuki += "Group Name : {}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                #cuki += "\nGroup Creator : {}".format(str(gCreator))
                                #cuki += "\nMembers : {}".format(str(len(group.members)))
                                #cuki += "\nPendings Member : {}".format(gPending)
                                #cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                #cuki += "\nGroup Qr : {}".format(gQr)
                                #puy.sendMessage(to, str(cuki))
                                puy.sendImageWithURL(to, path)

                elif msg.text.lower().startswith("gsteal 2"):
                                group = puy.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(group.id)))
                                cuki = ""
                                cuki += "「Grup Steal」\nNama Grup:\n{}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                #cuki += "\nGroup Creator : {}".format(str(gCreator))
                                #cuki += "\nMembers : {}".format(str(len(group.members)))
                                #cuki += "\nPendings Member : {}".format(gPending)
                                #cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                #cuki += "\nGroup Qr : {}".format(gQr)
                                puy.sendMessage(to, str(cuki))

                elif msg.text.lower().startswith("gsteal 3"):
                                group = puy.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(group.id)))
                                cuki = ""
                                #cuki += "Nama Grup: {}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                cuki += "「Grup Steal」\nPembuat Grup:\n{}\n  Kontaknya:".format(str(gCreator))
                                #cuki += "\nMembers : {}".format(str(len(group.members)))
                                #cuki += "\nPendings Member : {}".format(gPending)
                                #cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                #cuki += "\nGroup Qr : {}".format(gQr)
                                puy.sendMessage(to, str(cuki))
                                puy.sendContact(to, group.creator.mid)

                elif msg.text.lower().startswith("gsteal 4"):
                                group = puy.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(group.id)))
                                cuki = ""
                                cuki += "「Grup Steal」\nAnggota:\n{}".format(str(len(group.members)))
                                puy.sendMessage(to, str(cuki))

                elif msg.text.lower().startswith("gsteal 5"):
                          #if user in PuySekawan or user in PUYWAIT["Admin"]:
                            if msg.toType == 2:
                                grup = puy.getGroup(to)
                                if grup.preventedJoinByTicket == True:
                                   grup.preventedJoinByTicket == False
                                   puy.updateGroup(grup)
                                set = puy.reissueGroupTicket(to)
                                puy.sendMessage(to, "「Grup Steal」\nGrup Url:\nhttps://line.me/R/ti/g/{}".format(str(set)))
                            #else:
                            #    puy.sendMessage(to, "Tertutup :(")

                elif msg.text.lower().startswith("gsteal 6"):
                            gid = puy.getGroup(to)
                            puy.sendMessage(to, "「Grup Steal」\nID Group:\n" + gid.id)
### GROUP PROFILE ###
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        ret_ += "\n╚══[ Status ]"
                        puy.sendMessage(to, str(ret_))
                    except Exception as e:
                        puy.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    puy.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    puy.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    puy.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    puy.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    puy.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autojoin off':
                    settings["autoLeave"] = False
                    puy.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    puy.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    puy.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    puy.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    puy.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    puy.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    puy.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'puyonecontact':
                    settings["copy"] = True
                    puy.sendMessage(to, "to Contact Yang Mau Di Copy")
#==============================================================================#
                elif text.lower() == 'me':
                    sendMessageWithMention(to, puyMID)
                    puy.sendContact(to, puyMID)
                elif text.lower() == 'mymid':
                    puy.sendMessage(msg.to,"[MID]\n" +  puyMID)
                elif text.lower() == 'myname':
                    me = puy.getContact(puyMID)
                    puy.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = puy.getContact(puyMID)
                    puy.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = puy.getContact(puyMID)
                    puy.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = puy.getContact(puyMID)
                    puy.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = puy.getContact(puyMID)
                    cover = puy.getProfileCoverURL(puyMID)    
                    puy.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = puy.getContact(ls)
                            mi_d = contact.mid
                            puy.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        puy.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = puy.getContact(ls)
                            puy.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = puy.getContact(ls)
                            puy.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.puy.naver.jp/" + puy.getContact(ls).pictureStatus
                            puy.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.puy.naver.jp/" + puy.getContact(ls).pictureStatus + "/vp"
                            puy.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
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
                                path = puy.getProfileCoverURL(ls)
                                puy.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("puyoneprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            puy.puyoneContactProfile(contact)
                            puy.sendMessage(msg.to, "Berhasil puyone member tunggu beberapa saat sampai profile berubah")
                        except:
                            puy.sendMessage(msg.to, "Gagal puyone member")
                            
                elif text.lower() == 'restoreprofile':
                    try:
                        puyProfile.displayName = str(myProfile["displayName"])
                        puyProfile.statusMessage = str(myProfile["statusMessage"])
                        puyProfile.pictureStatus = str(myProfile["pictureStatus"])
                        puy.updateProfileAttribute(8, puyProfile.pictureStatus)
                        puy.updateProfile(puyProfile)
                        puy.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        puy.sendMessage(msg.to, "Gagal restore profile")
                        
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            puy.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            puy.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            puy.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            puy.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimipuyist':
                    if settings["mimic"]["target"] == {}:
                        puy.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+puy.getContact(mi_d).displayName
                        puy.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            puy.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            puy.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = puy.getGroup(to)
                    GS = group.creator.mid
                    puy.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = puy.getGroup(to)
                    puy.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = puy.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    puy.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = puy.getGroup(to)
                    puy.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = puy.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = puy.reissueGroupTicket(to)
                            puy.sendMessage(to, "[ Group Ticket ]\nhttps://puy.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            puy.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'groupticket on':
                    if msg.toType == 2:
                        group = puy.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            puy.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            puy.updateGroup(group)
                            puy.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'groupticket off':
                    if msg.toType == 2:
                        group = puy.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            puy.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            puy.updateGroup(group)
                            puy.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = puy.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://puy.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    puy.sendMessage(to, str(ret_))
                    puy.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = puy.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        puy.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = puy.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = puy.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        puy.sendMessage(to, str(ret_))
#==============================================================================#          
                elif text.lower() == 'mentionall':
                    group = puy.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        puy.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        #puy.sendMessage(to, "Total {} Mention".format(str(len(nama))))
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                puy.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            puy.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        puy.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        puy.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        puy.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        puy.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            puy.sendMessage(receiver,"None")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = puy.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n"#+ readTime
                        try:
                            puy.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        puy.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
#==============================================================================# 
#==============================================================================#  
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        puy.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    puy.sendMessage(to, str(ret_))
                elif "instagraminfo" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            puy.sendImageWithURL(to, str(path))
                            puy.sendMessage(to, str(ret_))
                        except:
                            puy.sendMessage(to, "Pengguna tidak ditemukan")
                elif "instagrampost" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1, 999):
                            print('PAGE: ', count)
                            r = x.get(profile, params={'max_id': end_cursor})
                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)
                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                if node['is_video']:
                                    page = 'https://www.instagram.com/p/' + node['code']
                                    r = x.get(page)
                                    url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                    print(url)
                                    puy.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    puy.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                elif "searchimage" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            puy.sendImageWithURL(to, str(path))
                elif "searchyoutube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        puy.sendMessage(to, str(ret_))
                elif "searchmusic" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ reading Audio ]"
                                puy.sendMessage(to, str(ret_))
                                puy.sendAudioWithURL(to, song[3])
                        except:
                            puy.sendMessage(to, "Musik tidak ditemukan")
                elif "searchlyric" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                puy.sendMessage(to, str(ret_))
                        except:
                            puy.sendMessage(to, "Lirik tidak ditemukan")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    puy.sendMessage(to, str(ret_))
#==============================================================================#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != puy.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    puy.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        puy.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in puyMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if puyMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = puy.getContact(sender)
                                    puy.sendMessage(to, "ha")
                                    sendMessageWithMention(to, contact.mid)
                                break
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
