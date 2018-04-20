import matplotlib.pyplot as plt
import numpy as np
import collections
from random import randint

def safety(crashAll):
    # initializing crash dataset
    success, fail = 0, 0
    for crash in crashAll:
        if crash == 1:
            fail += 1
        else:
            success += 1
    # plot the dataset
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


def timeDistribution(timeAll):
    # initializing time dataset
    timeDist = {}
    for time in timeAll:
        if time not in timeDist:
            timeDist[time] = 1
        else:
            timeDist[time] += 1
    # plot the dataset
    X = list(timeDist.keys())
    Y = list(timeDist.values())
    for x, y in zip(X, Y):
        plt.text(x, y + 0.1, '%d' % y, ha='center', va='bottom')
    plt.bar(X,Y,0.08,facecolor="#9999ff",edgecolor="white")  
    plt.xlabel("Time")  
    plt.ylabel("Frequency")  
    plt.title("Braking Time Distribution")
    plt.show()


def linear_regression(speedAll,sample):
    # initializing distance dataset
    time_point = []
    for speed in speedAll:
        time_point.append(np.arange(0.0, (1/8)*len(speed), (1/8)).tolist())
    # plot the dataset
    X = np.array(time_point[sample])
    Y = np.array(speedAll[sample])
    f1 = np.polyfit(X, Y, 1)
    p1 = np.poly1d(f1)
    print(p1)
    yvals = p1(X)
    plot1 = plt.scatter(X, Y, label="Real-time Speed")
    plot2 = plt.plot(X, yvals, 'r', label="Linear Regression")
    plt.xlabel("Time(s)")
    plt.ylabel("Speed(m/s)")
    plt.legend(loc=1)
    plt.title("Curve-fitting: Speed")
    plt.show()


def polycurvefit(distanceAll,sample):
    # initializing distance dataset
    time_point = []
    time_points = []
    dis_points = []
    for distance in distanceAll:
        time_point.append(np.arange(0.0, (1/8)*len(distance), (1/8)).tolist())
    # plot the dataset
    X = np.array(time_point[sample])
    Y = np.array(distanceAll[sample])
    f1 = np.polyfit(X, Y, 2)
    p1 = np.poly1d(f1)
    print(p1)
    yvals = p1(X)
    plot1 = plt.scatter(X, Y, label="Real-time Distance")
    plot2 = plt.plot(X, yvals, 'r', label="Curve fitting")
    plt.xlabel("Time(s)")
    plt.ylabel("Distance(m)")
    plt.legend(loc=1)
    plt.title("Curve-fitting: Distance")
    plt.show()


if __name__ == "__main__":

    # Load and read the dataset
    fr = open('samples3.txt')
    arrayOfLines = fr.readlines()
    n = len(arrayOfLines)
    distanceAll = []
    speedAll = []
    brakeforceAll = []
    timeAll = []
    crashAll = []
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        distance = [float(dis) for dis in listFromLine[0].split(' ')]
        distanceAll.append(distance)
        speed = [float(v) for v in listFromLine[1].split(' ')]
        speedAll.append(speed)
        brakeforce = [float(fb) for fb in listFromLine[2].split(' ')]
        brakeforceAll.append(brakeforce)
        time = float(listFromLine[3])
        timeAll.append(time)
        crash = int(listFromLine[4])
        crashAll.append(crash)
    sample = randint(0,n)

    safety(crashAll) # Plot the safety results in dataset
    timeDistribution(timeAll) # Plot the time distribution results in dataset
    linear_regression(speedAll,sample) # Plot the linear regression of speed
    polycurvefit(distanceAll,sample) # Plot the curvefit of distance
