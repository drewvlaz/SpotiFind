from SpotifyClient import *
from statistics import variance, mean
import math
def match_emotion(list_of_faces):
    a = SpotifyClient("Hack2022")
    mood_list = a.get_category_playlists("mood")['playlists']['items']
    dict_x = {}
    for x in mood_list:
        dict_x[x['name']] = x['id']
    
    #print(dict_x)
    
    joy_total = [x[0] for x in list_of_faces]
    sorrow_total = [x[1] for x in list_of_faces]
    anger_total = [x[2] for x in list_of_faces]
    surprise_total = [x[3] for x in list_of_faces]
    if (len(list_of_faces) == 1):
        var_total = 0
    else:
        var_total = sum([variance(x) for x in [joy_total, sorrow_total, anger_total, surprise_total]])

    #print(var_total)
    if (var_total > 2.6):
        playlistid = dict_x['y2k']
    elif (mean(joy_total) == 4):
        playlistid = dict_x['Good Vibes']
    elif (mean(sorrow_total) == 4):
        playlistid = dict_x['sad girl starter pack']
    else:
        playlistid = dict_x['park hangs']

    return playlistid

#print(match_emotion([[4,0,0,0]]))
import json
import random
def generate_similar_playlist(seed_id):
    a = SpotifyClient("Hack2022")
    pl = a.get_playlist(seed_id)['tracks']['items']
    # pl = a.get_playlist(seed_id)['tracks']['items']
    #print(pl)
    seeds = []
    index = 0
    while len(seeds) < 5:
        num = randint(0, 49)
        if num not in seeds:
            seeds.append(num)
        
    #print(seeds)
    #print(json.dumps(pl, indent=4))
    seed_songs = [pl[x]["track"]["id"] for x in seeds if x < len(pl)]
    seed_urls = [pl[x]["track"]["external_urls"]["spotify"] for x in seeds if x < len(pl)]
    print(seed_urls)
    b = ",".join(seed_songs)
    #print(b)
    c = a.get_recommendations(s_track=b, num=20, random = False)["tracks"]
    final_urls = [x['external_urls']["spotify"] for x in c]
    #print(final_urls)
    url = seed_urls + final_urls
    return url
generate_similar_playlist('37i9dQZF1DWYBO1MoTDhZI')
#a.get_playlist('37i9dQZF1DWYBO1MoTDhZI')


def closest_color(color_hex_tuple):
    color_s = ["green", "blue", "red", "yellow", "purple", "orange", "pink", "grey", "black", "white", "brown" ]
    colors = [(0, 153,0), (0, 0, 255), (255,0 ,0), (255 ,255, 0), (102, 0, 204), 
    (255, 128, 0), (255,153,255), (192, 192,192), (0, 0,0), (255, 255,255), (102,51,0)]
    diffs = [color_diff(color_hex_tuple, x) for x in colors]
    min_diff = min(diffs)
    min_index = diffs.index(min_diff)
    print("closest color is " + color_s[min_index])
    return color_s[min_index]
    


def color_diff(hex_1_tup, hex_2_tup):
    r_delt = abs(hex_1_tup[0] - hex_2_tup[0])
    g_delt = abs(hex_1_tup[1] - hex_2_tup[1])
    b_delt = abs(hex_1_tup[2] - hex_2_tup[2])
    r_mean = (hex_1_tup[0] + hex_2_tup[0])/2
    diff = math.sqrt(((2 + r_mean/256) * (r_delt) ** 2 )+ 4 * (g_delt **2) + (2 + (255-r_mean)/256) * (b_delt ** 2))
    return diff

closest_color((155,150,142))

'''
red = anger => 5O12S9z3O8dEhHWt3bPbxm//
orange = playfulness => ("Feelin' Myself", '37i9dQZF1DX6GwdWRQMQpq')
yellow = happy/sunny days => ('Wake Up Happy', '37i9dQZF1DX0UrRvztWcAU')
green = envy => 6IbaCObGskjZMODeeMc6K9//
blue = sad => ('Life Sucks', '37i9dQZF1DX3YSRoSdA634')
purple = royalty =>('Villain Mode', '37i9dQZF1DX3R7OWWGN4gH')
pink = love => 4cJ8qUzt5CSTE9XN5uK2z2//
brown = warm, cocoa, => '(Your Favorite Coffeehouse', '37i9dQZF1DX6ziVCJnEm59')
gray = melancholy, neutral =>  '5zxPaDEr4XtbvaZdUYN4FJ' //
black = mournfulness, emo => 68uGYIL2ZyiJxheYDOPWa5 //
white = cold, shock =>3nv1mjzIyACjKJ4Wy0RWYg //
'''
def match_color(color_hex_tuple):
    playlists = {"red": "5O12S9z3O8dEhHWt3bPbxm", "orange":"37i9dQZF1DX6GwdWRQMQpq", 
    "yellow":"37i9dQZF1DX0UrRvztWcAU", "green":"6IbaCObGskjZMODeeMc6K9",
    "blue":"37i9dQZF1DX3YSRoSdA634", "purple":'37i9dQZF1DX3R7OWWGN4gH',
    "pink": "4cJ8qUzt5CSTE9XN5uK2z2", "brown":'37i9dQZF1DX6ziVCJnEm59', 
    "grey":'5zxPaDEr4XtbvaZdUYN4FJ',
    "black": "68uGYIL2ZyiJxheYDOPWa5", "white": "3nv1mjzIyACjKJ4Wy0RWYg"}
    col = closest_color(color_hex_tuple)
    pl = playlists[col]
    print(pl)
    return pl

#generate_similar_playlist(match_color((155,150,142)))
generate_similar_playlist("5zxPaDEr4XtbvaZdUYN4FJ")
