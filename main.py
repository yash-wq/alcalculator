import random, flask
from flask import Flask, request
import requests
import datetime



def add(a,b):
    return(int(a)+int(b))

def sub(a,b):
    return(int(a)-int(b))

def mult(a,b):
    return(int(a)*int(b))

app = Flask(__name__)


@app.route('/<op>/<fno>/<lno>', methods=['GET'])

def testing(op,fno,lno):
    now = datetime.datetime.now()

  
    if op == 'add':
        nos = fno+" "+lno
        return({'operation':'Addition', 'Result':add(fno,lno)})
    elif op == 'sub':
        nos = fno+" "+lno
        return({'operation':'Substraction', 'Result':sub(fno,lno)})
    elif op == 'mult':
        nos = fno+" "+lno
        return({'operation':'Multiplication', 'Result':mult(fno,lno)})
    return({'Ans':"BAD CALL"})


@app.route('/', methods=['POST'])

def post_handling():
    content = request.get_json()
    # "POST {}".format(
    no = content['fno']+","+content['lno']
    now = datetime.datetime.now()
    if(content['operation']=='add'):
        return({"Result":int(content['fno'])+int(content['lno'])})
    if(content['operation']=='sub'):
        return({"Result":int(content['fno'])-int(content['lno'])})
    if(content['operation']=='mult'):
        return({"Result":int(content['fno'])*int(content['lno'])})

@app.route('/get_docs', methods=['GET','POST'])
def return_docs():
    new_dict={}
    for i in docs:
        new_dict[i.id] = i.to_dict()
    return(new_dict)


if __name__ == "__main__":
    app.run(debug=True)