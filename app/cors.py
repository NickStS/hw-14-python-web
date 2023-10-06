from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


def setup_cors(app: FastAPI):
    origins = ["http://localhost"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/example-route/", tags=["cors"])
    async def example_route():
        return {"message": "This route has CORS enabled."}

    @app.get("/other-route/", tags=["no_cors"])
    async def other_route():
        return {"message": "This route has no CORS."}


