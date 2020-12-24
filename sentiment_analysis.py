#function used to calculate the happiness score of the timezone provided, also calculates number of keyword tweets
def find_score(timezone, keywords):

#variables are defined
    region_score = 0
    tweet_score = 0
    count_of_keyword_tweets = 0
    count_of_keywords = 0
    average = 0

#main loop that iterates for each tweet in the given timezone
    for tweet in timezone:
        tweet_score = 0
        count_of_keywords = 0

#nested loop that iterates for each word in the tweet, words are compared to keywords, temporary list is used
        for word in tweet:
            word = word.strip("""!#$%&'()*+",-./:;<=>?@[]^_`{|}~""")
            word = word.lower()

            for keyword in keywords:
                temp = keyword.split(",")
                if word == temp[0]:
                    count_of_keywords += 1
                    tweet_score += int(temp[1])

# calculates the score of the tweet, adds to the regional score if necessary
        if count_of_keywords > 0:
            tweet_score /= count_of_keywords
        if count_of_keywords >= 1:
            region_score += tweet_score
            count_of_keyword_tweets += 1

#regional score is calculated
    if count_of_keyword_tweets > 0:
        average = region_score/count_of_keyword_tweets

#regional score, the amount of keyword tweets, and the total number of tweets are returned
    return average, count_of_keyword_tweets, len(timezone)


#main function that reads from given files, organizes tweets based on location, and returns the calculated statistics
def compute_tweets(tweetsfile,keywordsfile):

#reads from tweets file
    try:
        tweets_file = open(tweetsfile, encoding='utf-8', errors='ignore')
        tweets_lines = tweets_file.readlines()
        tweets_file.close()
    except:
        results_list = []
        return results_list

#reads from keywords file
    try:
        keywords_file = open(keywordsfile, encoding='utf-8', errors='ignore')
        keywords = keywords_file.readlines()
        keywords_file.close()
    except:
        results_list = []
        return results_list

#lists are defined
    locations = []
    tweets = []
    Eastern = []
    Central = []
    Mountain = []
    Pacific = []
    count = 0

#Constants are defined, only points that will be needed to find the location of the tweets are defined
    P1 = (49.189787, -67.444574)
    P2 = (24.660845, -67.444574)
    P3 = (49.189787, -87.518395)
    P5 = (49.189787, -101.998892)
    P7 = (49.189787, -115.236428)
    P9 = (49.189787, -125.242264)

#loops used to break the data from the tweets file into location and tweets lists seperately
    for i in tweets_lines:
        temp = i.split("]")
        temp[0] = temp[0].strip("[")
        locations.append((temp[0].split(",")))

        temp1 = temp[1].split()
        for j in range(0,3):
            del temp1[0]
        tweets.append((temp1))

#loop used to organize tweets into timezones based on latitude and longitude
    for i in locations:
        i[0] = float(i[0])
        i[1] = float(i[1])

        if i[0] <= P1[0] and i[0] >= P2[0]:
            if i[1] <= P1[1] and i[1] >= P3[1]:
                Eastern.append(tweets[count])
            elif i[1] <= P3[1] and i[1] >= P5[1]:
                Central.append(tweets[count])
            elif i[1] <= P5[1] and i[1] >= P7[1]:
                Mountain.append(tweets[count])
            elif i[1] <= P7[1] and i[1] >= P9[1]:
                Pacific.append(tweets[count])
        count += 1

#function called to find the score of each timezone, results are placed into a list and returned to main.py
    eastern_tuple = find_score(Eastern, keywords)
    central_tuple = find_score(Central, keywords)
    mountain_tuple = find_score(Mountain, keywords)
    pacific_tuple = find_score(Pacific, keywords)
    results_list = [eastern_tuple, central_tuple, mountain_tuple, pacific_tuple]
    return results_list
