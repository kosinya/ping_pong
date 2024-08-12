import uvicorn
from fastapi import FastAPI
from database import Base, engine
from routers import tournament, player, department, league


app = FastAPI()
app.include_router(tournament.router, prefix='/tournaments')
app.include_router(player.router, prefix='/players')
app.include_router(league.router, prefix='/leagues')
app.include_router(department.router, prefix='/departments')
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, workers=4)

