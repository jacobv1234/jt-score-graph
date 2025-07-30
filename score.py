class Score:
    def __init__(self, info):
        self.name = info['name']
        self.score = info['score']
        self.time = info['time']
    
    def calc_colour(self, min, max):
        shade = (self.time - min) / (max-min)
        self.col = (shade, shade, shade)
    
    def __eq__(self, other):
        return self.score == other.score
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __ne__(self, other):
        return self.score != other.score
    
    def __str__(self):
        return self.name + ' scored ' + str(self.score) + ' at time ' + str(self.time)