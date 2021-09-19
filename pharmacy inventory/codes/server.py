#libraries
import socket 
import threading
import sys
import types
import mysql.connector
import codecs

#DataBase connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="pharmacy"
)
mycursor = mydb.cursor()

#the max number of recieved bytes 
HEADER = 1024
#the IP and Port that we will run the server on
PORT = 1234
#get the local IPv4 address of the device
SERVER = socket.gethostbyname(socket.gethostname())
#the decoding format
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#create the server socket using the IPv4 address family and TCP connection protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the server to this specific address 
server.bind((SERVER, PORT))

#this function will handle the individual connections between the client and the server 
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    #
    connected = True
    while connected:
        #decoding the recieved message from bytes to string
        #determines how long is the message to know the actual number of bytes needed for the message
        msg_length = conn.recv(HEADER).decode(FORMAT) 
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            #closing the connection when the client close it
            if msg == DISCONNECT_MESSAGE:
                close=[b'close']
                conn.send(close[0])
                connected = False
                print(f"[closing connection to ] {addr} ")
            else:
                #print the recieved message
                print(f"[{addr}] {msg}")
                #search for the data from the database 
                mycursor.execute("SELECT branch_name, count  FROM products WHERE product_name =%s",(msg,))
                branch=mycursor.fetchall()
                #converting a list of tubles(branch) to a string(message)
                message=''
                for i in range (0, len(branch)):
                    message+=branch[i][0]+"|"+branch[i][1]+','
            
                #check if the product is not in the database and send it to the client
                if branch==[]:
                    mess=[b'product not found in any branch']
                    sent = conn.send(mess[0])  # Should be ready to write

                else :

                    #converting the message from a string to bytes and sending it to the client 
                    message=[bytes(message,'utf-8')]
                    if message[0]:
                        print("sending", repr(message[0]), "to", addr)
                        sent = conn.send(message[0])
                        

    conn.close()    

#this function handles the new connections 
def start():
    #server listen to the connections
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    #the server will be listenning until we execute it 
    while True:
        #the server waits until getting a new connection to the server
        #conn is the socket where the connection would happen , addr contains the IP address and the port of the connection  
        conn, addr = server.accept() 
        #start a new thread and sending the connection address to the handle_client function
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        #start the thread 
        thread.start()
        #print the number of active threads/clients 
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        


print("[STARTING] server is starting...")
start()