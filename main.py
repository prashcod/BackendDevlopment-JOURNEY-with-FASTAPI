from fastapi import FastAPI


app = FastAPI() 

@app.get('/') #routes 
def index(): 
  return "HEYY"