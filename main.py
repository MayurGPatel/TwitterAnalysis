#Name:           Mayur Patel
#Student Number: 251158360
#Course:         COMPSCI 1026A
#Description:    This program calculates how happy people are in various timezones of the US, based on Twitter's tweets

from sentiment_analysis import compute_tweets

#variables are defined
count_name = 0
count_stat = 0
timezone_name = ""

#file names are taken as input
tweets_file = input("Please enter the name of the file containing tweets: ")
keywords_file = input("Please enter the name of the file containing keywords: ")
print("\n")

#a function is called in order to compute the statistics, results are placed in a list
results = compute_tweets(tweets_file, keywords_file)

#loop used to ouput all statistics, which are grouped by timezone
for timezone in results:
    if count_name == 0:
        timezone_name = "Eastern"
    elif count_name == 1:
        timezone_name = "Central"
    elif count_name == 2:
        timezone_name = "Mountain"
    elif count_name == 3:
        timezone_name = "Pacific"

    count_stat = 0
    for statistic in timezone:
        if count_stat == 0:
            print("The Happiness Score for the", timezone_name, "timezone is:", statistic)
        elif count_stat == 1:
            print("The amount of Keyword Tweets for the", timezone_name, "timezone is:", statistic)
        elif count_stat == 2:
            print("The amount of Tweets for the", timezone_name, "timezone is:", statistic)
        count_stat += 1
    print("\n")

    count_name += 1
