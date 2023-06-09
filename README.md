# Deep-Dive-Spreadsheet

This project arose because I felt Spotify's search wasn't comprehensive enough, the interface doesn't give you all the information, and artist pages often don't show you songs they've submitted to compilation albums or other projects. I'm a huge music lover and sometimes if I like an artist I want to find and check out even their most obscure songs.

It does two things, you enter an artist name and it searches for every song of theirs on Spotify, returns them and then sends them to a Google Sheets doc with all the often missing information displayed such as a popularity rating, release date, a link to the song, a preview.

It also then creates a new playlist, filters the songs to remove artists with similar names that may have appeared in the search, then adds the songs to the new playlist.

In this way, you can quickly create a Discography playlist for all your favourite artists.

#Step 1 - Spotify

1. Create Spotify developer account
2. Create Spotify app
3. Collect Client ID and Client Secret
4. Add to main.py


#Step 2 - Google API

1. Click Sheets API | Google Developers
2. Create new project under Dashboard (provide relevant project name and other required information)
3. Go to Credentials
4. Click on “Create Credentials” and Choose “Service Account”. Fill in all required information viz. Service account name, id, description et. al.
5. Go to Step 2 and 3 and Click on “Done”
6. Click on your service account and Go to “Keys”
7. Click on “Add Key”, Choose “Create New Key” and Select “Json”. Your Service Json File will be downloaded. Put this under your repo folder and path to this file is your service_file_path.
8. In that Json, “client_email” key can be found.
9. Create a new google spreadsheet. Note the url of the spreadsheet.
10. Provide an Editor access to the spreadsheet to "client_email" (step 8) and Keep this service json file while running your python code.
11. Note: add json file to .gitignore without fail.
12. From url (e.g. https://docs.google.com/spreadsheets/d/1E5gTTkuLTs4rhkZAB8vvGMx7MH008HjW7YOjIOvKYJ1/) extract part between /d/ and / (e.g. 1E5gTTkuLTs4rhkZAB8vvGMx7MH008HjW7YOjIOvKYJ1 in this case) which is your spreadsheet_id.
13. sheet_name is the name of the tab in google spreadsheet. By default it is "Sheet1" (unless you have modified it.

#Step 3 - Add full spreadsheet URL to YOUR_SPREADSHEET_URL
