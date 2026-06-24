# Testdokumentation

Diese Datei beschreibt die durchgeführten Testfälle für unsere API und die integrierten Funktionen (Mapping, Dateiverarbeitung und Regeln).

## Testfälle

| Testfall | Beschreibung | Erwartetes Ergebnis | Tatsächliches Ergebnis | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TF02** | Import von Dateien (CSV/JSON/XML) | Dateien werden fehlerfrei geladen und in das interne Datenmodell geparst. | Daten erfolgreich geladen und verarbeitet. | Bestanden |
| **TF03** | API-Regel: `POST /classify` (Mapping) mit gültigen Daten | Ticket/Story wird anhand der Regeln dem korrekten Fachbereich zugewiesen. | Mapping-Regel greift, Zuweisung ist korrekt. | Bestanden |
| **TF04** | API-Regel: `POST /classify` mit unbekannten Parametern | Ticket/Story wird der Standardkategorie zugewiesen oder gibt definierten Fehler aus. | Standardkategorie wurde erfolgreich zugewiesen. | Bestanden |
| **TF05** | `POST /userstories` - Neues Ticket anlegen | API antwortet mit Status 201 (Created), Ticket wird gespeichert. | Status 201 erhalten, ID wurde erfolgreich vergeben. | Bestanden |
| **TF06** | `POST /userstories` mit fehlenden Feldern | API antwortet mit Status 400 oder 422 und lehnt die Anfrage ab. | Status 422 erhalten, Validation Error wird ausgegeben. | Bestanden |
| **TF07** | `GET /userstories` - Abruf aller Tickets | Status 200, JSON-Antwort mit einer Liste aller vorhandenen Tickets. | Status 200, Liste ist vollständig und valide formatiert. | Bestanden |
| **TF08** | `GET /userstories/{id}` - Abruf über ID | Status 200, JSON mit detaillierten Daten zum angefragten Ticket. | Status 200, korrekte Ticket-Daten abgerufen. | Bestanden |
| **TF09** | `GET /userstories/{id}` mit falscher ID | Status 404 (Not Found) inkl. verständlicher Fehlermeldung. | Status 404, Fehlermeldung "Not Found" wird ausgegeben. | Bestanden |
| **TF10** | Dateiverarbeitung: Fehlerhafte Dateien importieren | Die Applikation fängt den Fehler ab, es kommt zu keinem Absturz. | Logik fängt Fehler ab, entsprechende Fehlermeldung in der API. | Bestanden |
| **TF11** | Komplettes Mapping-Regelwerk validieren | Alle Punkte/Kategorien werden ordnungsgemäß und korrekt berechnet. | Kategorien werden fehlerfrei nach Punkten berechnet. | Bestanden |
