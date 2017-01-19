
# coding: utf-8

# In[2]:

import numpy
import matplotlib.pyplot
import glob



filenames = sorted(glob.glob('data/data/weather*.csv'))

def analyse (filename):
    data = numpy.loadtxt(fname=filename,delimiter=',')
    
    if numpy.max (data,axis=0)[0] == 0 and numpy.max (data,axis=0)[20] ==20:
        print ("Suspicious looking maxima")
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print ("Minima add up to zero")
    else:
        print ("Data looks ok")
        

    fig = matplotlib.pyplot.figure(figsize=(10.0,3.0))

    #create placeholders for plots
    subplot1 = fig.add_subplot (1,3,1)
    subplot2 = fig.add_subplot (1,3,2)
    subplot3 = fig.add_subplot (1,3,3)

    subplot1.set_ylabel('max')
    subplot1.plot(numpy.max(data, axis=0))

    subplot2.set_ylabel('average')
    subplot2.plot(numpy.mean(data, axis=0))

    subplot3.set_ylabel('min')
    subplot3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    if outfile is None:
        matplotlib.pyplot.show()
    else:
        matplotlib.pyplot.savefig(outfile)
    


# In[1]:

def detect_problems (filename, outfile=None):
    """
    This is to detect problem in the data
    """
    data = numpy.loadtxt(fname=filename,delimiter=',')
    
    if numpy.max (data,axis=0)[0] == 0 and numpy.max (data,axis=0)[20] ==20:
        print ("Suspicious looking maxima")
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print ("Minima add up to zero")
    else:
        print ("Data looks ok")


# In[45]:

if __name__ == "__main__":
    
    print("Running ", sys.argv[0])

    print (sys.argv[1])
    analyse (sys.argv[1], outfile=sys.argv[2])
    detect_problems(sys.argv[1])





