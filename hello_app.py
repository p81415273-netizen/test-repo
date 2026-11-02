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
    uvicorn.run("hello_app:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
