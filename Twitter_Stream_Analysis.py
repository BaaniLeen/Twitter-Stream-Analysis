import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'psycho_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()



playtime = []

for x in tweets_data:
	if("place" in x):
		if x["place"] != None:
			if "country" in x["place"]:
				playtime.append(x["place"]["country"])

tweets['country'] = playtime
# tweets['retweet_count'] = map(lambda tweet: tweet['text'], tweets_data)
# tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

plt.show()