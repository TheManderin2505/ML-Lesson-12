import pandas as pd

data = pd.read_csv("C:/Users/alexd/Desktop/Machine Learning/Lesson 12/sng.csv")



out = data[['track_id','artist_ids','release_date','speechiness']]

data = data.drop("track_id",axis=1)
data = data.drop("artist_ids",axis=1)
data = data.drop("release_date",axis=1)
data = data.drop("speechiness",axis = 1)
data = data.drop("album_id",axis=1)




from sklearn.preprocessing import LabelEncoder
encoder1 = LabelEncoder()

columes_1 = ["track_name","artist_names","year","acousticness","danceability","duration_ms","energy","explicit","instrumentalness","key","liveness","loudness","mode","popularity","tempo"]

for j in columes_1:
    data[j] = encoder1.fit_transform(data[j])



def ask_usr_1():

    user_I1 = input("What type of music would you like to listen to? ").lower()
    request = user_I1.split()
    print(request)

    
    if "high" in request:
        v1 = 1
       
    elif "low" in request:
        v1 = 0

    if "loud" in request:
        volume = 1 

    elif "quite" in request or "soft" in request :
        volume = 0

    if "tempo" in request:
        tempo = 1
        print("Tempo : ",tempo)

    

    print("v1 : ",v1)
    print("volume : ",volume)
    


    
ask_usr_1()




