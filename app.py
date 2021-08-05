from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def shounok():  
    return "<h1>We are from learning cloud deployment</h1>";  
  
if __name__ =='__main__':  
    app.run()  



