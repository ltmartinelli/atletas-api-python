from fastapi import FastAPI
from fastapi_pagination import add_pagination


from routers import api_router

app = FastAPI(title='WorkoutAPI')
app.include_router(api_router)
add_pagination(app)
