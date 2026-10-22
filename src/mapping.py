import folium
from folium.plugins import HeatMap

def generate_heatmap(df):
    center_lat = df['Center_Lat'].mean() if not df.empty else 41.8781
    center_lon = df['Center_Lon'].mean() if not df.empty else -87.6298
    
    base_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11, tiles='OpenStreetMap')
    
    heat_data = [[row['Center_Lat'], row['Center_Lon'], row['Risk_Score']] for index, row in df.iterrows()]
    HeatMap(heat_data, radius=35, blur=20, max_zoom=1).add_to(base_map)
    
    for index, row in df.iterrows():
        allocated = int(row['Allocated_Officers'])
        if allocated > 0:
            folium.CircleMarker(
                location=[row['Center_Lat'], row['Center_Lon']],
                radius=allocated * 2,
                color='#00ff00',
                fill=True,
                fill_color='#00ff00',
                fill_opacity=0.7,
                tooltip=f"<b>District:</b> {row['District']}<br><b>Risk:</b> {row['Risk_Score']}<br><b>Deployed:</b> {allocated}"
            ).add_to(base_map)
            
    return base_map._repr_html_()