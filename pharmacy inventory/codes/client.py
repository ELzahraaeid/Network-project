#libraries
import sys
import socket
from gui import Ui_MainWindow
from PyQt5 import QtWidgets, uic
import codecs
import time 

HEADER = 1024
PORT = 1234
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = b'!DISCONNECT'
SERVER = "192.168.1.11"
ADDR = (SERVER, PORT)

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send_input)
        #create the client socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect the client socket to the server 
        self.client.connect(ADDR)
    def send(self , msg):
    	#handle the length of the message and send it to the server and calling the recieve function
    	msg_length = len(msg)
    	send_length = str(msg_length).encode(FORMAT)
    	send_length += b' ' * (HEADER - len(send_length))
    	self.client.send(send_length)
    	self.client.send(msg)
    	self.receive()
	    


    def receive(self):
    	#reciving data from the server
    	recv_data = self.client.recv(1024)
    	#converting the recieved data from bytes to string
    	m=codecs.decode(recv_data , 'UTF-8')
    	#sending the data to the text label in the ui
    	if m=='product not found in any branch':
    		self.ui.label_4.setText(m)
    	elif m=='close':
    		print(m , "connection")
    	else:    
            index=[]
            count_index=[]
            for i in range (0,len(m)):
                if m[i]=='|':
                    count_index.append(i)
                    
                elif m[i]==',':
                    index.append(i)
            self.message=m[:count_index[0]]+'\t    '+m[count_index[0]+1:index[0]]+'\n'
            for i in range(0,len(index)-1):
                self.message+=m[index[i]+1:count_index[i+1]]+'\t    ' +m[count_index[i+1]+1:index[i+1]]+'\n'
            self.ui.label_4.setText(self.message)




    def send_input(self):
    	#getting the inserted messages from the ui
        self.data=self.ui.lineEdit.text()
        #converting the message from string to bytes
        self.messages=[bytes(self.data,'utf-8')]
        #sending the message to the send function to send it to the server 
        self.send(self.messages[0])

    def closeEvent(self , event):
    	#closing the connection by the client
    	self.send(DISCONNECT_MESSAGE)




def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()    


