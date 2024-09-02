import pyupbit
import requests
import dotenv
import os

#val setting
dotenv.load_dotenv()
hostenv = os.getenv("DB_HOST")
userenv = os.getenv("DB_USER")
passwdenv = os.getenv("DB_PASSWORD")
charsetenv = os.getenv("DB_CHARSET")
svrNo = os.getenv("SVR_NO")


#function Set
def print_hi(name):
    print(hostenv)


#Main Process

if __name__ == '__main__':
    print_hi('PyCharm')


