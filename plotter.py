import matplotlib.pyplot as plt
import numpy as np
import itertools
import matplotlib.animation as animate 
import functools
import sys
import pickle

class FileRead:
    @classmethod
    def load_fixed_width_raw_data(self,filePath,width):
        """
        File to read into a 2D list, where data has size of width bytes (a char is a byte)
        Really could be a more efficient system
        """
        f = open(filePath,"r")
        data = []
        for line in f:
            row =[]
            for i in range(0,len(line),width):
                for j in range(0,width):
                    try:
                        row.append(int(line[i+j]))
                    except:
                        break #Where \n reached
            data.append(row)
            
        return data

    
    #@classmethod
    #def file_read_animate(fileObj):



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

        anim.save('anim.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

        
    # animation function.  This is called sequentially
    """
    def animate_func(i):
        a=im.get_array()
        a=a*np.exp(-0.001*i)    # exponential decay of the values
        im.set_array(a)
        return [im]
    """
    @staticmethod
    def _loadNext(filePath):
        with open(filePath, 'rb') as f:
            yield pickle.load(f)


    @staticmethod
    def animateFunc(i,fileName):
        print("HELLO")
        with open(fileName,'rb') as f:
            a = pickle.loads(f)
        
        return Plotting.colour_map_gen(a)
    @staticmethod
    def CmapFromNPBs(filePath):
        fig = plt.figure()
        with open(filePath, 'rb') as f:
            anim = animate.FuncAnimation(
                               fig,
                               Animate.animateFunc,
                               frames = 1000 , 
                               fargs = (filePath,),
                               interval=1000/10
                               )

            anim.save('anim.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
    
    #@staticmethod
    #def _loadNext(filePath):
    #    while(True):
    #        try:
    #            print(pickle.load(f))
    #            #yield pickle.load(f)
    #        except:
    #            return

    #@staticmethod
    #def animateFunc(i):
    #    return Plotting.colour_map_gen(i)

    #@staticmethod
    #def CmapFromNPBs(filePath):
    #    fig = plt.figure()
    #    with open('test.file', 'rb') as f:

    #        anim = animate.FuncAnimation(
    #                           fig,
    #                           Animate.animateFunc,
    #                           frames =1000 , 
    #                           interval=1000/10
    #                           )

    #    anim.save('anim.mp4', fps=10, extra_args=['-vcodec', 'libx264'])




class Plotting:
    
    marker = itertools.cycle((',', '+', '.', 'o', '*')) 
   
    @classmethod
    def colour_map_gen(self,npArray,fileName=None,*args, bar=False ):
        """
        Takes some form of numpy array and formats it into a colour map depending on value at array
        index
        """
        
        im = plt.imshow(npArray)
        if (bar):
            fig, ax = plt.subplots()
            fig.colorbar(im)
        #im = plt.imshow() was here
        plt.title(fileName)
        
        return im



    @classmethod
    def colour_map_show(self,npArray,fileName=None,*args,bar=False):
        """
        Takes some form of numpy array and formats it into a colour map depending on value at array
        index
        """
        
        self.colour_map_gen(npArray,fileName)
        if(not fileName==None):
            plt.savefig(fileName)

        plt.show()
        #Should have some form of close plot here 
        

    #Scatter and line plot functions
    @classmethod
    def scatter(self,x_data,y_datas,*args,x_title=None,y_title=None,y_labels=None,title=None):
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
        plt.savefig(title)
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


if __name__ == '__main__':
    if (len(sys.argv)==1):
        print("USAGE: plotType, dataFilePath, dataType, dataWidt\n plotType: cmap, cmapAnimate\ndataType: fixedLength (dataWidth also has to be specified); npbs for an array of numpybinarys for use in animation")
    else:
        if (sys.argv[3] == "fixedLength"):
            data = FileRead.load_fixed_width_raw_data(sys.argv[2],int(sys.argv[4]))
        elif(sys.argv[3]=="npbs"):
            if(sys.argv[1]=="cmapAnimate"):
                Animate.CmapFromNPBs(sys.argv[2])
        else:
            print("See usage for command line usable") 
        
        if (sys.argv[1] == "cmap"):
            Plotting.colour_map_show(data,sys.argv[2]+".png",bar=True)




