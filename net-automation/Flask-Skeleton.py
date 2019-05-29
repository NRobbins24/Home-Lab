# Example template for using Flask to return netmiko 
from flask import Flask                                                                                                                                                                        
from flask import render_template                                                                                                                                                              
from flask import request                                                                                                                                                                      
from netmiko import Netmiko                                                                                                                                                                    
app = Flask(__name__)                                                                                                                                                                          
cisco1 = {                                                                                                                                                                                     
        "host": "10.0.1.170",                                                                                                                                                                  
        "username": "cisco",                                                                                                                                                                   
        "password": "cisco",                                                                                                                                                                   
        "device_type": "cisco_ios",                                                                                                                                                            
}                                                                                                                                                                                              

                                                                                                                                                                                               
def showRun(commandflag):                                                                                                                                                                      
        net_connect = Netmiko(**cisco1)                                                                                                                                                        
        command = commandflag                                                                                                                                                                  
        print()                                                                                                                                                                                
        print(net_connect.find_prompt())                                                                                                                                                       
        output = net_connect.send_command(command)                                                                                                                                             
        net_connect.disconnect()                                                                                                                                                               
        return(output)                                                                                                                                                                         
                                                                                                                                                                                               
                                                                                                                                                                                               
@app.route("/")                                                                                                                                                                                
def hello():                                                                                                                                                                                   
        cmd = request.args.get('cmd')                                                                                                                                                          
        if cmd == "run":                                                                                                                                                                       
                commandflag = "show run"                                                                                                                                                       
        elif cmd == "int":                                                                                                                                                                     
                commandflag = "show ip int brief"                                                                                                                                              
        else:                                                                                                                                                                                  
                commandflag = "show ver"                                                                                                                                                       
        conf = showRun(commandflag)                                                                                                                                                            
        return render_template('index.html',conf=conf)                                                                                                                                         
                                                                                                                                                                                               
if __name__ == "__main__":                                                                                                                                                                     
        app.run(host='0.0.0.0')              
