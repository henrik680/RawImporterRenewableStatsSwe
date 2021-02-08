from RenewableEnergyFacilityApplicationStatisticsSweden import *
from main import *

def test():
    cols = []
    #for x in RenewSweStatSchema()['fields']:
    #    cols.append(x['name'])
    #return cols


def testCols():
    cols = []
    for x in g_schema['fields']:
        cols.append(x['name'])
    return cols

def allCols(cols):
    s = ''
    for c in cols:
        s += c + '\t'
    return s

#print(test())
print(allCols(testCols()))