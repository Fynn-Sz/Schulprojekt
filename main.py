#Da alle Module in einem Verzeichnis liegen kein import z.B. xxx.database
from importExportFunktionen import jsonRead, csvRead, jsonWriteInDatabase, csvWriteInDatabase
from database import alleTicketsLaden, ticketLoeschen, einTicketLaden, alleTicketsLoeschen
from datensatzStruktur import ImportDatensatz
from pathlib import Path
from dataclasses import asdict
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI(
    title="Abschlussprojekt Ticket",
    version="1.0.0"
)

#Endpunkte
@app.get("/userstories")
async def get_all_userstories():
    tickets: list[ImportDatensatz] = alleTicketsLaden()
    return {"status": "read", "tickets": [asdict(ticket) for ticket in tickets]}

@app.get("/userstories/{story_id}")
async def get_single_userstory(story_id: str):
    tickets: list[ImportDatensatz] = einTicketLaden(story_id)
    if len(tickets) == 0:
        raise HTTPException(
        status_code=404,
        detail="Ticket nicht gefunden"
    )
    return {"status": "read", "ticket": [asdict(ticket) for ticket in tickets]}

@app.delete("/delete/{story_id}")
async def deleteTicket(story_id: str):
    tickets = ticketLoeschen(story_id)
    if len(tickets) == 0:
        raise HTTPException(
        status_code=404,
        detail="Ticket nicht gefunden"
    )
    return {"status": "deleted", "ticketID": story_id}

@app.delete("/delete")
async def deleteAllTickets(importDatei: UploadFile = File(...)):
    alleTicketsLoeschen()
    return {"status": "Es wurden alle Einträge der Datenbank gelöscht."}

@app.post("/import")
async def import_data(importDatei: UploadFile = File(...)):
    dateiInhalt = await importDatei.read()

    dateiPfadUndName, dateiname = importVerzeichnisErstellen(importDatei)
    importDateiCheckUndDateiKopieren(dateiInhalt, dateiname, dateiPfadUndName)
    
    dateiTyp = dateiname.split(".")[-1].lower()
    tickets = writeFile(str(dateiPfadUndName), dateiTyp)
    
    if len(tickets) == 0:
        raise HTTPException(
        status_code=404,
        detail="Ticket nicht gefunden"
    )   
    return {"status": "saved", "ticket": [asdict(ticket) for ticket in tickets]}
    


#Hilfsfunktionen
#Erstellt "imports" Ordner im Projektverzeichnis und gibt Dateinamen und Pfad zurück
def importVerzeichnisErstellen(importDatei):
    speicherPfad = Path("imports")
    speicherPfad.mkdir(exist_ok=True)

    dateiname = Path(importDatei.filename).name
    dateiPfadUndName = speicherPfad / dateiname
    
    return dateiPfadUndName, dateiname

#Checks + schreiben der importieren Datei
def importDateiCheckUndDateiKopieren(dateiInhalt, dateiname, dateiPfadUndName):
    #Dateityp kontrollieren
    if not dateiname.endswith((".csv", ".json", ".xml", ".CSV", ".JSON", ".XML")):
        raise HTTPException(status_code=400, detail="Ungültiger Dateityp")

    #Dateigröße Checken
    maxDateiGroesse = 5 * 1024 * 1024
    if len(dateiInhalt) > maxDateiGroesse:
        raise HTTPException(status_code=401, detail="Importdatei zu groß")

    with open(dateiPfadUndName, "wb") as f:
        f.write(dateiInhalt)

#Liest die Importdatei, verarbeitet den Inhalt und schreibt ihn in die Datenbank, 
#anschließend wird das Objekt, bzw. die Objekte zurück gegeben
def writeFile(dateiname, dateiTyp) -> list[ImportDatensatz]:
    match dateiTyp:
        case "json":
            return jsonWriteInDatabase(dateiname)

        case "csv":
            return csvWriteInDatabase(dateiname)

        #case "xml":
        #   return xmlWriteInDatabase(dateiname)
        

def readFile(dateityp, dateiName) -> list[ImportDatensatz]:
    match dateityp:
        case "json":
            return jsonRead(dateiName)

        case "csv":
            return csvRead(dateiName)

        #case "xml":
        #    return xmlRead(dateiName)