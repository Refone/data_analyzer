#!/usr/bin/env python
# encoding: utf-8

#import numpy as np
#import statsmodels.api as sm
#import matplotlib.pyplot as plt
from __future__ import division
import sys

def main():
    n = int(sys.argv[3])
    p = int(sys.argv[4])

    try :
        f1 = open(sys.argv[1])
        f2 = open(sys.argv[2])
    except IOError:
        print "Open data file failed."
        return

    n-=1

    data1 = []
    f1.readline()
    for i in range(0, n):
        data1.append(int(f1.readline()))
    data1.sort()

    data2 = []
    f2.readline()
    for i in range(0, n):
        data2.append(int(f2.readline()))
    data2.sort()
    #for d in data:
    #    print d
        #data = map(float, data)
        #cdf_plot(data, f, 100)

    left = min(data1[0], data2[0])
    right = max(data1[n-1], data2[n-1])
    dis = right - left

    fence = []
    for i in range(0,p+1):
        fence.append(float(left + i*(dis/p)))

    rate1 = []
    rate2 = []
    for i in range(0,p+1):
        r = 0
        while r<n and data1[r] < fence[i] :
            r+=1
        rate1.append(float(r/n))
        r = 0
        while r<n and data2[r] < fence[i] :
            r+=1
        rate2.append(float(r/n))


    for i in range(0,p+1):
        print ("%8.4f  %3.2f  %3.2f"%(fence[i], rate1[i]*100, rate2[i]*100))

if __name__ == '__main__':
    main()
