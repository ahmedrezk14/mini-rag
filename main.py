from fastapi import FastAPI

app=FastAPI()

# decorator
@app.get("/welcome")
def welcome():
    return {
        "message":"Hello world!"
    }


