from select import select
from unittest import result
from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
import string
import secrets
from django.db.models import Q
# Create your views here.
from django.contrib import messages 
from django.contrib.messages.api import error
def index(request):
    if 'unid' in request.session:
        unid = request.session['unid']
        if admininfo.objects.filter(email=unid):
            scount=studentinfo.objects.all().count()
            tcount=teacherinfo.objects.all().count()
            cevent=eventgoing.objects.get(tempid="1")
            techerstable=teacherinfo.objects.all()
            studentstable=studentinfo.objects.all()
            return render(request,"adminpage.html",{'scount':scount,'tcount':tcount,'cevent':cevent,'techerstable':techerstable,'studentstable':studentstable})
        elif eventgoing.objects.filter(tempid="1")[0].event=="OFF":
            return render(request,"noevent.html")
        elif teacherinfo.objects.filter(tid=unid):

                  teacher=teacherinfo.objects.get(tid=unid)
                  eventslist=studentevent.objects.filter(event=teacher.mangingfevent)
                  return render(request,"teacherpage.html",{'teacher':teacher,'eventslist':eventslist})
        elif studentinfo.objects.filter(Admissionno=unid):
                  val=studentevent.objects.filter(email=request.session['unid'])
                  return render(request,"studentpage.html",{'displaydata':val})
 
    ranklist=studentevent.objects.filter(Q(grade="A") |  Q(grade="B") | Q(grade="C")).order_by('grade')
    return render(request,"index.html",{'ranklist':ranklist,'cevent':eventgoing.objects.filter(tempid="1")[0],'resultlist':resultpublic.objects.filter(tempid="1")[0]})


def stlogin(request):
    return render(request,"Studentlog.html")


def techlogin(request):
    return render(request,"teacherlog.html")

def about(request):
    return render(request,"about.html")

def team(request):
    return render(request,"info.html")



def tlogincheck(request):
    if 'unid' in request.session:

        unid = request.session['unid']
        print(unid)
        if admininfo.objects.filter(email=unid):
            scount=studentinfo.objects.all().count()
            tcount=teacherinfo.objects.all().count()
            cevent=eventgoing.objects.get(tempid="1")
            techerstable=teacherinfo.objects.all()
            studentstable=studentinfo.objects.all()
            return render(request,"adminpage.html",{'scount':scount,'tcount':tcount,'cevent':cevent,'techerstable':techerstable,'studentstable':studentstable})
        elif eventgoing.objects.filter(tempid="1")[0].event=="OFF":
            return render(request,"noevent.html")
        elif teacherinfo.objects.filter(tid=unid):
                  teacher=teacherinfo.objects.get(tid=unid)
                  eventslist=studentevent.objects.filter(event=teacher.mangingfevent)
                  return render(request,"teacherpage.html",{'teacher':teacher,'eventslist':eventslist})
        elif studentinfo.objects.filter(Admissionno=unid):
                  val=studentevent.objects.filter(email=request.session['unid'])
                  return render(request,"studentpage.html",{'displaydata':val})
    if request.method == "POST":
        uname = request.POST.get('idno')
        pwd = request.POST.get('pwd')
        print(uname,pwd)
        if admininfo.objects.filter(email=uname, password=pwd).exists():
            request.session['unid'] = uname
            scount=studentinfo.objects.all().count()
            tcount=teacherinfo.objects.all().count()
            cevent=eventgoing.objects.get(tempid="1")
            techerstable=teacherinfo.objects.all()
            studentstable=studentinfo.objects.all()
            return render(request,"adminpage.html",{'scount':scount,'tcount':tcount,'cevent':cevent,'techerstable':techerstable,'studentstable':studentstable})
        elif teacherinfo.objects.filter(tid=uname, password=pwd).exists():
            
            if eventgoing.objects.filter(tempid="1")[0].event=="OFF":
              return render(request,"noevent.html")
            request.session['unid'] = uname
            teacher=teacherinfo.objects.get(tid=uname)
            eventslist=studentevent.objects.filter(event=teacher.mangingfevent)
            return render(request,"teacherpage.html",{'teacher':teacher,'eventslist':eventslist})
        else:
            return render(request, "teacherlog.html")

def slogincheck(request):
    if 'unid' in request.session:
        unid = request.session['unid']
        print(unid)
        if admininfo.objects.filter(email=unid):
            return render(request,"adminpage.html")
        elif teacherinfo.objects.filter(tid=unid):
                  if eventgoing.objects.filter(tempid="1").event=="OFF":
                    return render(request,"noevent.html")
                  teacher=teacherinfo.objects.get(tid=unid)
                  eventslist=studentevent.objects.filter(event=teacher.mangingfevent)
                  return render(request,"teacherpage.html",{'teacher':teacher,'eventslist':eventslist})
        elif studentinfo.objects.filter(Admissionno=unid):
                  if eventgoing.objects.filter(tempid="1")[0].event=="OFF":
                    return render(request,"noevent.html")
                  val=studentevent.objects.filter(email=request.session['unid'])
                  return render(request,"studentpage.html",{'displaydata':val})
    if request.method == "POST":
        adno = request.POST.get('adno')
        pwd = request.POST.get('pwd')
        print(adno,pwd)
        if studentinfo.objects.filter(Admissionno=adno, password=pwd).exists():
            if eventgoing.objects.filter(tempid="1")[0].event=="OFF":
                    return render(request,"noevent.html")
            request.session['unid'] = adno
            val=studentevent.objects.filter(email=request.session['unid'])
            return render(request,"studentpage.html",{'displaydata':val})
        return render(request, "studentlog.html")

def sregistraion(request):
    if request.method == "POST":
        adno = request.POST.get('adno')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        stclass = request.POST.get('stclass')
        uname=request.POST.get('uname')
        studentinfo.objects.create(Admissionno=adno, password=pwd, email=email, phone=phone, stclass=stclass,username=uname)
        request.session['unid'] = adno
        val=studentevent.objects.filter(email=request.session['unid'])
        if eventgoing.objects.filter(tempid="1")[0].event=="OFF":
            return render(request,"noevent.html")
        return render(request,"studentpage.html",{'displaydata':val})

def tregistration(request):
    if request.method == "POST":
        tid = request.POST.get('idno')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        teacherinfo.objects.create(tid=tid, password=pwd, email=email)
        request.session['unid'] = tid
        if eventgoing.objects.filter(tempid="1")[0].event=="OFF":
            return render(request,"noevent.html")
        return render(request, "teacher.html")

def eventswitchoff(request):
    if admininfo.objects.filter(email=request.session['unid']).exists():
            teacherinfo.objects.filter().all().update(mangingfevent="Not selected")
            eventgoing.objects.filter(tempid="1").update(event="OFF")
            resultpublic.objects.all().update(result="not publish")
            studentevent.objects.all().delete()
            return redirect('/')

def eventswitchsports(request):
    if admininfo.objects.filter(email=request.session['unid']).exists():
            teacherinfo.objects.filter().all().update(mangingfevent="Not selected")
            eventgoing.objects.filter(tempid="1").update(event="Sports")
            studentevent.objects.all().delete()
            resultpublic.objects.all().update(result="not publish")
            return redirect('/')

def eventswitcharts(request):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        teacherinfo.objects.filter().all().update(mangingfevent="Not selected")
        eventgoing.objects.filter(tempid="1").update(event="Arts")
        studentevent.objects.all().delete()
        resultpublic.objects.all().update(result="not publish")
        return redirect('/')

def sdelete(request,adno):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        studentinfo.objects.filter(Admissionno=adno).delete()
        return redirect('/')
def tdelete(request,id):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        teacherinfo.objects.filter(tid=id).delete()
        return redirect('/')

def teacherview(request):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        techerstable=teacherinfo.objects.all()
        ls=eventgoing.objects.filter(tempid="1")
        if ls[0].event=="OFF":
            return render(request,"adminteacherdisaplay.html",{'displaydata':techerstable})
        if  ls[0].event=="Sports":
            sports=event.objects.filter(aors="Sports")
            return render(request,"adminteacherdisaplay.html",{'displaydata':techerstable,'eventlist':sports})
        if  ls[0].event=="Arts":
            Arts=event.objects.filter(aors="Arts")
            return render(request,"adminteacherdisaplay.html",{'displaydata':techerstable,'eventlist':Arts})
        return render(request,"adminteacherdisaplay.html",{'displaydata':techerstable})

def studentview(request):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        studentstable=studentinfo.objects.all()

        return render(request,"adminstudentdisaplay.html",{'displaydata':studentstable})

def Addevent(request):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        eventlist=event.objects.all()
        return render(request,"addevent.html",{'eventlist':eventlist})
def enterresult(request):
    if teacherinfo.objects.filter(tid=request.session['unid']).exists():
        return render(request,"teacherenterresult.html")

def addsports(request):
    eventname = request.POST.get('eventn')
    if admininfo.objects.filter(email=request.session['unid']).exists():
        event.objects.create(aors="Sports",event=eventname)       
        eventlist=event.objects.all()
        return render(request,"addevent.html",{'eventlist':eventlist})

def addarts(request):

    eventname = request.POST.get('eventn')
    if admininfo.objects.filter(email=request.session['unid']).exists():
        event.objects.create(aors="Arts",event=eventname)
        eventlist=event.objects.all()
        return render(request,"addevent.html",{'eventlist':eventlist})

def assignduty(request,ids):
    sevent=request.POST.get('event')
    if admininfo.objects.filter(email=request.session['unid']).exists():
        teacherinfo.objects.filter(tid=ids).update(mangingfevent=sevent) 
        return redirect('/tview')

def eventchoose(request):
    if studentinfo.objects.filter(Admissionno=request.session['unid']).exists():
        eventlist=event.objects.filter(aors=eventgoing.objects.filter(tempid="1")[0].event)
        if studentevent.objects.filter(email=request.session['unid']).count()==3:
            return render(request,"eventchoose.html",{'eventlist':eventlist,'message':"You have already choosen 3 events"})
        return render(request,"eventchoose.html",{'eventlist':eventlist})

def registerevent(request):
    if studentinfo.objects.filter(Admissionno=request.session['unid']).exists():
        eventname=request.POST.get('event')
        if studentevent.objects.filter(email=request.session['unid'],event=eventname).count()==1:
            messages.error(request,"already choosen")
            return redirect('/')
        if studentevent.objects.filter(email=request.session['unid']).exists():
            studentevent.objects.create(email=request.session['unid'],event=eventname,chestno=studentevent.objects.filter(email=request.session['unid'])[0].chestno,name=studentinfo.objects.filter(Admissionno=request.session['unid'])[0].username)
            return redirect('/')
        
        studentevent.objects.create(email=request.session['unid'],event=eventname,chestno=chestno(),name=studentinfo.objects.filter(Admissionno=request.session['unid'])[0].username)
        return redirect('/')

def addresult(request):
    if teacherinfo.objects.filter(tid=request.session['unid']).exists():
        ches=request.POST.get('chesno')
        grade=request.POST.get('grade')
        studentevent.objects.filter(chestno=ches,event=teacherinfo.objects.filter(tid=request.session['unid'])[0].mangingfevent).update(grade=grade)
        return redirect('/enterresult')




def rview(request):
    if studentinfo.objects.filter(Admissionno=request.session['unid']).exists():
        result=resultpublic.objects.get(tempid="1")
        print(result.result)
        val=studentevent.objects.filter(email=request.session['unid'])
        return render(request,"resultview.html",{'resultlist':result,'val':val})
    return redirect('/')

def printit(request,eventname):
    if studentinfo.objects.filter(Admissionno=request.session['unid']).exists():

        val=studentevent.objects.filter(email=request.session['unid'],event=eventname)[0]
        print(val.grade)
        return render(request,"printpage.html",{'val':val})
    return redirect('/')

def resultbublish(request):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        resultpublic.objects.all().update(result="Published")
        return redirect('/')


def rank(request):
        ranklist=studentevent.objects.filter(Q(grade="A") |  Q(grade="B") | Q(grade="C")).order_by('grade')
        print(ranklist)
        return render(request,"rank.html",{'ranklist':ranklist,'cevent':eventgoing.objects.filter(tempid="1")[0],'resultlist':resultpublic.objects.filter(tempid="1")[0]})

def aedelete(request,eventname):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        event.objects.filter(pk=eventname).delete()
        return redirect('/Addevent')
def sedelete(request,eventname):
    if admininfo.objects.filter(email=request.session['unid']).exists():
        event.objects.filter(pk=eventname).delete()
        return redirect('/Addevent')


def logout(request):
    del request.session['unid']
    return redirect('/')

def chestno():
    n=4
    while True:
        cod=''.join(secrets.choice(string.digits) for x in range(n))
        if studentevent.objects.filter(chestno=cod).count() == 0:
            return cod
