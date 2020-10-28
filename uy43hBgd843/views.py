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
        return render(request,"userbase.html",{'curl':curl,'cumn':request.COOKIES.get('cunm'),'name':name})
    else:	
            cun=request.COOKIES.get('cunm')
            field=request.POST.get('field')
            value=request.POST.get('value')	
            query="update facultydb set %s='%s' where email='%s' " %(field,value,cun)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'userbase.html',{'curl':curl,'output':'Changed Successfully'})

def leave(request):
    if (request.method=="GET"):
            return render(request,'uleave.html',{'curl':curl,'output':''})
    else:	
            cunm=request.COOKIES.get('cunm')
            reason=request.POST.get('reason')
            fdate=request.POST.get('fdate')
            tdate=request.POST.get('tdate')
            dt=time.asctime(time.localtime(time.time()))
            query1="update facultydb set leaveapp='yes' where email='%s' " %(cunm)
            models.cursor.execute(query1)
            models.db.commit()
            query=" select * from facultydb where email='%s' " %(cunm)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            name=userDetails[0][1]
            me= "burhanuddinbootwala6864@gmail.com"
            you = cunm
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Medi-FRMCampus"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                            <head></head>
                                <body>
                                    <h1>Welcome to Medicaps University</h1>
                                    <h2>Your leave application has been Registered. Wait for the Manager To review your application. </h2>
                                    <h2>Date: """+dt+"""</h2>
                                    <h2>Name: """+userDetails[0][1]+"""</h2>
                                    <h2>Reason: """+reason+"""</h2>
                                    <h2>From: """+fdate+"""</h2>
                                    <h2>To: """+tdate+"""</h2>

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
            me = "burhanuddinbootwala6864@gmail.com"
            you = "en18cs301071@medicaps.ac.in"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Medi-FRMCampus"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Welcome to Medicaps University</h1>
                                    <h2>Following Leave Application Is Registered.</h2>
                                    <h2>Date: """+dt+"""</h2>
                                    <h2>Name: """+userDetails[0][1]+"""</h2>
                                    <h2>Email: """+userDetails[0][3]+"""</h2>
                                    <h2>Reason: """+reason+"""</h2>
                                    <h2>From: """+fdate+"""</h2>
                                    <h2>To: """+tdate+"""</h2>

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
                
            
            return render(request,'uleave.html',{'curl':curl,'output':'Mail Sent Successfully'})
    


def attendance(request):
    cunm=request.COOKIES.get('cunm')
    query=" select * from facultydb where email='%s' " %(cunm)
    models.cursor.execute(query)
    userDetails=models.cursor.fetchall()
    name=userDetails[0][1]
    tday=userDetails[0][10]
    mday=userDetails[0][9]
    per=(mday/tday)*100
    return render(request,'uattendance.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'name':name,'tday':tday,'mday':mday,'per':per})

def salary(request):
    cunm=request.COOKIES.get('cunm')
    query=" select * from facultydb where email='%s' " %(cunm)
    models.cursor.execute(query)
    userDetails=models.cursor.fetchall()
    sal=userDetails[0][12]
    ctc=float((sal*0.1))
    salnew=float((sal+ctc))
    pt=float((salnew*0.363)/100)
    erf=float((salnew*3.27)/100)
    ei=float((salnew*0.45)/100)
    net=float(salnew-(pt+(2*erf)+ei))
    return render(request,'usalary.html',{'curl':curl,'net':net,'ei':ei,'sal':sal,'ctc':ctc,'pt':pt,'erf':erf})

def uchange(request):
    if (request.method=="GET"):
            return render(request,'upass.html',{'curl':curl,'output':''})
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
            
                return render(request,'upass.html',{'curl':curl,'output':'Changed Successfully'})
            else:
                return render(request,'upass.html',{'curl':curl,'output':'Exisiting Password Is Invalid'})
        
def addinfo(request):
    return render(request,'addinfo.html',{'curl':curl})

def academic(request):
    if (request.method=="GET"):
            return render(request,'academic.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            exm=request.POST.get('exm')
            year=request.POST.get('year')
            board=request.POST.get('board')
            mark=request.POST.get('marks')
            pri=request.POST.get('pri')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbacademic values(%s,'%s','%s','%s','%s','%s')" %(regid,exm,year,board,mark,pri)
            models.cursor.execute(query)
            models.db.commit()
        
            return render(request,'academic.html',{'curl':curl,'output':'Added Successfully'})
           

def workexp(request):
    if (request.method=="GET"):
            return render(request,'workexp.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            s1=request.POST.get('s1')
            s2=request.POST.get('s2')
            s3=request.POST.get('s3')
            val=request.POST.get('val')
            
            	
            regid=userDetails[0][0]
            if val=='add':
                query="insert into facultydbwe values(%s,'%s','%s','%s')" %(regid,s1,s2,s3)
                models.cursor.execute(query)
                models.db.commit()
                return render(request,'workexp.html',{'curl':curl,'output':'Added Successfully'})
            else:
                query="update facultydbwe set industry='%s' where regid='%s' " %(regid,s1)
                models.cursor.execute(query)
                models.db.commit()
                query="update facultydbwe set academic='%s' where regid='%s' " %(regid,s2)
                models.cursor.execute(query)
                models.db.commit()
                query="update facultydbwe set research='%s' where regid='%s' " %(regid,s3)
                models.cursor.execute(query)
                models.db.commit()
                return render(request,'workexp.html',{'curl':curl,'output':'Updated Successfully'})
            



def workshopa(request):
    return render(request,'workshopa.html',{'curl':curl})

def workshopaw(request):
    if (request.method=="GET"):
            return render(request,'workshopaw.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            s1=request.POST.get('s1')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbworkshopa values(%s,'Workshop','%s')" %(regid,s1)
            models.cursor.execute(query)
            models.db.commit()
            
        
            return render(request,'workshopaw.html',{'curl':curl,'output':'Added Successfully'})
   

def workshopac(request):
    if (request.method=="GET"):
            return render(request,'workshopac.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            s1=request.POST.get('s1')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbworkshopa values(%s,'Conference','%s')" %(regid,s1)
            models.cursor.execute(query)
            models.db.commit()
            
        
            return render(request,'workshopac.html',{'curl':curl,'output':'Added Successfully'})
    

def workshopaf(request):
    if (request.method=="GET"):
            return render(request,'workshopaf.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            s1=request.POST.get('s1')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbworkshopa values(%s,'Faculty Development Program','%s')" %(regid,s1)
            models.cursor.execute(query)
            models.db.commit()
            
        
            return render(request,'workshopaf.html',{'curl':curl,'output':'Added Successfully'})


def workshopo(request):
    if (request.method=="GET"):
            return render(request,'workshopo.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            s1=request.POST.get('s1')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbworkshopo values(%s,'%s')" %(regid,s1)
            models.cursor.execute(query)
            models.db.commit()
            
        
            return render(request,'workshopo.html',{'curl':curl,'output':'Added Successfully'})
    



def achievements(request):
    if (request.method=="GET"):
            return render(request,'achievements.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            ach=request.POST.get('ach')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbach values(%s,'%s')" %(regid,ach)
            models.cursor.execute(query)
            models.db.commit()
        
            return render(request,'achievements.html',{'curl':curl,'output':'Added Successfully'})
           


def certifications(request):
    if (request.method=="GET"):
            return render(request,'certifications.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            cert=request.POST.get('cert')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbcert values(%s,'%s')" %(regid,cert)
            models.cursor.execute(query)
            models.db.commit()
        
            return render(request,'certifications.html',{'curl':curl,'output':'Added Successfully'})
        
def strengths(request):
    if (request.method=="GET"):
            return render(request,'strengths.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            s1=request.POST.get('s1')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbstrengths values(%s,'%s')" %(regid,s1)
            models.cursor.execute(query)
            models.db.commit()
            
        
            return render(request,'strengths.html',{'curl':curl,'output':'Added Successfully'})



def weakness(request):
    if (request.method=="GET"):
            return render(request,'weakness.html',{'curl':curl,'output':''})
    else:	
            
            cun=request.COOKIES.get('cunm')
            query=" select * from facultydb where email='%s' " %(cun)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            s1=request.POST.get('s1')
            	
            regid=userDetails[0][0]
                
            query="insert into facultydbweakness values(%s,'%s')" %(regid,s1)
            models.cursor.execute(query)
            models.db.commit()
            
        
            return render(request,'weakness.html',{'curl':curl,'output':'Added Successfully'})


