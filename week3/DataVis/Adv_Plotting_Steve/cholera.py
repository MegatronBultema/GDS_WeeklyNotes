import pandas as pd
import re
import folium
from geopy.distance import vincenty

df = pd.read_csv('data/Cholera.csv')
df['strip'] = df['geometry'].map(lambda x: x.lstrip('<Point><coordinates>').rstrip('</coordinates></Point>'))
df['longitude'] = df['strip'].map(lambda x: float(x.split(',')[0]))
df['latitude'] = df['strip'].map(lambda x: float(x.split(',')[1]))

wells = df[df['count'] == -999]
deaths = df[df['count'] != -999]

first_map = folium.Map(location = [51.513, -0.137], zoom_start = 16, tiles = "Stamen Terrain")
vin = 1000
colormap = {1:'#FFFF00', 2:'#FF9900', 3: '#66FFFF', 4: '#6600CC', 5:'#0066CC', 6: '#009999', 0: '#FF6600', 7: '#000000'}
for row in range(len(deaths)):
    long_row = deaths.iloc[row,3]
    lat_row = deaths.iloc[row,4]
    size = deaths.iloc[row,0]
    vin = 1000
    closest = -1
    for r in range(len(wells)-1):
        long_well = wells.iloc[r,3]
        lat_well = wells.iloc[r,4]
        t = vincenty((lat_row, long_row), (lat_well, long_well)).miles
        #print(r, t)
        if t < vin:
            vin = t
            #print(t,vin, r)
            closest = r
        else:
            pass
        folium.CircleMarker(location = [lat_row, long_row], color = colormap[closest], fill_color=colormap[closest], radius=size, popup = '{} deaths' .format(size)).add_to(first_map)



for row in range(len(wells)):
    long_row = wells.iloc[row,3]
    lat_row = wells.iloc[row,4]
    colormap = {1:'#FFFF00', 2:'#FF9900', 3: '#66FFFF', 4: '#6600CC', 5:'#0066CC', 6: '#009999', 0: '#FF6600', 7: '#000000'}
    folium.CircleMarker(location = [lat_row, long_row], color = '#000000', fill_color=colormap[row], radius=5, popup = 'well: {}, {}'.format(lat_row, long_row)).add_to(first_map)


def change():
    '''**3.)** Let's reframe this problem. Rather than plot the points where the fatalities occurred, plot a `CircleMarker` for each pump that is sized based on the total of closest fatalities.'''

    df = pd.read_csv('data/Cholera.csv')
    df['strip'] = df['geometry'].map(lambda x: x.lstrip('<Point><coordinates>').rstrip('</coordinates></Point>'))
    df['longitude'] = df['strip'].map(lambda x: float(x.split(',')[0]))
    df['latitude'] = df['strip'].map(lambda x: float(x.split(',')[1]))

    wells = df[df['count'] == -999]
    deaths = df[df['count'] != -999]

    first_map = folium.Map(location = [51.513, -0.137], zoom_start = 16, tiles = "Stamen Terrain")
    vin = 1000
    colormap = {1:'#FFFF00', 2:'#FF9900', 3: '#66FFFF', 4: '#6600CC', 5:'#0066CC', 6: '#009999', 0: '#FF6600', 7: '#000000'}
    for row in range(len(deaths)):
        long_row = deaths.iloc[row,3]
        lat_row = deaths.iloc[row,4]
        size = deaths.iloc[row,0]
        vin = 1000
        closest = -1
        
        for r in range(len(wells)-1):
            long_well = wells.iloc[r,3]
            lat_well = wells.iloc[r,4]
            t = vincenty((lat_row, long_row), (lat_well, long_well)).miles
            #print(r, t)
            if t < vin:
                vin = t
                #print(t,vin, r)
                closest = r
            else:
                pass
            folium.CircleMarker(location = [lat_row, long_row], color = colormap[closest], fill_color=colormap[closest], radius=size, popup = '{} deaths' .format(size)).add_to(first_map)



#folium.Marker(location = [51.513418, -0.13793], popup ='test').add_to(first_map)
first_map.save("Cholera.html")
