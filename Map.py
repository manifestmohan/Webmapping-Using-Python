import folium
import pandas

volcano = pandas.read_csv("Volcanoes.txt")
lat=list(volcano["LAT"])
lon=list(volcano["LON"])
elev=list(volcano["ELEV"])

map=folium.Map(location=[38.58,-99],zoom_start=10,tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Volcanoes")

def color_selector(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <=  elevation < 3000:
        return "orange"
    else:
        return "red"

for i,j,k in zip(lat,lon,elev):
    #fg.add_child(folium.Marker(location=[i,j],popup=str(k)+"m",icon=folium.Icon(color=color_selector(k))))
    fgv.add_child(folium.CircleMarker(location=[i,j],radius=10,fill_color=color_selector(k),popup=str(k)+"m",))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else'orange'
if 10000000 <= x ['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")
