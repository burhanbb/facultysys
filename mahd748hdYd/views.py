from django.shortcuts import render
from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from . import models
import time
from django.core.mail import send_mail
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL
# Create your views here.
def home(request):
    if (request.method=="GET"):
        cunm=request.COOKIES.get('cunm')
        query=" select * from facultydb where email='%s' " %(cunm)
        models.cursor.execute(query)
        userDetails=models.cursor.fetchall()
        name=userDetails[0][1]
        return render(request,"managebase.html",{'curl':curl,'cumn':request.COOKIES.get('cunm'),'name':name})
    else:	
            cun=request.COOKIES.get('cunm')
            field=request.POST.get('field')
            value=request.POST.get('value')	
            query="update facultydb set %s='%s' where email='%s' " %(field,value,cun)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'managebase.html',{'curl':curl,'output':'Changed Successfully'})
def applicants(request):
    query1="select * from facultydb where leaveapp='yes' "
    models.cursor.execute(query1)
    splist=models.cursor.fetchall()
    return render(request,'mlapplicants.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'splist':splist})

def approval(request):
    if (request.method=="GET"):
            return render(request,'mlapproval.html',{'curl':curl,'output':''})
    else:	
            cunm=request.COOKIES.get('cunm')
            field=request.POST.get('field')
            email=request.POST.get('email')
            reason=request.POST.get('reason')
            dt=time.asctime(time.localtime(time.time()))
            query1="select * from facultydb where email='%s' " %(email)
            models.cursor.execute(query1)
            userDetails=models.cursor.fetchall()
            query="select * from facultydb where email='%s' " %(cunm)
            models.cursor.execute(query)
            userDetails1=models.cursor.fetchall()
            if field=='yes':
                
                me = "burhanuddinbootwala6864@gmail.com"
                you = email
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Medi-FRMCampus"
                msg['From'] = me
                msg['To'] = you
                html = """<html>
                            <head></head>
                                <body>
                                    <h1>Welcome to Medicaps University</h1>
                                    <h2>Your leave application has been accepted by manager """ +userDetails1[0][1]+"""</h2>
                                    <h2>Date: """+dt+"""</h2>

                                </body>
                            </html>
                        """
                s = smtplib.SMTP('smtp.gmail.com', 587) 
                s.starttls() 
                s.login("burhanuddinbootwala6864@gmail.com", "xmydoicztftnanvc") 

                part2 = MIMEText(html, 'html')

                msg.attach(part2)

                s.sendmail(me,you, str(msg)) 
                s.quit()
                print("mail send successfully....")
            else:
                me = "burhanuddinbootwala6864@gmail.com"
                you = email
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Medi-FRMCampus"
                msg['From'] = me
                msg['To'] = you
                html = """<html>
                            <head></head>
                                <body>
                                    <h1>Welcome to Medicaps University</h1>
                                    <h2>Sorry, Your leave application is declined by manager """+userDetails1[0][1]+"""</h2>
                                    <h2>Date: """+dt+"""</h2>
                                    <h2>Reason: """+reason+"""</h2>

                                </body>
                            </html>
                        """
                s = smtplib.SMTP('smtp.gmail.com', 587) 
                s.starttls() 
                s.login("burhanuddinbootwala6864@gmail.com", "xmydoicztftnanvc") 

                part2 = MIMEText(html, 'html')

                msg.attach(part2)

                s.sendmail(me,you, str(msg)) 
                s.quit()
                print("mail send successfully....")
                
            
            return render(request,'mlapproval.html',{'curl':curl,'output':'Mail Sent Successfully'})
    

def attendance(request):
    if (request.method=="GET"):
            return render(request,'mlattendance.html',{'curl':curl,'output':''})
    else:	
            
            
            email=request.POST.get('email')
            field=request.POST.get('days')
            value=request.POST.get('myattend')	
            query="update facultydb set myattend='%s' where email='%s' " %(value,email)
            models.cursor.execute(query)
            models.db.commit()
            query1="update facultydb set totalattend='%s' where email='%s' " %(field,email)
            models.cursor.execute(query1)
            models.db.commit()
            
            return render(request,'mlattendance.html',{'curl':curl,'output':'Uploaded Successfully'})
        
def mstatus(request):
    if (request.method=="GET"):
            return render(request,'mstatus.html',{'curl':curl,'output':''})
    else:	
            
            
            email=request.POST.get('email')
            days=request.POST.get('days')
            
            query="select * from facultydb where email='%s' " %(email)
            models.cursor.execute(query)
            user=models.cursor.fetchall()
            query1="update facultydbjoin set daterel='%s' where regid='%s' " %(days,user[0][0])
            models.cursor.execute(query1)
            models.db.commit()
            query1="update facultydbjoin set status='Not Active' where regid='%s' " %(user[0][0])
            models.cursor.execute(query1)
            models.db.commit()
            
            return render(request,'mstatus.html',{'curl':curl,'output':'Changed Successfully'})
        
    

def mchange(request):
    if (request.method=="GET"):
            return render(request,'mpass.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            field=request.POST.get('field')
            value=request.POST.get('value')	
            if field==userDetails[0][4]:
                
                query="update facultydb set password='%s' where email='%s' " %(value,cun)
                models.cursor.execute(query)
                models.db.commit()
            
                return render(request,'mpass.html',{'curl':curl,'output':'Changed Successfully'})
            else:
                return render(request,'mpass.html',{'curl':curl,'output':'Exisiting Password Is Invalid'})
        

def search(request):
    if (request.method=="GET"):
        return render(request,'search.html',{'curl':curl,'output':''})
    else:	
            
            
        value=request.POST.get('value')
        choice=request.POST.get('field')
        
        
        if choice=="First Name":
            try:
                query="select regid from facultydb where first_name='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
            
        elif choice=='Last Name':
            try:
                query="select regid from facultydb where second_name='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
            
        elif choice=="Gender":
            try:
                query="select regid from facultydb where gender='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Email":
            try:
                query="select regid from facultydb where email='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Attendance %(>)":
            try:
                query="select regid,(myattend/totalattend) from facultydb" 
                models.cursor.execute(query)
                userD=models.cursor.fetchall()
                val=int(value)
                per=val/100
                user=list()
                for s in userD:
                    p=int(s[1])
                    if p>per:
                        user.append(s[0])
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                 return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
             
        elif choice=="Attendance %(<)":
            try:
                query="select regid,(myattend/totalattend) from facultydb" 
                models.cursor.execute(query)
                userD=models.cursor.fetchall()
                val=int(value)
                per=val/100
                user=list()
                for s in userD:
                    p=int(s[1])
                    if p<per:
                        user.append(s[0])
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                 return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
             
        elif choice=="Salary(<)":
            try:
                query="select regid,salary from facultydb" 
                models.cursor.execute(query)
                userD=models.cursor.fetchall()
                sal=int(value)
                user=list()
                for s in userD:
                    p=int(s[1])
                    if p<sal:
                        user.append(s[0])
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                 return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Salary(>)":
            try:
                query="select regid,salary from facultydb" 
                models.cursor.execute(query)
                userD=models.cursor.fetchall()
                sal=int(value)
                user=list()
                for s in userD:
                    p=int(s[1])
                    if p>sal:
                        user.append(s[0])
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                 return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Industry Experience":
            try:
                query="select regid from facultydbwe where industry='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Research Experience":
            try:
                query="select regid from facultydbwe where research='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Academic Experience":
            try:
                query="select regid from facultydbwe where academic='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
            
        elif choice=="Department Name":
            try:
                query="select regid from facultydbdept where deptname='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Date Of Birth(Year)":
            try:
                query="select regid from facultydbdob where year='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Year Of Joining":
            try:
                query="select regid from facultydbjoin where datejoin='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Year Of Relieving":
            try:
                query="select regid from facultydbjoin where daterel='%s' " %(value)
                models.cursor.execute(query)
                user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        elif choice=="Status(Active/Not Active)":
            try:
                if value=="Active":
                    
                    query="select regid from facultydbjoin where status='Active'"
                    models.cursor.execute(query)
                    user=models.cursor.fetchall()
                else:
                    query="select regid from facultydbjoin where status='Not Active'"
                    models.cursor.execute(query)
                    user=models.cursor.fetchall()
                dlist=[]
                for regid in user:
                    details={}
                    query="select * from facultydb where regid='%s'"%(regid)
                    models.cursor.execute(query)
                    user1=models.cursor.fetchall()
                    if user1[0][8]=='user':
                        details["first"]=user1[0][1]
                        details["second"]=user1[0][2]
                        details["email"]=user1[0][3]
                        details["mobile"]=user1[0][5]
                        details["address"]=user1[0][6]
                        details["gender"]=user1[0][7]
                        per=(user1[0][9]/user1[0][10])*100
                        details["per"]=per
                        details["leave"]=user1[0][11]
                        details["salary"]=user1[0][12]
                        query="select deptname from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept1=models.cursor.fetchall()
                        deptn=str(dept1).strip("(',)")
                        details["deptn"]=deptn
                        query="select deptid from facultydbdept where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dept2=models.cursor.fetchall()
                        depti=str(dept2).strip("(',)")
                        details["deptid"]=depti
                        query="select industry from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we1=models.cursor.fetchall()
                        wei=str(we1).strip("(',)")
                        details["industry"]=wei
                        query="select academic from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we2=models.cursor.fetchall()
                        wea=str(we2).strip("(',)")
                        details["academic"]=wea
                        query="select research from facultydbwe where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        we3=models.cursor.fetchall()
                        wer=str(we3).strip("(',)")
                        details["research"]=wer
                        query="select * from facultydbacademic where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ac=models.cursor.fetchall()
                        details["ac"]=ac
                        query="select details from facultydbach where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        ach=models.cursor.fetchall()
                        details["ach"]=ach
                        query="select details from facultydbweakness where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        w=models.cursor.fetchall()
                        details["weakness"]=w
                        query="select details from facultydbstrengths where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        s=models.cursor.fetchall()
                        details["stre"]=s
                        query="select * from facultydbdob where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        dob=models.cursor.fetchall()
                        details["dob"]=dob
                        query="select details from facultydbcert where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        cert=models.cursor.fetchall()
                        details["cert"]=cert
                        query="select * from facultydbworkshopa where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        work=models.cursor.fetchall()
                        details["workshopa"]=work
                        query="select details from facultydbworkshopo where regid='%s'"%(regid)
                        models.cursor.execute(query)
                        worko=models.cursor.fetchall()
                        details["workshopo"]=worko
                        dlist.append(details)
                return render(request,'search.html',{'curl':curl,'dlist':dlist,'output':'Results Are Shown Below!'})
            except:
                return render(request,'search.html',{'curl':curl,'out':'No Results Found!'})
        
             
            
                
                
        #query="update facultydb set myattend='%s' where email='%s' " %(value,email)
        #models.cursor.execute(query)
        #models.db.commit()
        #query1="update facultydb set totalattend='%s' where email='%s' " %(field,email)
        #models.cursor.execute(query1)
        #models.db.commit()
        
        #return render(request,'search.html',{'curl':curl,'output':'Uploaded Successfully'})