# package for notify error messages to telegram

### How to use?

> set env vars

example:\
EXCEPTION_NOTIFY_NOTIFY_TO=telegram\
EXCEPTION_NOTIFY_BOT_TOKEN=your-bot-token\
EXCEPTION_NOTIFY_CHAT_ID=your-chat-id\
EXCEPTION_NOTIFY_SERVICE_NAME=your-service-name

> initialize exception_notifier with your FastApi app instance

example:

```
from fastapi import FastAPI

import exception_notifier

app = FastAPI()

exception_notifier.init(app=app)


@app.get('/error')
async def root():
    zero_division_error = 1 / 0


@app.get('/success')
async def hello():
    return {'ok': 'true'}
```

then run with gunicorn
> gunicorn app:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
