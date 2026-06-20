from fastapi import FastAPI, HTTPException, UploadFile, File
from typing import List
from Schulprojekt.models import UserStory, ClassificationResult

app = FastAPI(
    title="Abschlussprojekt Ticket",
    version="1.0.0"
)

fake_db: List[UserStory] = []


@app.get("/userstories", response_model=List[UserStory])
async def get_all_userstories():
    return fake_db


@app.get("/userstories/{story_id}", response_model=UserStory)
async def get_single_userstory(story_id: str):
    for story in fake_db:
        if story.id == story_id:
            return story
    raise HTTPException(status_code=404, detail="User Story nicht gefunden")

@app.post("/import/{source_type}")
async def import_data(source_type: str, file: UploadFile = File(...)):
    if source_type not in ["csv", "json", "xml"]:
        raise HTTPException(status_code=400, detail="Nicht unterstütztes Format.")
    
    # platzhalter finn
    
    return {"message": f"Datei {file.filename} empfangen"}

@app.post("/classify", response_model=ClassificationResult)
async def classify_userstory(story: UserStory):
    
    return #platzhalter finn