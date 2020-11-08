import wikipedia

def getdata(data):
    query=data['message'].lower()
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=2)
    except Exception as e :
        results = "Cannot find any result.Please try again"
    return results