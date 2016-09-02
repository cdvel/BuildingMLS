import numpy as np
print 'numpy version:', np.version.full_version

a = np.array([0,1,2,3,4,5])
print 'array dim:', a.ndim
print 'array shape:', a.shape

print 'reshaping array...'
b = a.reshape(3,2)
print b, b.shape; print "\n";

b[1][0] = 77
print b; print a; print "\n";
#numpy avoids copies whenever possible

# a totally independent copy
c = a.reshape(3,2).copy()
c[0][0] = -99

print a; print c; print "\n";

#changes propagate to individual elements
print 'propagate changes to each element... x2, ^2'
z = np.array([0,1,2,3,4,5])
print z*2; print z**2; print "\n";

#------indexes-------
print a;
#arrays as indexes
print a[np.array([2,3,4])]

print a>4 #locating
print a[a>4] #filtering out
a[a>4] = 4 #trimming
print a
print a.clip(0,4) #trimming via function clip
print "\n"

#------Nan-------

c = np.array([1,2, np.NAN, 3,4])
print c

print np.isnan(c)
print c[~np.isnan(c)]
print np.mean(c[~np.isnan(c)])
print "\n"

#---Runtime comparisons--

import timeit as tim

normal_py_sec = tim.timeit('sum(x*x for x in xrange(1000))', number=10000)
naive_np_sec  = tim.timeit('sum(na*na)', setup = "import numpy as np; na=np.arange(1000)", number = 10000)
good_np_sec   = tim.timeit('na.dot(na)', setup = "import numpy as np; na=np.arange(1000)", number = 10000)

print "Normal Python: %f sec" %normal_py_sec
print "Naive Numpy  : %f sec" %naive_np_sec
print "Normal Numpy : %f sec" %good_np_sec

# move into numpy only to use optimised functions, but less flexibility (1 datatype)
print "\n"
a = np.array([1,2,3])
print a.dtype
a5 = np.array(['1', 'stringy'])
print a5
print a5.dtype
a6 = np.array([1, "sting", set ([1,2,3])])
print a6, a6.dtype

import scipy, numpy
print scipy.version.full_version
print scipy.dot is numpy.dot

