class RuleSet(object):
    def __init__(self, data):
        self.ruleInteractions = data
    def generateLanguageIndex(self, fileName):
        langCatalog = {}
        for R in self.ruleInteractions:
            L = R.language
            if L not in langCatalog:
                langCatalog[L] = 0
            langCatalog[L] += 1
        sorted = langCatalog.keys()
        sorted.sort()
        for L in sorted:
            print("Language: %s has %d records" % (L, langCatalog[L]))
        
    def generateInteractionIndex(self, fileName):
        intCatalog = {}
        for RT in self.ruleInteractions:
            I = RT.opacityType
            if I not in intCatalog:
                intCatalog[I] = 0
            intCatalog[I] += 1

    def toList(self):
        result = []
        for i in self.ruleInteractions:
            result.append(i.toMap())
        return result

class RuleInteraction(object):
    def __init__(self):
        self.language = None
        self.name = None
        self.opacityType = None
        self.references = None
        self.freeVariation = None
        self.comments = None
        self.altAnalyses = None
    def loadData(self, row):
        for i in range(36 - len(row)):
            row.append("")
        self.language = row[3]
        self.name = row[4]
        self.opacityType = row[5]
        self.references = row[6]
        self.processes = []
        self.processes.append(Process(row[7], row[8], row[14], row[15], row[16]))
        self.processes.append(Process(row[17], row[18], row[24], row[25], row[26]))
        self.freeVariation = row[29]
        self.comments = row[31]
        self.altAnalyses = row[32]
    def toString(self):
        result = 'Language: ' + self.language + '\nName: ' + self.name + '\nInteraction Type: ' + self.opacityType + '\nReferences: ' + self.references + "\nProcess 1: \n" + self.processes[0].toString() + '\nProcess 2: \n' + self.processes[1].toString() + '\nFree Variation? ' + self.freeVariation + '\nComments: ' + self.comments + '\nAlternate Analyses: ' + self.altAnalyses
        return result
    def toMap(self):
        result = {}
        result["language"] = self.language
        result["name"] = self.name
        result["opacityType"] = self.opacityType
        result["references"] = self.references
        result["processes"] = []
        for p in self.processes:
            result["processes"].append(p.toMap())
        result["freeVariation"] = self.freeVariation
        result["comments"] = self.comments
        result["altAnalyses"] = self.altAnalyses
        return result
    
class Process(object):
    def __init__(self, desc, ruleType, lim, prod, add):
        self.description = desc
        self.ruleType = ruleType
        self.limitations = lim
        self.productivity = prod
        self.additionalInt = add
    def toString(self):
        result = 'Rule Description: ' + self.description + '\nRule Type: ' + self.ruleType + '\nLimitations: ' + self.limitations + '\nProductivity: ' + self.productivity + '\nAdditional Interactions: ' + self.additionalInt
        return result
    def toMap(self):
        result = {}
        result["description"] = self.description
        result["ruleType"] = self.ruleType
        result["limitations"] = self.limitations
        result["productivity"] = self.productivity
        result["additionalInt"] = self.additionalInt
        return result;
        
        
