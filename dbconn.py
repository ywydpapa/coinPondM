import pymysql
import dotenv
import pyupbit
import os
import time,datetime
import requests


#setup values
dotenv.load_dotenv()
hostenv = os.getenv("DB_HOST")
userenv = os.getenv("DB_USER")
passwdenv = os.getenv("DB_PASSWD")
dbnameenv = os.getenv("DB_DATABASE")
charsetenv = os.getenv("DB_CHARSET")
nowt = datetime.datetime.now()
now = nowt.strftime("%Y-%m-%d %H:%M:%S")
myip = requests.get('http://ip.jsontest.com').json()['ip']


#exp functions
def checkwallet(uno): #지갑 내용 조회
    global key1, key2, walletitems
    walletitems = []
    db01 = pymysql.connect(host=hostenv, user=userenv, password=passwdenv, db=dbnameenv, charset=charsetenv)
    cur01 = db01.cursor()
    try:
        sql = "SELECT apiKey1, apiKey2 FROM pondUser WHERE userNo=%s and attrib not like %s"
        cur01.execute(sql,(uno, '%XXX'))
        keys = cur01.fetchall()
        if len(keys) == 0:
            print("No available Keys !!")
        else:
            key1 = keys[0][0]
            key2 = keys[0][1]
            upbit = pyupbit.Upbit(key1,key2)
            walletitems = upbit.get_balances()
    except Exception as e:
        msg = "업비트 지갑 조회 오류 " + now + " (" + str(e) + ") at "+myip
        errlog(msg, uno)
    finally:
        cur01.close()
        db01.close()
        return walletitems


def checkwalletwon(uno): #지갑내 원화 조회
    global key1, key2, walletwon
    db02 = pymysql.connect(host=hostenv, user=userenv, password=passwdenv, db=dbnameenv, charset=charsetenv)
    cur02 = db02.cursor()
    try:
        sql = "SELECT apiKey1, apiKey2 FROM pondUser WHERE userNo=%s and attrib not like %s"
        cur02.execute(sql,(uno, '%XXX'))
        keys = cur02.fetchall()
        if len(keys) == 0:
            print("No available Keys !!")
        else:
            key1 = keys[0][0]
            key2 = keys[0][1]
            upbit = pyupbit.Upbit(key1,key2)
            walletwon = round(upbit.get_balance("KRW"))
    except Exception as e:
        msg = "업비트 지갑 원화 조회 오류 " + now + " (" + str(e) + ") at "+myip
        errlog(msg, uno)
    finally:
        cur02.close()
        db02.close()
        return walletwon


def getsetup(uno): # 설정 조회
    global setupdata
    db03 = pymysql.connect(host=hostenv, user=userenv, password=passwdenv, db=dbnameenv, charset=charsetenv)
    cur03 = db03.cursor()
    try:
        sql = "SELECT * from multiSetup where userNo=%s and attrib not like %s"
        cur03.execute(sql, (uno, '%XXXUP'))
        setupdata = cur03.fetchall()
    except Exception as e:
        msg = "설정 조회 오류 " + now + " (" + str(e) + ") at "+myip
        errlog(msg, uno)
    finally:
        cur03.close()
        db03.close()
        return setupdata


def errlog(errmsg,uno):
    global rows
    db04 = pymysql.connect(host=hostenv, user=userenv, password=passwdenv, db=dbnameenv, charset=charsetenv)
    cur04 = db04.cursor()
    try:
        sql = "INSERT INTO error_Log (error_detail, userNo) VALUES (%s, %s)"
        cur04.execute(sql,(errmsg, uno))
        db04.commit()
    except Exception as e:
        print('에러 메세지 전송오류 :',now,'내용 ', e)
    finally:
        cur04.close()
        db04.close()


def clearcache():
    db05 = pymysql.connect(host=hostenv, user=userenv, password=passwdenv, db=dbnameenv, charset=charsetenv)
    cur05 = db05.cursor()
    sql = "RESET QUERY CACHE"
    cur05.execute(sql)
    cur05.close()
    db05.close()


def getsvruser(svrNo):
    global userdata
    db06 = pymysql.connect(host=hostenv, user=userenv, password=passwdenv, db=dbnameenv, charset=charsetenv)
    cur06 = db06.cursor()
    try:
        sql = "SELECT userNo from tradingSetup where attrib not like %s and serverNo=%s"
        cur06.execute(sql,('%XXXUP', svrNo))
        userdata = cur06.fetchall()
    except Exception as e:
        msg = "서버별 사용자 조회 오류 " + now + " (" + str(e) + ") at "+myip
        errlog(msg, 0)
    finally:
        cur06.close()
        db06.close()
        return userdata

