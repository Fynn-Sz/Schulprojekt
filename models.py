from pydantic import BaseModel
from typing import List, Optional

class UserStory(BaseModel):
    id: str
    titel: str
    beschreibung: Optional[str] = None
    quelle: str 
    rolle: Optional[str] = None
    prioritaet: Optional[str] = None
    tags: Optional[List[str]] = []

class ClassificationResult(BaseModel):
    sdm_punkte: int
    evp_punkte: int
    gid_punkte: int
    begruendung: str