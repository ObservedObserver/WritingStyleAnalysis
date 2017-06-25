import re
import math, json, time
#Book = Novel(novel)
#novel is the location of your novel, example: /home/books/war_peace.txt
class Novel():
    # story = []
    # nameSet = {}
    # relationalMatrix = []
    # stat = {}
    # tf = {}
    def __init__(self, article):
        self.article = open(article, "r")
        self.story = self.article.readlines()
        self.nameSet = {}
        self.relationalMatrix = []
        self.stat = {}
        self.tf = {}
    #To close the novel file.
    def close_novel(self):
        return self.article.close()

    #Return basic statics of the novel.
    def statics(self):
        if len(self.stat) != 0:
            return self.stat
        else:
            self.stat = {"wordCount": 0, "characterCount": 0, "punct": 0}
            for line in self.story:
                self.stat["wordCount"] += len(re.findall(r'[A-Za-z0-9]+',line))
                self.stat["characterCount"] += len(line)
                self.stat["punct"] += len(re.findall(r'[,.;:""!]',line))
            return self.stat

    #Return the tf dictionary of the novel.
    def term_frenquency(self):
        if len(self.tf) != 0:
            return self.tf
        else:
            for line in self.story:
                words = re.findall(r'[A-Za-z]+',line)
                for word in words:
                    if self.tf.__contains__(word):
                        self.tf[word] += 1
                    else:
                        self.tf[word] = 1
            delList = []
            print(len(self.tf))
            Total = self.statics()["wordCount"]
            for word in self.tf:
                if self.tf[word] < 10:
                    delList.append(word)
                self.tf[word] /= Total
            for word in delList:
                self.tf.pop(word)
            return self.tf

    #Return an apperance distribution of a name.
    def time_density(self, name):
        pattern = []
        patterns = name.split(' ')
        if len(patterns) == 1:
            pattern = re.compile(name)
        elif len(patterns) == 2:
            tmp = patterns[0]+'|'+patterns[1]+'|'+(patterns[0]+' '+patterns[1])
            pattern = re.compile(tmp)
        personTD = []
        i = 0
        pos = 0
        for line in self.story:
            #Compression
            if i % 100 == 0:
                personTD.append(0)
            result = re.findall(pattern, line)
            personTD[i//100] += len(result)
            i += 1
        return personTD

    #Return a list of cahracters in the novel.
    def characters(self):
        if len(self.nameSet) != 0:
            return self.nameSet
        else:
            namePattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+')
            timeDensity = []
            i = 0
            #Count apperance of names in the story:
            for line in self.story:
                timeDensity.append(0)
                result = namePattern.findall(line)
                for name in result:
                    if self.nameSet.__contains__(name):
                        self.nameSet[name]+=1
                    else:
                        self.nameSet[name]=1
                timeDensity[i] += len(result)
                i += 1
            #Get a delete list to delete those names with low frenquency:
            delList = []
            for name in self.nameSet:
                if self.nameSet[name] < 20:
                    delList.append(name)
                elif re.match(r'(The [A-Z][a-z]+)|(.*God)', name) is not None:
                    delList.append(name)
            #Delete the names:
            for name in delList:
                self.nameSet.pop(name)

            return self.nameSet

    #A grading function used to calcute the relationship between two name.
    def grades(self, name1, name2):
        Name1 = self.time_density(name1)
        Name2 = self.time_density(name2)
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

    #Return a relationship matrix contains the grades between different pair of name.
    def relational_matrix(self):
        if len(self.nameSet) == 0:
            self.characters()
        i = 0
        for (key1,val1) in self.nameSet.items():
            #gradeList[key1] = 0
            #time cost per cycle:0.48s
            for (key2,val2) in self.nameSet.items():
                self.relationalMatrix.append({})
                self.relationalMatrix[i]["name1"] = key1
                self.relationalMatrix[i]["name2"] = key2
                self.relationalMatrix[i]["grade"] = self.grades(key1, key2)
                i += 1
                #gradeList[key1] += grades(key1,key2)
        return self.relationalMatrix

#Examples:
# war_peace = Novel("war_peace.txt")
# print(len(war_peace.term_frenquency()))
# print(war_peace.time_density("Prince Vasili"))
# print(war_peace.characters())
# print(war_peace.statics())
# print(war_peace.relational_matrix())
# print(war_peace.close_novel())
# Novel("test.txt").term_frenquency()
#
# Novel("war_peace.txt").term_frenquency()
