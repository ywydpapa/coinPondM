import pyupbit
import requests
import dotenv
import os,sys
import dbconn
import datetime,time

#val setting
dotenv.load_dotenv()
hostenv = os.getenv("DB_HOST")
userenv = os.getenv("DB_USER")
passwdenv = os.getenv("DB_PASSWORD")
charsetenv = os.getenv("DB_CHARSET")
svrNo = os.getenv("SVR_NO")
serVer = os.getenv("SERVICE_VER")

#function Set
def trademain():
    print(hostenv)


def service_restart():
    tstamp = datetime.now()
    print("Service Restart : ", tstamp)
    myip = requests.get('http://ip.jsontest.com').json()['ip']
    msg = "Server " + str(svrNo) + " Multi Service Restart : " + str(tstamp) + "  at  " + str(myip) + " Service Ver : "+ str(serVer)
    dbconn.errlog(msg, '0')
    os.execl(sys.executable, sys.executable, *sys.argv)


def service_start():
    tstamp = datetime.now()
    print("Service Start : ", tstamp)
    myip = requests.get('http://ip.jsontest.com').json()['ip']
    msg = "Server " + str(svrNo) + " Multi Service Start : " + str(tstamp) + "  at  " + str(myip) + " Service Ver : "+ str(serVer)
    dbconn.errlog(msg,0)


#Main Process

if __name__ == '__main__':
    dbconn.clearcache()


