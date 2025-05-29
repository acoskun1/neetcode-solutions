import socket

#initialise host and port
PORT: int = 1111
HOST: str = '127.0.0.1'

def socket_server():
    #using context manager, create a server socket of IPv4 family and TCP kind to listen for connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #before accepting connection, socket must be bound and listening
        s.bind((HOST, PORT))
        s.listen(1)
        #return value of socket.accept() is a pair: conn - new socket object usable to send and receive data on. addr - address bound to socket on other end of connection
        conn, addr = s.accept()
        #using a context manager keep connection to conn socket open inside this block.
        with conn:
            while True:
                #data is set to data received from conn socket up to 1024 in UTF-8 decoded format.
                data = conn.recv(1024).decode()
                #if data is exit or empty, break out of the while loop and context manager, closing the connection to conn
                if not data or data == 'exit':
                    break
                #reflect data back to user through conn socket object.
                else:
                    conn.sendall(data.encode())
