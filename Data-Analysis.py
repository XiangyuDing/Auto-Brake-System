import matplotlib.pyplot as plt
import numpy as np


##def dataAnalysis(filename):
fr = open('samples.txt')
arrayOfLines = fr.readlines()
n = len(arrayOfLines)
success, fail = 0, 0
for line in arrayOfLines:
    line = line.strip()
    listFromLine = line.split('\t')
    if int(listFromLine[-1]) == 0:
        success += 1
    else:
        fail += 1
print(success,fail)
plt.figure(figsize=(6,6))
labels = [u'Success',u'Fail']
sizes = [success,fail]
colors = ['green','red']
explode = (0.01,0.01)
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%',
                      shadow = False,
                      startangle =90,
                      pctdistance = 0.6)
plt.axis('equal')
plt.show()


def linear_regression(filename):
    pass

def polycurvefit(filename):
    pass


##if __name__ == "__main__":
    
