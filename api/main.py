from fastapi import FastAPI
import api.route 

app = FastAPI()

app.include_router(api.route )
