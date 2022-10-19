from queue import Empty
import subprocess
subprocess.run(["javac", "ChatApp/window.java","ChatApp/ChatTag.java"])
#subprocess.run(["dir",""])

proc = subprocess.Popen(["java", "ChatApp/window"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
while(True):
    output = proc.stdout.readline()
    if len(output) > 0:
        print(output.rstrip().decode("utf-8"))
    # Receive data from java code
    proc.communicate()
    poll = proc.poll()
    if poll is not None:
        print(poll)
        exit()
    
    