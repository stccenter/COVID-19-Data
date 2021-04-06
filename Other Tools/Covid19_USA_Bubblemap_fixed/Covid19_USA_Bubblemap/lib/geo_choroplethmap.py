import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import numpy as np
import plotly as py

def choroplethmap(df, legend_data, date, image_path):
    fig = go.Figure()
    
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df['lon'],
        lat = df['lat'],
        marker = dict(size = df[date]/200, color = "lightcoral", line_color='darkred',
                      line_width=0.5, sizemode = 'area', opacity=0.6), #opacity=0.8
        showlegend = False))
    
    # 5 bubbles in Legend
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = legend_data['lon'],
        lat = legend_data['lat'],
        marker = dict(size = legend_data[date]/200, color = 'lightcoral', line_color='darkred',
                      line_width=0.5, sizemode = 'area', opacity=0.6), #opacity=0.8
        showlegend = False))
    
    fig.update_layout(
        title=dict(text='Number of Confirmed Cases (' + str(date) + ')', x=0.48),
        titlefont=dict(family="Times New Roman", color="#000000", size=30),        
        width=1200,
        height=700,
        geo=dict(scope='usa', showsubunits=True, subunitcolor='white', subunitwidth=0.5),#equirectangular/natural earth
        font=dict(family='Times New Roman', size = 14),
        annotations = [dict( x=0.25, y=-0.1, xref='paper', yref='paper',
                            text='Data collection, process and visualization by NSF Spatiotemporal Innovation Center.',
                            showarrow = False)])
        
    fig.write_image(image_path + str(date) + ".jpg")


#nested circles
#data = [10,100,250]
#labels = list(['1,000','50,000','60,000'])
#nested_circles(data, labels=labels, cmap="copper", textkw=dict(fontsize=14))    
def nested_circles(data, labels=None, c=None, ax=None, cmap=None, norm=None, textkw={}):    
    ax = ax or plt.gca()
    data = np.array(data)
    R = np.sqrt(data/data.max())
    p = [plt.Circle((0,r), radius=r) for r in R[::-1]]
    arr = data[::-1] if c is None else np.array(c[::-1])
    col = PatchCollection(p, cmap=cmap, norm=norm, array=arr)

    ax.add_collection(col)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.autoscale()

    if labels is not None:
        kw = dict(color="white", va="center", ha="center")
        kw.update(textkw)
        ax.text(0, R[0], labels[0], **kw)
        for i in range(1, len(R)):
            ax.text(0, R[i]+R[i-1], labels[i], **kw)
    plt.show()