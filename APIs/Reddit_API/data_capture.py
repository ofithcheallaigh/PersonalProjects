import json
import requests
import requests.auth
from my_private_config import username, password, client_secret, client_id
from pprint import pprint
import pandas as pd

client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

post_data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}

headers = {'User-Agent': 'MyAPI by LateThree1'}
TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
response = requests.post(TOKEN_ACCESS_ENDPOINT, data=post_data, headers=headers, auth=client_auth)

# print(response.reason)
# print(response.json())

TOKEN = response.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'
# print(headers)

# Now that we have this authorisation, we can access all other end-points within reddit
temp = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers).json()
# pprint(temp)

# Look for "hot" posts on x-subreddit
res = requests.get('https://oauth.reddit.com/r/northernireland/hot', headers=headers, params={'limit':100})
with open('hot.json', 'w') as outfile:
    json.dump(res.json(), outfile, indent=4)

# Now to extract some more targeted information
# for post in res.json()['data']['children']:
    # print(post)

# for post in res.json()['data']['children']:
    # print(post['data']['title']) 

# initalise empty dataframe
df = pd.DataFrame()

# -------------------------------------------------------- #
# ----------------- Data Capture Stat -------------------- #
# -------------------------------------------------------- #
"""
To Do: Put into a function once I figure out how to work with the various 'after' string 
which is used in the parameter to allow me to extract data after that post
"""
for post in res.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'post_title': post['data']['title'],
        'post_author': post['data']['author'],
        'post_content': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score'],
        'created': post['data']['created_utc'],
        'url': post['data']['url']
    }, ignore_index=True)

# print(df)
# df.to_json("reddit_ni_data.json")

# to see all the options open to us, we can use:
# print(post['data'].keys())


# print(post['kind'] + '_' + post['data']['id'])
print(post['kind'] + '_' + post['data']['id'])

res1 = requests.get('https://oauth.reddit.com/r/northernireland/hot', headers=headers, params={'limit':100, 'after':'t3_v5dvju'})

for post in res1.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'post_title': post['data']['title'],
        'post_author': post['data']['author'],
        'post_content': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score'],
        'created': post['data']['created_utc'],
        'url': post['data']['url']
    }, ignore_index=True)

# df.to_json("reddit_ni_data.json")

print(post['kind'] + '_' + post['data']['id'])

res2 = requests.get('https://oauth.reddit.com/r/northernireland/hot', headers=headers, params={'limit':100, 'after':'t3_v33xwa'})

for post in res2.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'post_title': post['data']['title'],
        'post_author': post['data']['author'],
        'post_content': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score'],
        'created': post['data']['created_utc'],
        'url': post['data']['url']
    }, ignore_index=True)

print(post['kind'] + '_' + post['data']['id'])

res3 = requests.get('https://oauth.reddit.com/r/northernireland/hot', headers=headers, params={'limit':100, 'after':'t3_v0wi6i'})

for post in res3.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'post_title': post['data']['title'],
        'post_author': post['data']['author'],
        'post_content': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score'],
        'created': post['data']['created_utc'],
        'url': post['data']['url']
    }, ignore_index=True)

print(post['kind'] + '_' + post['data']['id'])

res4 = requests.get('https://oauth.reddit.com/r/northernireland/hot', headers=headers, params={'limit':100, 'after':'t3_v07yav'})

for post in res4.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'post_title': post['data']['title'],
        'post_author': post['data']['author'],
        'post_content': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score'],
        'created': post['data']['created_utc'],
        'url': post['data']['url']
    }, ignore_index=True)

df.to_json("reddit_ni_data.json") # Save to json file

# ----------------------------------------------------------- #
# --------------- Data Capture End -------------------------- #
# ----------------------------------------------------------- #

