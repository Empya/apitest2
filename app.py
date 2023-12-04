from flask import Flask, jsonify, request

app = Flask(__name__)

all_students = [
{"id":1, "name": "a"},
{"id":2, "name": "b"},
{"id":3, "name": "c"},
{"id":4, "name": "d"},
{"id":5, "name": "e"},
{"id":6, "name": "f"}
]
print(dir(all_students))

@app.get("/students")

def get_students():
    return jsonify(all_students)
    

@app.get("/students/<int:id>")

def get_student(id): 
    if request.is_json:
        for student in all_students: 
            if student["id"] == id:
                return student
            
            else:
          
                return {"error": " Not Found", "code": " 404"}

    else:
        return {"error":"Not json request"}
 
 
@app.delete("/students/<int:id>")

def delete_student(id):
    for data in all_students:
        if data["id"] == id:
            all_students.remove(data)
            return jsonify(all_students)
            
        return {"error": 404}
        
