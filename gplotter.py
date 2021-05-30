from subprocess import PIPE, Popen
import pexpect
import os


animate_script = read_script_file(os.getcwd()+"/Plotter/animate")


class gPlot():
    def __init__(self):
        gnuplot_c = pexpect.spawn("gnuplot")

    def send_gnuplot_msg(self,msg_str):
        gnuplot_c.send(msg_str+"\n")
        gnuplot_c.expect("gnuplot>")
        #print(str(gnuplot_c.before))
        
    def read_script_file(self,filePath):
        with open(filePath, 'r') as file:
            return file.read()
    
    def run_script(self,script_filepath):
        send_gnuplot_msg("l '"+str(script_filepath)+"'")
         
        if(gnuplot_c.expect(["expecting filename","gnuplot>"])==0)#Maybe should be == expecting filename"
            raise FileNotFoundError("Filename invalid")
        else:
            return
    
    
    def animate_lattice(self):
        """
            Animates lattice stored in data.dat file as a matrix (i.e. 2x2 array stored with each 
            position being the vlue at that position (i.e. form saved by np.savetxt())
        """
        try:
            while(True): #gnuplot can crash animation occasionally, this restarts the animation if it hangs
                send_gnuplot_msg(animate_script)
                gnuplot_c.expect("gnuplot>")
        except KeyboardInterrupt:
                gnuplot_c.expect("gnuplot>")
    


    def run_gnuplot_command(self,cmd):
        self.send_gnuplot_msg(cmd+"\n")
        self.gnuplot_c.expect("gnuplot>")





"""
print(str(gnuplot_c.before))

send_gnuplot_msg("set terminal x11 noraise\n")
send_gnuplot_msg("set datafile separator whitespace\n")
send_gnuplot_msg("set view map\n")
send_gnuplot_msg("set pm3d map")

send_gnuplot_msg("p 'data.dat' matrix w image\n")
send_gnuplot_msg("pause 1\n")
"""
input()












#p = Popen(["python3","helloWorld.py"],stdin=PIPE,stdout=PIPE,stderr=PIPE)
#
#while(True):
# print(p.communicate(b"HelloWorld"))
#Only allows single communication?? 
