from geopy.geocoders import Nominatim
import pandas as pd


geolocator = Nominatim(user_agent = 'user', timeout=3)

csv = 'companies.csv'
df = pd.read_csv(csv)

df["loc"] = df['Company Address'].apply(geolocator.geocode)
df["point"]= df["loc"].apply(lambda loc: tuple(loc.point) if loc else None)
df[['lat', 'lon', 'altitude']] = pd.DataFrame(df['point'].to_list(), index=df.index)

df.to_csv('out.csv')