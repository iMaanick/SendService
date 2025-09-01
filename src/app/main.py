from fastapi import FastAPI

app = FastAPI(title="FastAPI Example")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
