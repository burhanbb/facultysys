from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from . import models
import time
from django.core.mail import send_mail
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from . import settings

curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL

def home(request):	
	return render(request,'home.html',{'curl':curl})

def contact(request):	
    if (request.method=="GET"):
            return render(request,'contact.html',{'curl':curl,'output':''})
    else:	
            
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            
            
            me = "burhanuddinbootwala6864@gmail.com"
            you = "en18cs301071@medicaps.ac.in"
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "QUERY MAIL"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Following Query Was Registered!</h1>
                                <p></p>
                                <h2>Name: """+name+"""</h2>
                                <h2>Email: """+email+"""</h2>
                                <h2>Subject: """+subject+"""</h2>
                                <h2>Message: """+message+"""</h2>
                                <br></br>
                                	
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
            print("Submitted Successfully")
            
            return render(request,'contact.html',{'curl':curl,'output':'Sent Successfully'})
        	
def forget(request):
    if (request.method=="GET"):
            return render(request,'forget.html',{'curl':curl,'output':''})
    else:	
            email=request.POST.get('email')	
            query="select * from facultydb where email='%s' " %(email)
            models.cursor.execute(query)
            userDetails=models.cursor.fetchall()
            
            me = "burhanuddinbootwala6864@gmail.com"
            you = email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Forgot Password Medi-FRMCampus"
            msg['From'] = me
            msg['To'] = you
            html = """<html>
                        <head></head>
                            <body>
                                <h1>Welcome to Medi-FRMCampus</h1>
                                <p>Your Details Are Shown Below</p>
                                <h2>Email : """+email+"""</h2>
                                <h2>Password : """+str(userDetails[0][4])+"""</h2>
                                <br>
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
            
            return render(request,'forget.html',{'curl':curl,'output':'Check Your Email'})
        
    

def portfolio(request):	
	return render(request,'portfolio.html',{'curl':curl})

def about(request):	
	return render(request,'about.html',{'curl':curl})

def engineering(request):
    return render(request,'project.html',{'curl':curl})
def management(request):
    return render(request,'projectmanage.html',{'curl':curl})
def commerce(request):
    return render(request,'projectcom.html',{'curl':curl})
def science(request):
    return render(request,'projectscience.html',{'curl':curl})
def social(request):
    return render(request,'projectsocial.html',{'curl':curl})
def art(request):
    return render(request,'projectart.html',{'curl':curl})
def human(request):
    return render(request,'projecthuman.html',{'curl':curl})
def agriculture(request):
    return render(request,'projectagri.html',{'curl':curl})
def pharmacy(request):
    return render(request,'projectpharm.html',{'curl':curl})




def login(request):
	if request.method=="GET": 
		return render(request,'login.html',{'curl':curl,'output':''})
	else:
		email=request.POST.get('email')	
		password=request.POST.get('password')	
		
		query="select * from facultydb where email='%s' and password='%s' " %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		if len(userDetails)>0:
			if userDetails[0][8]=='admin':
				response=redirect(curl+'ad94bHry73/')
			elif userDetails[0][8]=='manager':	
				response=redirect(curl+'mahd748hdYd/')
			else:
				response=redirect(curl+'uy43hBgd843/')
			response.set_cookie('cunm',email,3600)
			return response		
		else:
			return render(request,'login.html',{'curl':curl,'output':'Invalid Email Or Password'})	
			






