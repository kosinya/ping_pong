import uvicorn
from fastapi import FastAPI
from database import Base, engine
from routers import tournament, player, department


app = FastAPI()
app.include_router(tournament.router, prefix='/tournaments')
app.include_router(player.router, prefix='/player')
app.include_router(department.router, prefix='/department')
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, workers=4)
