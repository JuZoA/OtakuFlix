from fastapi import FastAPI
import uvicorn

app = FastAPI(title="OtakuFlix")

@app.get("/")
async def hello():
    return "hello world"

if __name__ == "__main__":
    uvicorn.run(app)