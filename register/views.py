from django.shortcuts import render
from .models import details
import psycopg2
from django.contrib import messages
# Create your views here.
def index1(request):
    name  = request.POST.get('name')
    email = request.POST.get('mail')
    title = request.POST.get('title')
    cname = request.POST.get('cname')
    dept  = request.POST.get('dept')
    mailid = check_mail_id()
    temp = 0
    i = len(mailid)
    for j in range(i):
        if (email == mailid[j][0]):
            messages.info(request,"The Mail ID already exist.")
            return render (request,"index.html")
        else:
            temp = temp+1
    if temp == len(mailid):
        user = details(name=name,mail=email,title=title,clgname=cname,dept=dept)
        user.save()
        return render(request,"extend.html")
def index(request):
    return render(request,"index.html")
def check_mail_id():
    conn = psycopg2.connect(database = "sriram", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT mail  from register_details")
    rows = cur.fetchall()
    conn.close()
    return rows
def dindex(request):
    return render(request,"index.html")
def fform1(request):
    return render(request,"fform1.html")
def mform1(request):
    mail = request.POST.get('mail')
    ids = check_mail_id()
    temp = 0
    i = len(ids)
    for j in range(i):
        if (mail == ids[j][0]):
            return render(request,"mform1.html")
        else:
            temp = temp + 1
    if(temp == i):      
        messages.error(request,"kindly check your Mail ID\nThis mail id is ot registered ")
        return render(request,"fform1.html")
