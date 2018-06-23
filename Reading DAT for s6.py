# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:37:43 2018

@author: SCRAJU88
"""
import numpy as np
import os
import glob
import matplotlib.pyplot as plt

os.chdir('C:/Users/SCRAJU88/Documents/Main Docs/Life Stuff/Product Ideas/Pediabyte/Smartphone Reflectometry/Tests/Test Data/Patient 17/s6');
        
bottomLeft = sorted(glob.glob('*bottomLeft*.dat')) #enables you to find files with a particular tag line *the asterisk denotes that there are values before or after it
bottomRight = sorted(glob.glob('*bottomRight*.dat'))
control = sorted(glob.glob('*control*.dat'))

counterl = int(-1) #sets counter for each variable and rewrites fname with counter
counterr = int(-1)
counterc = int(-1)
d = {}

larray = np.zeros(shape=(len(bottomLeft),2600)) #starts by creating an array of zeros of a particular size, then you add other arrays
rarray = np.zeros(shape=(len(bottomRight),2600)) #starts by creating an array of zeros of a particular size, then you add other arrays
carray = np.zeros(shape=(len(control),2600)) #starts by creating an array of zeros of a particular size, then you add other arrays



for c in control:
    # print(c) (print the files)
    counterc += 1
    d["C{0}".format(counterc)] = np.genfromtxt(fname=c, delimiter=",", dtype="int") # don't forget to change fname to variable c #extracts data from filename into integers 
    # print(len(d['C{0}'.format(counterc)])) (print the length of these files)
    #d creates a dictionary. format modifies whatever is in the {}
    carray[counterc] = d['C{0}'.format(counterc)] #adds to the array during each iteration
    

cmean = carray.mean(1) # produces mean values across rows of carray, thus producing 18 values in a vertical array
ctotalmean = cmean.mean(0) #gets mean 
ctotalstd = cmean.std(0) # gets total STD

counterctrim = 0

for i in range(0,counterc+1): #this is to get maximum size of array, because it goes up to but does not include counterc unless you put +1
   if np.mean(d['C{0}'.format(i)]) > (ctotalmean - ctotalstd*2) and np.mean(d['C{0}'.format(i)]) < (ctotalmean + ctotalstd*2):
      counterctrim += 1

carraytrim = np.zeros(shape=(counterctrim,2600)) #creates max array

appendcounter = 0
for i in range(0,counterc+1):
   if np.mean(d['C{0}'.format(i)]) > (ctotalmean - ctotalstd*2) and np.mean(d['C{0}'.format(i)]) < (ctotalmean + ctotalstd*2):
       carraytrim[appendcounter] = d['C{0}'.format(i)] #can't use i here because if it is greater than i, then it won't be able to identify the right location. Need append counter.
       appendcounter += 1  

t = np.arange(1800,4400,1)
controlfinalmean = carraytrim.mean(0)
weights = 1/controlfinalmean
    
print (counterc)

for i in range(0,counterc+1):
   if np.mean(d['C{0}'.format(i)]) > (ctotalmean - ctotalstd*2) and np.mean(d['C{0}'.format(i)]) < (ctotalmean + ctotalstd*2):
       newfile = d['C{0}'.format(i)] * weights
       newname = 'C{0}'.format(i)
       fig, ax = plt.subplots()
       ax.plot(t,newfile)
       fig.savefig(newname + '.png')


#### BOTTOM LEFT

for l in bottomLeft: 
    counterl += 1
    d["L{0}".format(counterl)] = np.genfromtxt(fname=l, delimiter=",", dtype="int") 
    larray[counterl] = d['L{0}'.format(counterl)]

lmean = larray.mean(1) # produces mean values across rows of carray, thus producing 18 values in a vertical array
ltotalmean = lmean.mean(0) #gets mean 
ltotalstd = lmean.std(0) # gets total STD   

for i in range(0,counterl+1):
   if np.mean(d['L{0}'.format(i)]) > (ltotalmean - ltotalstd*2) and np.mean(d['L{0}'.format(i)]) < (ltotalmean + ltotalstd*2):
       newfile = d['L{0}'.format(i)] * weights
       newname = 'L{0}'.format(i)
       fig, ax = plt.subplots()
       ax.plot(t,newfile)
       fig.savefig(newname + '.png')

 ### BOTTOM RIGHT
 
for r in bottomRight: 
    counterr += 1
    d["R{0}".format(counterr)] = np.genfromtxt(fname=r, delimiter=",", dtype="int") 
    rarray[counterr] = d['R{0}'.format(counterr)]

rmean = rarray.mean(1) # produces mean values across rows of carray, thus producing 18 values in a vertical array
rtotalmean = rmean.mean(0) #gets mean 
rtotalstd = rmean.std(0) # gets total STD   

for i in range(0,counterr+1):
   if np.mean(d['R{0}'.format(i)]) > (rtotalmean - rtotalstd*2) and np.mean(d['R{0}'.format(i)]) < (rtotalmean + rtotalstd*2):
       newfile = d['R{0}'.format(i)] * weights
       newname = 'R{0}'.format(i)
       fig, ax = plt.subplots()
       ax.plot(t,newfile)
       
       



    
#for r in bottomRight:
 #   print(r)
  #  d["BR{0}".format(counterr)] = np.genfromtxt(fname=r, delimiter=",", dtype="int") #don't forget to change fname to variable r
   # print(len(d['BR{0}'.format(counterr)]))
    #counterr += 1

    
#print (counterl)
#print (counterr)
