from subprocess import PIPE, Popen
import pexpect

def send_gnuplot_msg(msg_str):
    gnuplot_c.send(msg_str+"\n")
    gnuplot_c.expect("gnuplot>")
    print(str(gnuplot_c.before))
    
def read_script_file(filePath):
    with open(filePath, 'r') as file:
        return file.read()

animate_script = read_script_file("animate")
print(animate_script)

gnuplot_c = pexpect.spawn("gnuplot")
gnuplot_c.expect("gnuplot>")
send_gnuplot_msg(animate_script)
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
