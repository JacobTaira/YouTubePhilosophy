import random
import pandas as pd
from openai import OpenAI
import getpass
import googleapiclient.discovery
import pandas as pd
import sys
import io
import os
from NoTouchy import secret_key



client = OpenAI(api_key=secret_key)

def get_response(example):
    """
    You are looking for quotes that could be applied in any context that are motivational and inspring."  
    "I am going to give you a collection of statements, and you must determine whether they are motivational or not." 
    "Do not respond with any output other than 'motivational' or 'not motivational." 
    "Also, any responses with inappropriate language, or language that includes 'shoutout' or 'video' or 'compilation' or" 
    "'videos like this' or 'compilations like this' or 'everyone who is watching this' should be automatically classified as not motivational.
    """
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "You are an expert in motivational speaking and determining whether comments by online users are motivational or not. Responses that can't be used in every setting/context should be marked as not motivational"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "If you're still breathing, you still have a chance to win"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "motivational"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "You changed my mentality ❤️🧠"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "not motivational"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Self Love is powerful",
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "motivational"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "be strong 🔥 ",
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "motivational"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "This compilation is a goldmine of motivation!",
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "not motivational"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Roar 🦁!",
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "motivational"
            }
        ]
        },
        {
        "role" : "user",
        "content" : f"""{example}"""
        }
    ],
    temperature=1,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "text"
    }
    )
    return response.choices[0].message.content # end of get response method

# set the encoding in your print statement by using the encoding parameter to deal with emojis in comments
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBtD0uJ9nNGgzu2Mou-NxkhXC3CyCgLGH0"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

video_ids = ["wpELD9wJqU8", "C3npAsGtY4U", "nvASM3ORLvY"]         #, "dQw4w9WgXcQ","eVTXPUF4Oz4","kxopViU98Xo","9bZkp7q19f0"
random_video_id = random.choice(video_ids)
print ("random_video_id: " + random_video_id)
request = youtube.commentThreads().list(
    part ="snippet",
    videoId = random_video_id, # this would have to be randomized 
    maxResults = 400
)
response = request.execute()
randomized_items = random.sample(response['items'], min(10, len(response['items'])))

comments = []
for item in randomized_items:   #['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    comments.append([
        comment['authorDisplayName'],
        comment['publishedAt'],
        comment['updatedAt'],
        comment['likeCount'],
        comment['textDisplay']
    ]
)

pd.set_option('display.max_columns', None)

df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
df = df.head(10)
df['GPT Assessment'] = df['text'].apply(get_response)

# Define the directory and file path
directory = "C:/Users/Jacob/ProfoundYouTubeMotivation/Data"
file_name = "output.csv"
file_path = os.path.join(directory, file_name)

# Save DataFrame to CSV, overwriting if file exists
df.to_csv(file_path, index=False)


motivational_comments = df[df['GPT Assessment'] == 'motivational']
genericQuotes = [
    "Dont stop when you are tired , stop when you are done 💪", 
    "BE COURAGEOUS AND BE STRONG, says THE LORD JESUS CHRIST, amen. 🥰🥰🥰",
    "Supper❤",
    "I stood alone.I betrayed I broked But when i m back I look me .. 🥵"
    "In the darkest moments, you must be your very best",
    "Self Discipline Is Self-Love.” 👍🙏🏽🥊❤️"
    "Get going get your life back live the best life what ever you have left every day you have a second chance !!!No one is promised tomorrow !!!LIVE IT!!!!❤❤❤"
    "If you don't build your dream someone else will hire you to help build theirs"
]
random_quote = random.choice(genericQuotes)

# Check if there are any motivational comments
if not motivational_comments.empty:
    # Randomly select one of the motivational comments
    random_motivational_comment = motivational_comments.sample(n=1)['text'].values[0] #alues[0] retrieves the text from random row
    # Store the comment in a string
    motivational_comment_string = f"{random_motivational_comment}"
else:
    motivational_comment_string = random_quote

print(motivational_comment_string)