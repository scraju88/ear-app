# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:37:43 2018

@author: SCRAJU88
"""
import numpy as np
import os
import glob
import matplotlib.pyplot as plt

patient = str(33)
os.chdir('C:/Users/SCRAJU88/Documents/Main Docs/Life Stuff/Product Ideas/Pediabyte/Smartphone Reflectometry/Data/Test Data/Patient ' + patient + '/iPhone');
        
bottomLeft = sorted(glob.glob('*lb*.dat')) #enables you to find files with a particular tag line *the asterisk denotes that there are values before or after it
bottomRight = sorted(glob.glob('*rb*.dat'))
control = sorted(glob.glob('*cb*.dat'))

##Define Variables 
bl_gt, bl_gt2 = 1, 2
br_gt, br_gt2 = 1, 2
c_gt, c_gt2 = 0, 0

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

counterctrim = 0 # see below- need to just get maximum size of array first because it might be more efficient rather than appending each time

for i in range(0,counterc+1): #this is to get maximum size of array, because it goes up to but does not include counterc unless you put +1
   if np.mean(d['C{0}'.format(i)]) > (ctotalmean - ctotalstd*2) and np.mean(d['C{0}'.format(i)]) < (ctotalmean + ctotalstd*2):
      counterctrim += 1 #if the array fits the above parameters, then increase the count to create a max array below

carraytrim = np.zeros(shape=(counterctrim,2600)) #creates max array
carraygt = np.zeros(shape=(1,counterctrim)) # creates max array for the ground truth
carraygt.fill(c_gt) #fills ground truth with above variable
carraygt2 = np.zeros(shape=(1,counterctrim)) # creates max array for the ground truth
carraygt2.fill(c_gt2) #fills ground truth with above variable


appendcounter = 0
for i in range(0,counterc+1):
   if np.mean(d['C{0}'.format(i)]) > (ctotalmean - ctotalstd*2) and np.mean(d['C{0}'.format(i)]) < (ctotalmean + ctotalstd*2):
       carraytrim[appendcounter] = d['C{0}'.format(i)] #can't use i here because if it is greater than i, then it won't be able to identify the right location. Need append counter.
       appendcounter += 1  


t = np.arange(1800,4400,1)
controlfinalmean = carraytrim.mean(0)
weights = 1/controlfinalmean

carraytrim = carraytrim*weights


    
print (counterc)





#### BOTTOM LEFT

for l in bottomLeft: 
    counterl += 1
    d["L{0}".format(counterl)] = np.genfromtxt(fname=l, delimiter=",", dtype="int") 
    larray[counterl] = d['L{0}'.format(counterl)]

lmean = larray.mean(1) # produces mean values across rows of carray, thus producing 18 values in a vertical array
ltotalmean = lmean.mean(0) #gets mean 
ltotalstd = lmean.std(0) # gets total STD   

counterltrim = 0

for i in range(0,counterl+1): #this is to get maximum size of array, because it goes up to but does not include counterc unless you put +1
   if np.mean(d['L{0}'.format(i)]) > (ltotalmean - ltotalstd*2) and np.mean(d['L{0}'.format(i)]) < (ltotalmean + ltotalstd*2):
      counterltrim += 1

larraytrim = np.zeros(shape=(counterltrim,2600)) #creates max array
larraygt = np.zeros(shape=(1,counterltrim)) # creates max array for the ground truth
larraygt.fill(bl_gt) #fills ground truth with above variable
larraygt2 = np.zeros(shape=(1,counterltrim)) # creates max array for the ground truth
larraygt2.fill(bl_gt2) #fills ground truth with above variable


appendcounter = 0
for i in range(0,counterl+1):
   if np.mean(d['L{0}'.format(i)]) > (ltotalmean - ltotalstd*2) and np.mean(d['L{0}'.format(i)]) < (ltotalmean + ltotalstd*2):
       larraytrim[appendcounter] = (d['L{0}'.format(i)] * weights) #can't use i here because if it is greater than i, then it won't be able to identify the right location. Need append counter.
       appendcounter += 1  




     
    
    
    
    
 ### BOTTOM RIGHT
 
for r in bottomRight: 
    counterr += 1
    d["R{0}".format(counterr)] = np.genfromtxt(fname=r, delimiter=",", dtype="int") 
    rarray[counterr] = d['R{0}'.format(counterr)]

rmean = rarray.mean(1) # produces mean values across rows of carray, thus producing 18 values in a vertical array
rtotalmean = rmean.mean(0) #gets mean 
rtotalstd = rmean.std(0) # gets total STD   

counterrtrim = 0

for i in range(0,counterr+1): #this is to get maximum size of array, because it goes up to but does not include counterc unless you put +1
   if np.mean(d['R{0}'.format(i)]) > (rtotalmean - rtotalstd*2) and np.mean(d['R{0}'.format(i)]) < (rtotalmean + rtotalstd*2):
      counterrtrim += 1

rarraytrim = np.zeros(shape=(counterrtrim,2600)) #creates max array
rarraygt = np.zeros(shape=(1,counterrtrim)) # creates max array for the ground truth
rarraygt.fill(br_gt) #fills ground truth with above variable
rarraygt2 = np.zeros(shape=(1,counterrtrim)) # creates max array for the ground truth
rarraygt2.fill(br_gt2) #fills ground truth with above variable


appendcounter = 0
for i in range(0,counterr+1):
   if np.mean(d['R{0}'.format(i)]) > (rtotalmean - rtotalstd*2) and np.mean(d['R{0}'.format(i)]) < (rtotalmean + rtotalstd*2):
       rarraytrim[appendcounter] = (d['R{0}'.format(i)] * weights) #can't use i here because if it is greater than i, then it won't be able to identify the right location. Need append counter.
       appendcounter += 1  


#Output

os.chdir('C:/Users/SCRAJU88/Documents/Main Docs/Life Stuff/Product Ideas/Pediabyte/Smartphone Reflectometry/Data/Test Data/Machine Learning Dat Files');


filenumber = patient + 'Iphone'
np.savetxt('Control' + filenumber + ' features.dat', carraytrim)
np.savetxt('Control' + filenumber + ' diagnosis.dat', carraygt)
np.savetxt('Control' + filenumber + ' diagnosis2.dat', carraygt2)

np.savetxt('Left' + filenumber + ' features.dat', larraytrim)
np.savetxt('Left' + filenumber + ' diagnosis.dat', larraygt)
np.savetxt('Left' + filenumber + ' diagnosis2.dat', larraygt2)


np.savetxt('Right' + filenumber + ' features.dat', rarraytrim)
np.savetxt('Right' + filenumber + ' diagnosis.dat', rarraygt)
np.savetxt('Right' + filenumber + ' diagnosis2.dat', rarraygt2)

