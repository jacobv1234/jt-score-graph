from json import loads
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime

from score import Score

# load data
scores = []
with open('data.json','r') as f:
    data = loads(f.read())
    for score in data:
        scores.append(Score(score))

scores.sort(reverse=True)
mintime = scores[0].time
maxtime = scores[0].time
for score in scores:
    if score.time < mintime:
        mintime = score.time
    if score.time > maxtime:
        maxtime = score.time
    
[score.calc_colour(mintime,maxtime) for score in scores]

plt.bar(
    [score.name + '\n' + datetime.strftime(datetime.fromtimestamp(score.time/1000),"%d/%m@%H:%M:%S") for score in scores],
    [score.score for score in scores],
    color = [score.col for score in scores],
    edgecolor = 'black'
)

plt.show()