import twitterstream as TWITTER
import frequency


if __name__ == "__main__":
    
    # Access the twitter_stream.py modeule to save a sample data from the streaming API. This would generate a file "tweets.txt" and save in the curr directory
    TWITTER.fetchsamples()

    # Getting the file and get the frequency
    frequency.calculateFrequency()


    
