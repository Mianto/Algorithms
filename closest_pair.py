from operator import itemgetter
import math

def closest(Pointlist,n):
    PointlistX = list()
    PointlistY = list()

    for point in Pointlist:
        PointlistX.append(point)
        PointlistY.append(point)

    PointlistX = sorted(PointlistX,key = itemgetter(0))
    PointlistY = sorted(PointlistY, key = itemgetter(1))

    return closestpair(PointlistX,PointlistY,n)

def closestpair(Px,Py,n):

    if n <= 3:
        return BruteForce(Px,n)

    mid = n/2
    Pointmid = Px[mid]

    Pyright = list()
    Pyleft = list()

    for i in range(0,n):
        if Pointmid[0] > Py[i][0]:
            Pyleft.append(Py[i])
        else :
            Pyright.append(Py[i])

    dl = closestpair(Px,Pyleft,n-mid)
    dr = closestpair(Px[mid:],Pyright,mid)
    d = min(dl,dr)

    strip = list()
    #populate strip using Py such that abs(Pointmid[0] - Py[i][0])< d
    for i in range (n):
        if abs(Pointmid[0] - Py[i][0]) < d :
            strip.append(Py[i])
    return min(d,stripcase(strip,len(strip),d))

def stripcase(A,size,d):
    minimum = d
    print d
    for i in range(size):
        for j in range (i+1,size):
            if dist(A[i],A[j]) < minimum:
                minimum = dist(A[i],A[j])

    return minimum

def BruteForce(Point,n):
    mini = 10000
    for i in range(n):
        for j in range(i+1,n):
            if dist(Point[i],Point[j]) < mini :
                mini = dist(Point[i],Point[j])
    return mini

def dist(Point1,Point2):
    d = ((Point1[0] - Point2[0])**2) + ((Point1[1] - Point2[1])**2)
    print d
    return math.sqrt(d)

def main():
    Point = [(2,3),(12, 30),(40, 50),(5,1),(12,10),(3,4)]
    size = len(Point)

    print 'The minimum distance between the points : ' + str(closest(Point,size))

if __name__ =="__main__":
    main()
