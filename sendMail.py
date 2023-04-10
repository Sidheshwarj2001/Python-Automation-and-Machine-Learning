import smtplib

def sendmain():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login("sidheshwarj2001@gmail.com","evogucrtwpjcknco")

    subject = " this email is send by Script"
    body = " ffsfhffjoihffj;hshf;hshfalfjflhlahlddffhldhlfh"

    message = "Subject : {}\n\n{}".format(subject,body)

    kiskosendkarna = ["sidjawale007@gmail.com","jawalesp108@gmail.com"]

    server.sendmail("sidheshwarj2001@gmail.com",kiskosendkarna,

def main():
    sendmain()

if __name__ == '__main__':
    main()