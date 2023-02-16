
import smtplib    
import ssl


smtpserver='smtp.gmail.com'
sender_mail = 'fousiqbal@gmail.com'    
receivers_mail = ['fousiaiqbal5@gmail.com']  
password = "fjsjfghejhkfakj"      
message = f"""From: From Person {sender_mail} 
To: To Person {receivers_mail} 
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""   
try:    
   smtpObj = smtplib.SMTP(smtpserver,587) 
   smtpObj.starttls()
   context = ssl.create_default_context()   
   smtpObj.login(sender_mail,password)    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")  
finally :
   smtpObj.quit() 
