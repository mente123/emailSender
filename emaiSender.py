import smtplib # communicates with smtp services like gmail and yahoo

reciever = input("Enter the email of recipient: \n")

content = input("Enter the content of the email: \n")

def sendEmail(reciever, content):
    myEmail = "example@gmail.com"
    server = smtplib.SMTP('smptp.gmail.com', 587) # specify the server and port number
    server.ehlo() # make a communication with gmail server
    server.starttls() #start the session for us
    server.login(myEmail,'password') # login to email with our email address and password
    server.sendmail(myEmail,reciever, content)
    server.close()
    
sendEmail(reciever, content)






















