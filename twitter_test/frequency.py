import json
import sys
import operator

## Function to identify and separate out stop words from the tweets.StopWords list taken from http://xpo6.com/list-of-english-stop-words/
def isStopWord(word):
    stopWords = ["a", "about", "above", "above", "across", "after", "afterwards", \
                 "again", "against", "all", "almost", "alone", "along", "already", \
                 "also","although","always","am","among", "amongst", "amoungst", "amount",  \
                 "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", \
                 "are", "around", "as",  "at", "back","be","became", "because","become","becomes", \
                 "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides",\
                 "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

    if word in stopWords:
        return True
    else:
        return False
    

def calculateFrequency():    
    #create an empty dictionary
    freq = {}
    
    tweet_file = open("tweets.txt","rb")

    # To save the total words in the data stream parsed
    totalTerms = 0
    
    for line in tweet_file:
        #newList.append(line)
        newLine = json.loads(line , encoding="utf-8")
        new = str((newLine.get("text","")).encode("utf-8"))
        sentence = new.split()
        for word in sentence:
            totalTerms += 1
            if word.isalpha() and isStopWord(word)== False:
                word = word.lower()
                freq[word] = freq.get(word , 0) + 1


    # Display the Total words in the stream
    print "Total words = ", totalTerms
    
   
    # Sorting the dictionary based on values. Descending sort for extracting the top 10 frequencies, using the operator module
    topFrequencies = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

    # Print the top occurring words in a nice formatted way. I add variable no of spaces to make the display aligned
    print "The top 10 words which appear most frequently are as below"
    for i in range(10):
        print topFrequencies[i][0]," "*(10-len(topFrequencies[i][0])),": ",topFrequencies[i][1]

    


## Main function
if __name__ == '__main__':
    calculateFrequency()




