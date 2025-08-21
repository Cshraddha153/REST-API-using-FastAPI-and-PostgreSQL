from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import sessionLocal
import models

app = FastAPI()
db = sessionLocal()

class OurBaseModel(BaseModel):
    class config:
        orm_mode = True

class Person(OurBaseModel):
    id: int
    first_name: str
    last_name: str
    is_male: bool

@app.get("/", response_model=list[Person] ,status_code=status.HTTP_200_OK)
def Person_info():
    Person_info = db.query(models.Person).all()
    return Person_info

@app.get('/get_by_id/{person_id}', response_model=Person, status_code=status.HTTP_200_OK)
def get_person_by_id(person_id: int):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    
    if find_person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    
    return find_person

@app.post('/add_person', response_model=Person, status_code=status.HTTP_201_CREATED)
def add_person(person: Person):
    new_person = models.Person(
        id = person.id,
        first_name = person.first_name,
        last_name = person.last_name,
        is_male = person.is_male
    )
    find_person = db.query(models.Person).filter(models.Person.id == person.id).first()
        
    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Person with this ID already exists")
    
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person
    
@app.put('/update_person/{person_id}', response_model=Person, status_code=status.HTTP_202_ACCEPTED)
def update_person(person_id: int, person: Person):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    
    if find_person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    
    find_person.id = person.id
    find_person.first_name = person.first_name
    find_person.last_name = person.last_name
    find_person.is_male = person.is_male

    db.commit()
    db.refresh(find_person)
    return find_person


@app.delete('/delete_person/{person_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_person(person_id: int):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if find_person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")   
    
    db.delete(find_person)
    db.commit()
    db.refresh(find_person)
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Person deleted successfully")   


