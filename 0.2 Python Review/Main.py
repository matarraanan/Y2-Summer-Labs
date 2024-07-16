import random as rnd

def create_youtube_video(title, description,hashtags):
    youtube_video = {
        "Title": title,
        "Description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {},
        'hashtag': hashtags[:5]  
    }
    return youtube_video

def like_vid(youtube_video):
    youtube_video["likes"] += 1

def dislike_vid(youtube_video):
    youtube_video["dislikes"] += 1

def add_comment(youtube_video, username, comment):
    youtube_video["comments"][username] = comment
    return youtube_video
def similarity_to_video(video1, video2):
    use1 = video1['hashtag']
    use2 = video2['hashtag']
    percent = 0
    
  
    min_length = min(len(use1), len(use2))
    
   
    for i in range(min_length):
        if use1[i] == use2[i]:
            percent += 20  
    
    return percent
def trendy (vid):
	if vid["likes"] > 20 and vid["likes"] > vid["dislikes"]:
		return True

	return False

def rndh(hashtags):
	hastag = []
	for i in range (5):
		hastag.append(random.choice(hashtags))
	return hashtag




hashtags = ["funny", "sad" , "great" , "amazing","boo", "nice", "wow","eww"]
vid = create_youtube_video("bro", "funny",hashtags)
vid2 = create_youtube_video("bro", "funny",hashtags)
for i in range(495):
    like_vid(vid)
trendy = bool( trendy ( vid))
dislike_vid(vid)
add_comment(vid, "matar", "shit")
simailarity = similarity_to_video(vid,vid2)
rndh
if(trendy):
	print(trendy)
print(simailarity)
print(vid)

