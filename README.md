# SpotiFind --

Drew Vlasnik, Maggie Zhao :alien:, Theo Ko, Jesse Ssengonzi

## Description of project:

It is said that a picture is worth 1000 words. It is well known that some feelings and emotions can't easily be captured by prose. But what about music?  Nostalgia, joy, sorrow, heartbreak; all these emotions have been expressed eloquently by the musical geniuses of our time. We were inspired by the Spotify machine learning session and Google cloud's vision AI to try to combine music with pictures to allow a user to immortalize memories in a unique way. What if we could listen to music and feel the feelings associated with a memory?

Spotifind turns an image into a playlist based on emotion and key objects in an easy four step process.
Step 1: Login to your spotify account
Step 2: upload your favorite image (or any image at all)
Step 3: De-select any objects that you don't want to influence your playlist
Step 4: Recieve a playlist of 20 songs to enjoy! this playlist is also directly added to your music with the image as the playlist cover!


## APIs used:
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Cloud Vision API](https://cloud.google.com/vision)

## Significance:

## Explanation, in broad strokes if necessary, of how you aim to make this data come alive.

The user will be able to switch between two modes:
- Emotion/Color - Depending on whether or not the Vision AI can detect faces in the image, we can generate a playlist based on the moods of the users in the photo, or a playlist based on the colors.
- Labels - The Vision AI will classify any objects it sees in the image, and we generate a list of songs with those labels in the song title.


We hope to explore and provoke the following questions:


## Explanation of feature utilization:

SpotiFind uses three features Google Cloud Vision Detected: FACE_DETECTION, IMAGE_PROPERTIES, LABEL_DETECTION. 
(i) FACE_DETECTION returns a list of strings that describe likeliness of four emotions - Joy, Sorrow, Anger, Surprise. If there are multiple faces, hence a combiination of emotion likelihoods are detected, then they are weighted using variance and mean. The weighted result is taken into account and returns a corresponding keyword for song recommendations. 

(ii) IMAGE_PROPERTIES returns a list of strings that 

(iii) LABEL_DETECTION returns a list of strings that 

## Our visualization

On the frontend, it takes 

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
