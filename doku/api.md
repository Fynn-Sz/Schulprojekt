# API-Dokumentation

Diese Dokumentation richtet sich an Entwickler und Nutzer, die unsere API verwenden möchten, ohne sich in den Quellcode einarbeiten zu müssen.

**Basis-URL (Lokal):** `http://127.0.0.1:8000`

---

## 1. Alle Tickets abrufen
Gibt eine Liste aller in der Datenbank gespeicherten Tickets und User Stories zurück.

* **Endpunkt:** `/userstories`
* **HTTP-Methode:** `GET`
* **Erwartete Eingabe:** Keine.
* **Erfolgreiche Rückgabe (200 OK):**
  ```json
  {
    "status": "read",
    "tickets": [
      {
        "id": "1",
        "titel": "Ticket Titel",
        "beschreibung": "Ausführliche Beschreibung...",
        "quellDatei": "import_data.json",
        "prio": "Hoch",
        "status": "Offen",
        "fach": ["EVP"]
      }
    ]
  }
  ```

  ### 1.1 Keine Tickets zuvor Hochgeladen
  ```
  {
  "status": "read",
  "tickets": []
  } 
  ``` 

---

## 2. Einzelnes Ticket abrufen
Ruft die Details eines spezifischen Tickets anhand seiner eindeutigen ID ab.

* **Endpunkt:** `/userstories/{story_id}`
* **HTTP-Methode:** `GET`
* **Erwartete Eingabe:** Die `story_id` als Pfad-Parameter.
* **Erfolgreiche Rückgabe (200 OK):**
  ```json
  {
    "status": "read",
    "ticket": [
      {
        "id": "1",
        "titel": "Ticket Titel",
        "beschreibung": "...",
        "quellDatei": "import_data.json",
        "prio": "Hoch",
        "status": "Offen",
        "fach": ["SDM"]
      }
    ]
  }
  ```
* **Fehlerfälle:**
  * `404 Not Found`: `"Ticket nicht gefunden"` (Falls die angegebene ID nicht existiert).

---

## 3. Daten importieren
Erlaubt das Hochladen einer Datei (JSON oder CSV), verarbeitet die darin enthaltenen Tickets, ermittelt automatisch die passenden Schulfächer und speichert die Daten in der Datenbank ab.

* **Endpunkt:** `/import`
* **HTTP-Methode:** `POST`
* **Erwartete Eingabe:** `multipart/form-data`
  * Feldname: `importDatei` (Die hochzuladende Datei, max. 5 MB)
* **Erfolgreiche Rückgabe (200 OK):**
  ```json
  {
    "status": "saved",
    "ticket": [
      {
        "id": "2",
        "titel": "Neues Ticket",
        "beschreibung": "...",
        ...
      }
    ]
  }
  ```
* **Fehlerfälle:**
  * `400 Bad Request`: `"Ungültiger Dateityp"` (Wenn die Datei weder CSV, JSON noch XML ist).
  * `401 Unauthorized`: `"Importdatei zu groß"` (Wenn die Dateigröße 5 MB überschreitet).
  * `404 Not Found`: `"Ticket nicht gefunden"` (Wenn die Datei erfolgreich verarbeitet, aber keine gültigen Tickets gefunden wurden).

---

## 4. Einzelnes Ticket löschen
Löscht ein spezifisches Ticket dauerhaft aus der Datenbank.

* **Endpunkt:** `/delete/{story_id}`
* **HTTP-Methode:** `DELETE`
* **Erwartete Eingabe:** Die `story_id` als Pfad-Parameter.
* **Erfolgreiche Rückgabe (200 OK):**
  ```json
  {
    "status": "deleted",
    "ticketID": "1"
  }
  ```
* **Fehlerfälle:**
  * `404 Not Found`: `"Ticket nicht gefunden"` (Falls die angegebene ID nicht existiert und somit nicht gelöscht werden konnte).

---

## 5. Alle Tickets löschen
Löscht **alle** gespeicherten Tickets aus der Datenbank.

* **Endpunkt:** `/delete`
* **HTTP-Methode:** `DELETE`
* **Erwartete Eingabe:**  (Erfordert aktuell form-data `importDatei` im Body laut API Definition).
* **Erfolgreiche Rückgabe (200 OK):**
  ```json
  {
    "status": "Es wurden alle Einträge der Datenbank gelöscht."
  }
  ```
