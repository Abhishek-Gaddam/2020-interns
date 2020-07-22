import json
from dateutil import parser
import matplotlib.pyplot as plot 
with open('data.json') as file:
    data=json.load(file)    
date=[]
INR=[]
GBP=[]
t1=parser.parse('2019-01-01')
t2=parser.parse('2019-01-31')
for i in data['rates']:
    t3=parser.parse(i)
    if t3<=t2 and t3>=t1:
        date.append(i)
        INR.append(data['rates'][i]['INR'])
        GBP.append(data['rates'][i]['GBP'])
ma=list(zip(date,INR,GBP))
rt=sorted(ma,key=lambda x:x[0])
date=[]
INR=[]
GBP=[]
date,INR,GBP=zip(*rt)
plot.style.use('dark_background')
plot.xlabel('Rates of Jan 2019')
plot.xticks(rotation=333)
plot.ylabel('Jan 2019')
plot.title('INR and GBP exchange rates against EUR')
plot.bar(date,INR,color='0.45',label='INR',width=0.3)
plot.bar(date,GBP,color='g',label='GBP',width=0.3)
plot.legend(loc='best')
plot.get_current_fig_manager().window.state('zoomed')
plot.show()