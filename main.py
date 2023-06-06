import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from pygfunction import *
from secret_details import *
import webbrowser

'''
This just opens the spreadsheet. Non-critical.
'''
YOUR_SPREADSHEET_URL = spreadsheet
if input("Open the spreadsheet? Y/N\n") == "Y":
    webbrowser.open(YOUR_SPREADSHEET_URL, new=2)

'''
took the below from here, includes credentials and id instructions:
https://stackoverflow.com/questions/62917910/how-can-i-export-pandas-dataframe-to-google-sheets-using-python
'''
# pygsheets
service_file_path = "credentials.json"
spreadsheet_id = spreadsheet_id

'''
Create a Spotify developer app and copy in the two below details
'''
# spotipy
client_id = client_id
client_secret = client_secret

sheet_name = input("Enter artist name: \n")


'''
This part searches spotify for the information.
'''
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

d = []

total = 1 # temporary variable
offset = 0

def millisecond_convert(ms):
    millis = ms
    millis = int(millis)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    return ("%d:%d" % (minutes, seconds))

while offset < total:
    results = sp.search(q=f"artist:{sheet_name}",  type='track', offset=offset, limit=50)
    #print(results)
    total = results['tracks']['total']
    offset += 50 # increase the offset
    for idx, track in enumerate(results['tracks']['items']):
        d.append (
            {
                'Track' : track['name'],
                'Album' : track['album']['name'],
                'Artist' : track['artists'][0]['name'],
                'Release Date' : track['album']['release_date'],
                'Track Number' : track['track_number'],
                'Popularity' : track['popularity'],
                'Track Number' : track['track_number'],
                'Duration': millisecond_convert(track['duration_ms']),
                'Audio Preview URL' : track['preview_url'],
                'Track URL' : track['external_urls']['spotify']
            }
        )

'''
Adds the spotify information to dataframe
'''
df = pd.DataFrame(d)
# df.to_csv(r'output.csv', index=None, header=True)


'''
writes the dataframe to a new google sheet.
'''
write_to_gsheet(service_file_path=service_file_path, spreadsheet_id=spreadsheet_id, sheet_name=sheet_name, data_df=df)