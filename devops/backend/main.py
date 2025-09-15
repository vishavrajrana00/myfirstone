# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (not secure for production!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI! This is 1st deployment"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/hello1/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
