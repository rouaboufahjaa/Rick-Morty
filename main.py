"""Main function."""
from fastapi import FastAPI
import api.episode as episodeApi
import api.character as characterApi
import api.comment as commentApi
import api.user as userApi
import api.statistics as statisticsApi



app = FastAPI()

app.include_router(characterApi.app)
app.include_router(episodeApi.app)
app.include_router(commentApi.app)
app.include_router(userApi.app)
app.include_router(statisticsApi.app)


@app.get('/')
def root_api():
    """Main function."""
    return {"message": "Rick&Morty Universe"}
