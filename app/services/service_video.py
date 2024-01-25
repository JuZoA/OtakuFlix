from fastapi import UploadFile
import shutil
class Video:
    pass


def write_video(file_name: str, file: UploadFile):
    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)