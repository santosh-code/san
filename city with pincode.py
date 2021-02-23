import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
df = pd.read_csv("F:\Sa.csv")
rows=[]
for x in df.Address4:
      location = geolocator.geocode(x)
      rows.append(location.address)
a = pd.DataFrame(rows, columns=["amber"])
