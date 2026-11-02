import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Hello App")


@app.get("/")
async def root():
    return {"message": "hello"}


@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"hello {name}"}


def main():
    uvicorn.run("hello_app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
