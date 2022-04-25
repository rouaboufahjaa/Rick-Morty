from fastapi import FastAPI
import api.episode as episodeApi
import api.character as characterApi



app = FastAPI()

app.include_router(characterApi.app)
app.include_router(episodeApi.app)


@app.get('/')
def root_api():
    return {"message": "Rick&Morty Universe"}

