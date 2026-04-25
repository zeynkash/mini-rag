from fastapi import FastAPI
app = FastAPI()

@app.get("/Welcome")
def welcome():
    return {"message": "welcome to fastapi"}
