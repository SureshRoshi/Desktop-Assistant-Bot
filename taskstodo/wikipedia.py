## Search in wikipedia and print the first statement taken from the wikipedia
import wikipedia

def getdata(data):
    query=data['message'].lower()
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=1)
    except Exception as e :
        results = "No result found.Please try again"
    return results