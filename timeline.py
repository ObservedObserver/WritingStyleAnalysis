import re
import math
class TimeLine():
    story = ""
    pattern = None

    def __init__(self, story, pattern):
        self.story=story
        patterns = pattern.split(' ')
        if len(patterns) == 1:
            self.pattern = re.compile(pattern)
        elif len(patterns) == 2:
            tmp = patterns[0]+'|'+patterns[1]+'|'+(patterns[0]+' '+patterns[1])
            self.pattern = re.compile(tmp)

    def time_density(self):
        personTD = []
        i = 0
        pos = 0
        for line in self.story:
            #Compression
            if i % 100 == 0:
                personTD.append(0)
            result = re.findall(self.pattern, line)
            personTD[i//100] += len(result)
            i += 1
        return personTD
    # def density(self):
    #     result = re.findall(self.pattern, "Prince Vasili \n Prince Vasili Prince Vasili")
    #     return len(result)
def grades(name1, name2):
    Name1 = TimeLine(story, name1).time_density()
    Name2 = TimeLine(story, name2).time_density()
    Name1Len = 0
    Name2Len = 0
    #Ans = Name1.time_density()
    Ans = 0
    i = 0
    Len = len(Name1)
    while i < Len:
        Ans += Name1[i]*Name2[i]
        Name1Len += (Name1[i]*Name1[i])
        Name2Len += (Name2[i]*Name2[i])
        i += 1
    return Ans/(math.sqrt(Name1Len)*math.sqrt(Name2Len))
article = open("war_peace.txt","r")
story = article.readlines()
nameSet = {}
namePattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+')
timeDensity = []
i = 0
for line in story:
    timeDensity.append(0)
    result = namePattern.findall(line)
    for name in result:
        if nameSet.__contains__(name):
            nameSet[name]+=1
        else:
            nameSet[name]=1
    timeDensity[i] += len(result)
    i += 1

#Prince Vasili
Prince = TimeLine(story, "Prince Vasili")
print(Prince.time_density())
print(len(Prince.time_density()))
# print(Prince.density())

print(grades("Anna Mikhdylovna","Prince Vasili"))

article.close()
