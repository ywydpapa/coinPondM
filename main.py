import pyupbit
import requests
import dotenv
import os,sys
import dbconn
import datetime,time

#val setting
dotenv.load_dotenv()
svrNo = os.getenv("SVR_NO")
serVer = os.getenv("SERVICE_VER")

#function Set
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
    while True:
        users = dbconn.getsvruser(svrNo) # 할당 사용자 조회
        for user in users:
            setups = dbconn.getsetup(user[0])
            print(setups)
        dbconn.clearcache() # 캐쉬 삭제
        time.sleep(10)


