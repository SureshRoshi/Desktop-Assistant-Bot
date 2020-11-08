import datetime

def gettime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    return strTime