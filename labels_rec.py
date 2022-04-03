import requests 
from secrets1 import CLIENT_ID, CLIENT_SECRET

def labels_rec(keywords):
    AUTH_URL = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        })
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)}
    
    BASE_URL = 'https://api.spotify.com/v1/'

    leng = len(keywords)
    urls = []
    print("hi")
    
    for i in range(0, leng):
        r = requests.get(BASE_URL + "search?q="+keywords[i]+"&type=track", headers=headers)
        r = r.json()
        
        for j in range(0,1):
            try:
                r = requests.get(BASE_URL + "search?q="+keywords[i]+"&type=track&limit=5", headers=headers)
                r = r.json()


                for j in range(0,5):
                    urls.append(r['tracks']['items'][j]['external_urls']['spotify']) 
            except:
                print("No songs matched")
    
    return urls  

