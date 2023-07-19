from fastapi import FastAPI, WebSocket

app = FastAPI()

global_users = dict()

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        await websocket.send_text(f"Received message: {message}")

# GET endpoint
@app.get("/get")
async def get_endpoint():
    data = {"message": "This is a GET request"}
    return data

# GET users
@app.get("/users")
async def get_users():
    return global_users

# DELETE user
@app.delete("/users/{username}")
async def get_users(username: str):
    del global_users[username]
    return global_users

# POST Add user
@app.post("/user")
async def post_endpoint(data: dict):
    global_users[data['name']] = data
    return global_users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)