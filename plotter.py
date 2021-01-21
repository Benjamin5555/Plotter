import matplotlib.pyplot as plt
import numpy as np
import itertools
import matplotlib.animation as animate 
import functools

class Animate:

    @staticmethod
    def oop_func_wrapper(func,func_self):
        return functools.partial(func,func_self) 


    @classmethod
    def live_animate(self,animate_func,nSeconds=15,fps=25):
                # First set up the figure, the axis, and the plot element we want to animate
        fig = plt.figure()
        #ax = plt.axes()#xlim=(0, 10), ylim=(0, 10))
        #ax.axis('scaled')
        #ax.set_xlim(0, 2*math.pi)
        #ax.set_ylim(-1.1, 1.1)
        #ax.set_xlabel('x (rads)')
        #ax.set_ylabel('sin(x)')
        #line, = ax.plot([], [], lw=2)
        #a=np.random.random((5,5))
        #im=plt.imshow(a,interpolation='none')

        anim = animate.FuncAnimation(
                               fig,
                               animate_func,
                               frames = nSeconds * fps,
                               interval = 1000 / fps, # in ms
                               )

        anim.save('test_anim.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])


    
    # animation function.  This is called sequentially
    """
    def animate_func(i):
        a=im.get_array()
        a=a*np.exp(-0.001*i)    # exponential decay of the values
        im.set_array(a)
        return [im]
    """



class Plotting:
    
    marker = itertools.cycle((',', '+', '.', 'o', '*')) 
   
    @classmethod
    def colour_map_gen(self,npArray):
        """
        Takes some form of numpy array and formats it into a colour map depending on value at array
        index
        """
        return plt.imshow(npArray)

    @classmethod
    def colour_map_show(self,npArray):
        """
        Takes some form of numpy array and formats it into a colour map depending on value at array
        index
        """
        self.colour_map_gen(npArray)
        plt.show()


    #Scatter and line plot functions
    @classmethod
    def scatter(self,x_data,y_datas,x_title=None,y_title=None,y_labels=None,title=None):
        i = 0 # Counter used for labelling
        
        for y in y_datas: #PLot each Y value against T
            if(not (y_labels ==None)):
                plt.scatter(x_data,y,label = str(y_labels[i]),marker=next(self.marker))
            else:
                plt.scatter(x_data,y,marker=next(self.marker))
            i= i+1 # Increment label counter
    
        # Set axes, titles and legend
        plt.title(title)
    
       
        plt.ylabel(y_title)
        plt.xlabel(x_title)
    
        plt.legend()
        plt.show()
     
    
    @classmethod
    def line(x_data,y_datas,x_title=None,y_title=None,y_labels=None,title=None):
        i = 0 # Counter used for labelling
        
        for y in y_datas: #PLot each Y value against T
            if(not (y_labels ==None)):
                plt.plot(x_data,y,label = str(y_labels[i]),marker=next(self.marker))
            else:
                plt.plot(x_data,y,marker=next(self.marker))
            i= i+1 # Increment label counter
    
        # Set axes, titles and legend
        plt.title(title)
    
       
        plt.ylabel(y_title)
        plt.xlabel(x_title)
    
        plt.legend()
        plt.show()
         
    @classmethod
    def hist(x_data,bins=None,NumBins=None,x_title=None,y_title=None,y_labels=None,title=None):
        """
            Creates histogram from some data set
            returns histogram_data(freq), bins to be unpacked
        """
        
        if(NumBins==None and bins==None):
            bins = len(x_data)
        elif(bins==None):
            bins = NumBins
        
        ns,bins,*_ = plt.hist(x_data,bins, alpha=0.75)    
    
        # Set axes, titles and legend
        plt.title(title)
       
        plt.ylabel(y_title)
        plt.xlabel(x_title)
        #plt.set_ylim([x_data])
        #plt.legend()
        plt.show()
        return ns,bins
    