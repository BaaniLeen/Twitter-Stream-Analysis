#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy.streaming import Stream
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

#Variables that contains the user credentials to access Twitter API
access_token = "820657672173142016-vI7RxNo64qHhY9cEXfFKTCGuH4oJNsw"
access_token_secret = "bE8Dt356mwYyoEMrZ3EJAr144IQSCznWL1QH9TNKurP3J"
consumer_key = "C2lB3tMoRvPpJcSkKRFBTDqEd"
consumer_secret = "L8i0FKLzwdGPTqe68nwRbiyf9ewWLwBOziakrOmghSiHj1D43z"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api=API(auth)
    
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'CVE'
    stream.filter(track=['feel happy','glad','elated','proud','adorable','awesome','appreciate','amazed','awe','joy','happiness','applaud','curious','excited','bless','bliss','bubbling','be happy','am happy','faith','thank you','thanks','creativity','contented','cheerful','cheery','merry','jovial','glee','delighted','gratified','ecstatic','exultant','good mood','high spirits'],async=True)