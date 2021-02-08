from main import DataIngestion

f = open("/Users/henrik/windstat_small.csv")
s = f.read()
di = DataIngestion()
print(di.parse_method(s))