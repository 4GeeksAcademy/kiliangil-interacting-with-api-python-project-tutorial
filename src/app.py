import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()


# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

#Paso 5. Realizar solicitudes API
artist_uri = "1rTUwYS38LkQTlT2fhikch"
results = spotify.artist_top_tracks(artist_uri, country='ES')['tracks']
print(results)

#Paso 6. Transofrmar a pandas DataFrame 
df = pd.DataFrame(results)
df["duration_min_sec"] = df["duration_ms"].apply(
    lambda x: f"{x//60000}:{int((x%60000)/1000):02d}")
df = df[["name", "popularity", "duration_min_sec"]]
df

#Paso 7. Analizar relación estadística
df_sorted = df.sort_values(by='duration_min_sec', ascending=False)
plt.figure(figsize=(5, 3))
plt.scatter(df_sorted['duration_min_sec'], df_sorted['popularity'])
plt.title('Relación duración vs popularidad')
plt.xlabel('Duración (min:sec)'); plt.ylabel('popularity')
plt.tight_layout(); plt.show()

Podríamos decir que a mayor duración mayor popularidad aunque la cantidad de datos usados no es suficientemente robusta como para ser representativay poder afirmar esta relación.