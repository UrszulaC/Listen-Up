1. Listen Up!

Listen Up! was build with intention to play music based on keyword search.

2. Project Description

Our music application uses Spotify Api to fetch requested tracks, albums and similar songs. 
Listen Up! contains also music visualiser displaying track's features as a polar diagram.  

We have used:

Streamlit for building modern dashboard with easy change of settings depending on personal choice.
Python for back - end logic - easy to understand and change if needed. 
Spotify API chosen as a one of the biggest streaming platforms letting to play music straight from a browser with minimal implementation.
Spotify also enabled us to create visualiser and song recommendation with sheer number of available features.

3. Next steps:
- adding more options to play the music 
- creating account and login feature 
- implementing playlists and recommended playlists 
- karaoke function

4. Installing and Executing:
Installing:

To run the program locally please install dependencies via

    pip install 

Dependencies: 
- streamlit 
- pandas 
- spotipy
- requests
- base64
- matplotlib
- numpy 
- seaborn
- PIL 

Executing program:

After virtual environment being created please write the below command into the terminal:

    streamlit run main.py

A new browser window should automatically open. You should be able to see the streamlit interface. 
You now can simply enter a song into the interface and press search.

5. Dashboard

<img width="1414" alt="Dashboard 1" src="https://user-images.githubusercontent.com/63776006/184504366-6efbf66b-98fa-4cd7-bdee-1b4e3ff90099.png">
<img width="1414" alt="Dashboard 2" src="https://user-images.githubusercontent.com/63776006/184504370-be6aa6b5-5bcd-4838-b07f-b8fab83c30ee.png">

6. Credits/Resources

https://dev.to/mxdws/using-python-with-the-spotify-api-1d02

https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

https://towardsdatascience.com/a-music-taste-analysis-using-spotify-api-and-python-e52d186db5fc

https://developer.spotify.com/community/showcase/spotify-audio-analysis/

https://www.theverge.com/platform/amp/tldr/2018/2/5/16974194/spotify-recommendation-algorithm-playlist-hack-nelson

https://towardsdatascience.com/interactive-machine-learning-and-data-visualization-with-streamlit-7108c5032144

https://medium.com/deep-learning-turkey/build-your-own-spotify-playlist-of-best-playlist-recommendations-fc9ebe92826a

https://github.com/tgel0/spotify-data

7. MIT License

Copyright (c) 2022 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
