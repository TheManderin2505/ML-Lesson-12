import pandas as pd

data = pd.read_csv("C:/Users/alexd/Desktop/Machine Learning/Lesson 12/sng.csv")



out = data[['track_id','artist_ids','release_date','speechiness']]

data = data.drop("track_id",axis=1)
data = data.drop("artist_ids",axis=1)
data = data.drop("release_date",axis=1)
data = data.drop("speechiness",axis = 1)
data = data.drop("album_id",axis=1)

print(data.head,data.info())


from sklearn.preprocessing import LabelEncoder
encoder1 = LabelEncoder()

columes_1 = ["track_name","artist_names","year","acousticness","danceability","duration_ms","energy","explicit","instrumentalness","key","liveness","loudness","mode","popularity","tempo"]

for j in columes_1:
    data[j] = encoder1.fit_transform(data[j])

print(data.head())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(stop_words="english")


