import socket
import sys
#Connect to time server time.nist.gov

user_time_server = sys.argv[1]

TIME_SERVER = ['time.nist.gov', 'time.windows.com', 'utcnist.colorado.edu']
TIME_SERVER_PORT = 13

sock = socket.socket()

for ts in TIME_SERVER:
    try:
        sock.connect((ts, TIME_SERVER_PORT))
        msg = sock.recv(1024)
        sock.close
        print(msg.decode('ascii'))
    except Exception:
        print(f'unable to connect {ts}. Trying to connect next')
