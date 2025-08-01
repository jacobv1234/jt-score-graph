from json import loads
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.colors as mcol
from matplotlib.collections import LineCollection
import matplotlib as mpl
from datetime import datetime
from random import choice

from timesortedscore import Score

# load data
scores = []
with open('data.json','r') as f:
    data = loads(f.read())
    for score in data:
        scores.append(Score(score))

# do calculations on data
scores.sort()

possibleUsers = []
for score in scores:
    if score.name not in possibleUsers:
        possibleUsers.append(score.name)

# assign colours
colours = {}
used_colours = []
css_colour_list = list(mcol.CSS4_COLORS.keys())
for user in possibleUsers:
    # pick a colour
    while True:
        col = choice(css_colour_list)
        if col not in used_colours:
            break
    used_colours.append(col)
    colours[user] = col

print(colours)

# create graph data
x = [md.date2num(datetime.fromtimestamp(score.time/1000)) for score in scores]
y = [score.score for score in scores]
c = [colours[score.name] for score in scores]
sc = []

# line needs to be split into individual sections to show colours properly
segments = []
for i in range(len(x) - 2):
    # straight line segments
    #segments.append([(x[i], y[i]), (x[i+1], y[i+1])])
    #sc.append(c[i+1])

    # square line segments
    segments.append([(x[i], y[i]), (x[i+1], y[i])])
    sc.append(c[i])
    segments.append([(x[i+1], y[i]), (x[i+1], y[i+1])])
    sc.append(c[i+1])

lines = LineCollection(segments, colors = sc, linewidth=2)



fig, ax = plt.subplots()
dateformat = md.DateFormatter('%d/%m @ %H:%M:%S')
ax.xaxis.set_major_formatter(dateformat)

# scatter plot for individual points per colour so the legend works
for user in possibleUsers:
    ux = [md.date2num(datetime.fromtimestamp(score.time/1000)) for score in scores if score.name == user]
    uy = [score.score for score in scores if score.name == user]
    c = colours[user]
    ax.scatter(ux,uy,25,c,label=user)

plt.legend()

# add line graph
ax.add_collection(lines)
ax.autoscale()

ax.set_xlabel('Time')
ax.set_ylabel('Score')
ax.set_title('Top Scores', size=20)
plt.xticks(rotation=15)

plt.show()