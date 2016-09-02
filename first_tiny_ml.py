#page 55

import scipy as sp
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
print data[:10]
print data.shape

#split the 2 columns into separate arrays
x = data[:,0]
y = data[:,1]

#find out how many nan values are in y
print sp.sum(sp.isnan(y))

#remove the values that are nan in y
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

# a standard scatter plot
import matplotlib.pyplot as plt 
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
#where and what to put in the axis
plt.xticks([w*7*24 for w in range(10)],
	['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
#plt.show()		#<------ uncomment

#basic error function
def error(f, x, y):
	return sp.sum((f(x)-y)**2)
	pass

#1. assumming the underying model is a straight line

#given x and y, finds the order 1 function that minimises error
#get fitten model function + extras (full is True)
fp1, residuals, rank, sv, rcond = sp.polyfit(x,y,1, full=True)

print "Model parameters: %s" % fp1
#best line fit : f(x) =    2.59619213 * x + 989.02487106

#create a model function from the parameters
f1 = sp.poly1d(fp1)
print '1st degree error: %f' % error(f1, x, y)

fx = sp.linspace(0,x[-1], 1000)
#generate x-values for plotting

#plt.plot(fx, f1(fx), linewidth=4)
#plt.legend(["d=%i" % f1.order], loc = "upper left")
plt.plot(fx, f1(fx), linewidth=3, label="d=%i"%f1.order)

#plt.show()		#<------ uncomment

#2. more advanced stuff; degree 2

f2p = sp.polyfit(x, y, 2)
print f2p
f2 = sp.poly1d(f2p)
print '2nd degree error: %f' % error (f2, x, y)
plt.plot(fx, f2(fx), linewidth=2, label="d=%i"%f2.order)
#plt.legend(["d=%i" % f2.order], loc = "upper left")


# with 3, 10, 50

for i in ([3,10, 100]):
	f3p = sp.polyfit(x, y, i)
	#print f3p
	f3 = sp.poly1d(f3p)
	print '%dnd degree error: %f' % (i, error (f3, x, y))
	plt.plot(fx, f3(fx), linewidth=2, label="d=%i"%i)
	pass


plt.legend(loc = "upper left")
plt.show()		#<------ uncomment

#page 68