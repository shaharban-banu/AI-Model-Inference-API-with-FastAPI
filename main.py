from fastapi import FastAPI
import models
from database import engine,Base
from routes import router

from ratelimiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from prometheus_fastapi_instrumentator import Instrumentator

models.Base.metadata.create_all(bind=engine)

app=FastAPI(title='Sentiment Analysis')

app.state.limiter=limiter
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)

Instrumentator().instrument(app).expose(app)


