from fastapi import FastAPI
from routes import first
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(first.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)
  
  