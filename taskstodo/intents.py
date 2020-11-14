name=''
mailto=''
mailcontent=''
from .voice import speak
def get_intent(data):
    global name
    global mailto
    global mailcontent
    m=data['message'].lower()
    if data['key'] =="name":
        name=m
        return "next"
    elif data['key']=="Email-Id":
        mailto=m
        return "content"
    elif data['key']=="content" :
        mailcontent=m
        return "sendemail"
    elif data['key']=="Question":
        return "wikipedia"
    elif any(x in m for x in ["search" , "wikipedia"]):
        return "search"
    elif any(x in m for x in ["send","mail","inform","email"]):
        return "email"
    elif any(x in m for x in ["time","currenttime"]):
        return "time"
    else :
        return "echo"

def handle(data):
    global name
    from flask import render_template
    intent=get_intent(data)
    if intent == "search":
        speak("what do you want to search")
        return render_template('messages/mail.html',
        question={"key":"Question","text":"What do you want to search?"})
    elif intent =="wikipedia":
        from .wikipedia import getdata
        searchdata=getdata(data)
        speak(searchdata)
        return render_template('messages/wikiresult.html',
        searchdata=searchdata,
        question={"key":"task","text":""})
    elif intent == "email":
        speak("Please enter the recipient Email ID")
        return render_template('messages/mail.html',
        question={"key":"Email-Id","text":"Please enter the recipient Email ID"})
    elif intent == "content" :
        speak("Please enter the content that you want to send to the recipient")
        return render_template('messages/mail.html',
        question={"key":"content","text":"Please enter the content that you want to send to the recipient"})
    elif intent == "sendemail" :
        from .mail import sendmailto
        mailmsg = sendmailto(mailto,mailcontent)
        speak(mailmsg)
        return render_template('messages/sendemail.html',
        mailmsg=mailmsg,
        question={"key":"task","text":""})
    elif intent == "next":
        speak("Nice to chat with you"+name+"Please let me know which task you would like to perform")
        return render_template('messages/greet.html',
        name=name,
        question={"key":"task","text":"Please let me know which task you would like to perform"})
    elif intent == "time" :
        from .time import gettime
        timemsg=gettime()
        speak("The current time is "+timemsg)
        return render_template('messages/sendtime.html',
        timemsg="The current time is "+timemsg,
        question={"key":"task","task":""})
    else:
        speak("Sorry I cannot perform this work.Please enter a valid task.")
        return render_template('messages/reply.html',data=data)