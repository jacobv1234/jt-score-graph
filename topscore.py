from json import loads
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib as mpl
from datetime import datetime

from score import Score

# load data
scores = []
with open('data.json','r') as f:
    data = loads(f.read())
    for score in data:
        scores.append(Score(score))

# do calculations on data
scores.sort()
mintime = scores[0].time
maxtime = scores[0].time
for score in scores:
    if score.time < mintime:
        mintime = score.time
    if score.time > maxtime:
        maxtime = score.time
    
[score.calc_colour(mintime,maxtime) for score in scores]

# create graph
fig, ax = plt.subplots()
dateformat = md.DateFormatter('%d/%m @ %H:%M:%S')
ax.xaxis.set_major_formatter(dateformat)
ax.plot([md.date2num(datetime.fromtimestamp(score.time/1000)) for score in scores],
        [score.score for score in scores])

ax.set_xlabel('Time')
ax.set_ylabel('Score')
ax.set_title('Top Scores', size=20)
plt.xticks(rotation=15)

plt.show()