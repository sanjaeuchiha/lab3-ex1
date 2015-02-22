import smtplib 

fromaddr = 'sanjae_allen@hotmail.com'
toaddr = 'sanjae_allen@hotmail.com'
message = """From:{}<{}>
To:{}<{}>
Subject:{}

{}
"""
fromname = "Bunny Allen"
fromaddr = "sanjae_allen@hotmail.com"
toname = "Bunny Allen"
toaddr = "sanjae_allen@hotmail.com"
subject = "lab3"
msg = "yow trial"

messagetosend = message.format(
                fromname,
                fromaddr,
                toname,
                toaddr,
                subject,
                msg)
                
# Credetials(if needed)
username = 'sanjae_allen@hotmail.com'
password ='esdhxyuvfvkietod'

#The actual mail send
server = smtplib.SMTP('smtp.live.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()