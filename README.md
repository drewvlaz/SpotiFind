# SpotiFind --

Drew Vlasnik, Maggie Zhao :alien:, Theo Ko, Jesse Ssengonzi

## Description of project:

## APIs used:
- [Spotify Web API] [https://developer.spotify.com/documentation/web-api/]
- [Cloud Vision API] [https://cloud.google.com/vision]

## Significance:

## Explanation, in broad strokes if necessary, of how you aim to make this data come alive.

The user will be able to switch between two modes:
- Emotion/Color - Depending on whether or not the Vision AI can detect faces in the image, we can generate a playlist based on the moods of the users in the photo, or a playlist based on the colors.
- Labels - The Vision AI will classify any objects it sees in the image, and we generate a list of songs with those labels in the song title.


We hope to explore and provoke the following questions:


## Explanation of feature utilization:

## Our visualization


## Launch Instructions
1. Create and open your virtual environment

```
$ python3 -m venv venv
$ . venv/bin/activate
```

2. Clone the Spotifind repository

```
$ git clone https://github.com/drewvlaz/SpotiFind.git
```

3. Install dependencies in [requirements.txt] (/requirements.txt)

```
pip install -r requirements.txt
```
3.5. Run the React app
```
cd spotifind-frontend
npm install
npm start
```

4. Run the flask app
```
$ cd Spotifind
$ flask run
```

4. Open the flask app in your favorite browser!
  Go to http://127.0.0.1:5000/
