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
        return render(request,"adminbase.html",{'curl':curl,'cumn':request.COOKIES.get('cunm'),'name':name})
    else:	
            cun=request.COOKIES.get('cunm')
            field=request.POST.get('field')
            value=request.POST.get('value')	
            query="update facultydb set %s='%s' where email='%s' " %(field,value,cun)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'adminbase.html',{'curl':curl,'output':'Changed Successfully'})

def change(request):
    if (request.method=="GET"):
            return render(request,'cpass.html',{'curl':curl,'output':''})
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
            
                return render(request,'cpass.html',{'curl':curl,'output':'Changed Successfully'})
            else:
                return render(request,'cpass.html',{'curl':curl,'output':'Existing Password Is Invalid'})
        

def info(request):
    if (request.method=="GET"):
            return render(request,'minfo.html',{'curl':curl,'output':''})
    else:	
            
            
            email=request.POST.get('email')
            field=request.POST.get('field')
            value=request.POST.get('value')	
            query="update facultydb set %s='%s' where email='%s' " %(field,value,email)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'minfo.html',{'curl':curl,'output':'Changed Successfully'})
        
def newinfo(request):
    if (request.method=="GET"):
            return render(request,'minfo1.html',{'curl':curl,'output':''})
    else:	
            
            first=request.POST.get('first')
            last=request.POST.get('last')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            mobile=request.POST.get('mobile')
            role=request.POST.get('role')
            gender=request.POST.get('gender')
            salary=int(request.POST.get('salary'))
            experience=request.POST.get('experience')
            deptname=request.POST.get('deptname')
            day=request.POST.get('day')
            date=request.POST.get('date')
            year=request.POST.get('year')
            deptid=request.POST.get('deptid')
            
            	#(first_name,second_name,email,password,mobile,address,gender,role,myattend,totalattend,leaveapp,salary,experience)
            query="insert into facultydb values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','1','1','no','%s','%s')" %(first,last,email,password,mobile,address,gender,role,salary,experience)
            models.cursor.execute(query)
            models.db.commit()
            query1=" select * from facultydb where email='%s'"%(email)
            models.cursor.execute(query1)
            userDetails=models.cursor.fetchall()
            regid=userDetails[0][0]
            query2=" insert into facultydbdob values(%s,'%s','%s','%s')"%(regid,day,date,year)
            models.cursor.execute(query2)
            models.db.commit()
            query2=" insert into facultydbdept values(%s,'%s','%s')"%(regid,deptname,deptid)
            models.cursor.execute(query2)
            models.db.commit()
            
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
                                <h2>Your details have been successfully added, Please use following credentials to login to <a href='http://localhost:8000/login/'></a></h2>
                                <h2>Email : """+email+"""</h2>
                                <h2>Password : """+str(password)+"""</h2>
                                		
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
            
            return render(request,'minfo1.html',{'curl':curl,'output':'Added New User And Mail Sent Successfully'})
        

def experience(request):
    if (request.method=="GET"):
            return render(request,'mexp.html',{'curl':curl,'output':''})
    else:	
            
            field=request.POST.get('field')
            email=request.POST.get('email')
            value=int(request.POST.get('value'))	
            if field=='Years' :
                query="update facultydb set experience='%s Years' where email='%s' " %(value,email)
                models.cursor.execute(query)
                models.db.commit()
            else:
                query="update facultydb set experience='%s Months' where email='%s' " %(value,email)
                models.cursor.execute(query)
                models.db.commit()
            
            
            
            return render(request,'mexp.html',{'curl':curl,'output':'Updated Successfully'})

def salary(request):
    if (request.method=="GET"):
            return render(request,'msalary.html',{'curl':curl,'output':''})
    else:	
            
            field=request.POST.get('field')
            email=request.POST.get('email')
            value=int(request.POST.get('value'))
            query="select * from facultydb where email='%s'" %(email)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()	
            if field=='Increment' :
                sal=int((userDetails[0][12]+(userDetails[0][12]*(value/100))))
            else:
                sal=int((userDetails[0][12]-(userDetails[0][12]*(value/100))))
            
            query="update facultydb set salary='%s' where email='%s' " %(sal,email)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'msalary.html',{'curl':curl,'output':'Updated Successfully'})

    
def leave(request):
    if (request.method=="GET"):
            return render(request,'mleave.html',{'curl':curl,'output':''})
    else:	
            
            
            email=request.POST.get('email')
            value=request.POST.get('value')	
            query="update facultydb set leaveapp='%s' where email='%s' " %(value,email)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'mleave.html',{'curl':curl,'output':'Updated Successfully'})

def login(request):
    if (request.method=="GET"):
            return render(request,'mlogin.html',{'curl':curl,'output':''})
    else:	
            
            
            email=request.POST.get('email')
            field=request.POST.get('field')
            query="update facultydb set role='%s' where email='%s' " %(field,email)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'mlogin.html',{'curl':curl,'output':'Updated Successfully'})
        
    
def delete(request):
    if (request.method=="GET"):
            return render(request,'mdelete.html',{'curl':curl,'output':''})
    else:	
            email=request.POST.get('email')
            query="delete from facultydb where email='%s' " %(email)
            models.cursor.execute(query)
            models.db.commit()
            
            return render(request,'mdelete.html',{'curl':curl,'output':'Deleted Successfully'})
    