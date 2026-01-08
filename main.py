from fastapi import FastAPI
from pydantic import BaseModel 
from typing import List     #ImportError: cannot import name 'list' from 'typing' (/usr/lib/python3.12/typing.py). Did you mean: 'List'?


app = FastAPI()

#pydantic two models : one for data in and another for data out

class Tea(BaseModel):
    id: int 
    name: str
    origin: str   #is more complex but simple for this crash course

# teas =[]   can be done but lets use typing

teas: List[Tea] = []    #define ds from pydantic

#fast api uses concepts of decorators 
'''for example we want / => welcome to tea house
'''

@app.get('/') #after this defination of method
def read_root():
    return {'message': 'Welcome to TeaHouse'}

@app.get('/teas')
def get_teas():
    return teas

#now lets do curd operations
@app.post('/teas')
def add_tea(tea: Tea):            #using pydantic so need datatype compulsory
    teas.append(tea)               #no validation or checking going on here directly append to the list
    return tea

@app.put("/teas/{tea_id}")          #by this way we can accept dynamic parameter direct into a function
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return{'error': "Tea not found"}


@app.delete('/teas/{tea_id}')
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            del teas[index]                    #teas.remove("tea") removes first occurence of tea
            return deleted
    return {'error': 'Tea not found'}

'''how to run:
1. run through uvicorn
2. app inside main 
    uvicorn main:app --reload '''
    
'''The correct command is simply:
deactivate

It's failing because the shell cannot find the deactivate function defined during the activation process. This usually happens if:

You are in a different terminal/shell session than the one where you activated the venv.
The activation process itself didn't complete correctly.'''