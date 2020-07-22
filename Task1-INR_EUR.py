import json
import matplotlib.pyplot as plot
from datetime import datetime

with open('data.json') as file:
    data=json.load(file)
fetch_rate=dict()
for i in data['rates']:
    dt=datetime.strptime(i,'%Y-%m-%d').date()
    if(dt.month==1 and dt.year==2019):
        fetch_rate[dt.day]=data['rates'][str(i)]['INR']
        
pg=sorted(fetch_rate.items())
dt,rates=zip(*pg)
plot.style.use('dark_background')
plot.step(dt,rates,color='lime')
plot.xlabel('Dates of Jan 2019')
plot.xticks()
plot.ylabel('Rates')
plot.title('Rate of INR against EUR.')
plot.get_current_fig_manager().window.state('zoomed')
plot.show()