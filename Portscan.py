import sys
import socket
import errno
from socket import error as socket_error

def scan():
    if( len(sys.argv) < 2 or len(sys.argv) > 4):
        print ("Usage: " + sys.argv[0] + " IP or FQDN [Portnumber [Endportnumber]]")
        sys.exit(1)
    
    remote_host = sys.argv[1]
    print ("Scanning " + remote_host + " ...")
    p_range = range(1024, 65536, 1)
    try:  
        if(len(sys.argv) == 3):
            p_range = range(int(sys.argv[2]),int(sys.argv[2])+1, 1)
        if(len(sys.argv) == 4):
            p_range = range(int(sys.argv[2]),int(sys.argv[3])+1, 1)
        for remote_port in p_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(20)
            try:
                sock.connect((remote_host,remote_port))
            except socket_error as serr:
                if(serr.errno != errno.ECONNREFUSED):
                    raise serr
                print ("%d closed!" % remote_port)
            else:
                print ("%d open" % remote_port)
            sock.close()
        print ("Scanning " + remote_host + " successfully finished.")
    except:
        print ("Unknown exception caught - program will exit.")
        sys.exit(1)

if __name__ == "__main__":   
    scan()
