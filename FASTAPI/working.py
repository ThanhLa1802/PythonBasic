from fastapi import FastAPI, HTTPException, status
from fastapi.params import Path
from pydantic import BaseModel
from typing import Optional
class Course(BaseModel):
    name: str
    price: float
    teacher: Optional[str] = None

app = FastAPI()
course = {}
@app.get("/get-course/{course_id}")
def get_course(course_id: int = Path(None, description = "The ID of the course less than 10")):
    return course[course_id]
    
@app.get("/get-name")
def get_course(name: str):
    for course_id in course:
        if course[course_id].name == name:
            return course[course_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
@app.post("/create_course")
def create_course(course_id: int, cou: Course):
    if course_id in course:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Course exists!")
    course[course_id] = cou
    return course[course_id]
@app.put("/update_course/{course_id}")
def update_course(course_id: int, cou: Course):
    if course_id not in course:
        return {"Error": "Course does not exists!"}
    course[course_id] = cou
    return course[course_id]
@app.delete("/delete_course/{course_id}")
def delete_course(course_id: int, cou: Course):
    if course_id not in course:
        return {"Error": "Course does not exists!"}
    del course[course_id]
    return {"Success":"Course deleted!"}