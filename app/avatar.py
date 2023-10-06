from fastapi import FastAPI, File, UploadFile
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary



app = FastAPI()

cloudinary.config(
    cloud_name="dpwcdsegr",
    api_key="183491821754649",
    api_secret="rEXZaDFrFsPqFfRIrv4wDBgqDNI"
)

@app.post("/uploadavatar/")
async def upload_avatar(user_id: int, avatar: UploadFile):
    result = upload(avatar.file)
    
    avatar_url, options = cloudinary_url(result['public_id'], format="jpg", width=150, height=150, crop="fill")
    
    return {"message": "Avatar updated", "avatar_url": avatar_url}

