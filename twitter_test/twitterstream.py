import oauth2 as oauth
import urllib2 as urllib
import time, sys

# Variables related to time to stop the execution after 5 minutes
start = 0
end = 0

# The oauth keys are initialized as global variables
api_key = "InKK7Tdfgm8IaJTVxdSSTtS0x"
api_secret = "l3ip2si3V4XWg8Tspz0tAcbFRzyx2eiZy6pcdBNm2qWbAk6Sto"
access_token_key = "2610970604-HGdwngAlGMuIXRshaASwNsmxQf08iNQmxOfgSum"
access_token_secret = "TOsZX0yMrJME0keRa9UkP1JL7nLgMlRYn9QDAOxDr5FDh"

_debug = 0


# Generating the oauth token
oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)


#Construct, sign, and open a twitter streaming API request using the hard-coded credentials above.


def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)
  return response


def fetchsamples():
  # This URL fetches all the samples in English
  URL = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
  parameters = []
  

  #create an output file "tweets.txt", and redirect the twitter stream to save into it
  output = open("tweets.txt","w")

  percent = 0
  
  start = time.clock()

  # Receiving the response from the Twitter Stream API
  response = twitterreq(URL, "GET", parameters)
  
  print "Saving tweets from Twitter Streaming API..." 
  for line in response:
    writeLine = line.strip()
    output.write(writeLine+"\n")
    if(int(time.clock() - start) >= 300):
      output.close()
      return
    
      
      

if __name__ == '__main__':
  fetchsamples()
