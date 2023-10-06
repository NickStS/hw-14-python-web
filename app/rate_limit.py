from fastapi import FastAPI, Depends, HTTPException
from datetime import datetime

app = FastAPI()

request_counters = {}
last_request_time = {}

def rate_limit_request(user_id: int):
    if user_id not in request_counters:
        request_counters[user_id] = 0
        last_request_time[user_id] = datetime.now()
    
    current_time = datetime.now()
    if (current_time - last_request_time[user_id]).total_seconds() >= 60:
        request_counters[user_id] = 0
        last_request_time[user_id] = current_time
    
    if request_counters[user_id] >= 5:
        raise HTTPException(status_code=429, detail="Too many requests")

    request_counters[user_id] += 1

@app.get("/contacts/")
async def list_contacts(user_id: int = Depends(rate_limit_request)):
    return {"message": "List of contacts"}
