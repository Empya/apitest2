
from flask import Flask, jsonify

app = Flask(__name__)

dict =[
{"name":1},{"name":2},{"name":3}
]


@app.get("/all")

def showall(): 
    return jsonify(dict)
    
@app.get("/<int:id>")  

def showany(id):
    a = None
    for any in dict:
        if any["name"] == id:
            print(any)
            a = any
            
    return a
    
@app.post("/", methods=["POST","GET"])

def add():
    
    if request.is_json:
        new = request.get_json
        dict.append(new)
        return new, 201
    
    else:
        return {"FAILED":"failed"}
