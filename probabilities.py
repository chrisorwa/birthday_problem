
from __future__ import division

#import required library
import pandas as pd
import numpy as np 
import math
import decimal
import os

#set working directory
os.chdir('C:/Users/iHub Research/Desktop/Projects/Birthday Problem/Birthday/Processed')

#load data
df = pd.read_csv('combined.csv')
birth = df['Birthday']

#combination function
def nPr(n,r):
    return math.factorial(n)/ math.factorial(n-r)

results = []
i = 1
while i < len(birth):
	set = birth[1:i]
	l  = len(np.unique(set))
	try:
		p = 1-nPr(365,l)/365**l
		r = [p,i]
		results.append(r)
	except Exception:
		pass
	i = i+1

#convert to data frame
re = pd.DataFrame(results)
print re

#write to file
re.to_csv('paradox.csv')
