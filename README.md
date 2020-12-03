# masterseminar

Willkommen zum Tutorial des Masterseminars für Neo4j. Dies
ist der Haupteinstiegspunkt zum Tutorial zum Einrichten und Arbeiten mit
Neo4j in Windows 10 64 Bit.

**@author**: Leander Féret

# Installiere Python3

Für dieses Tutorial wurde Python3 in der Version 3.9 verwendet. Sollte diese nicht bereits auf
dem System so vorhanden sein, dass es über Python in der Shell erreicht wird, sollte bitte folgendem Tutorial
zur Installation gefolgt werden:

[Install Guide - Python3 für Windows 10 64 Bit](tutorial/Installation-python3-win10b64.pdf)

# Virtual Environment erstellen und aktivieren

Installiere das Paket **virtualenv** für Ihre Python-Installation:

```bash
pip install virtualenv
```

Navigieren Sie im Terminal in das Projectverzeichnis dieses Tutorials über

```bash
cd C:\\Path\\to\\this\\project\\directory
```

Erstellen Sie eine virtuelle Umgebung.

```bash
python -m virtualenv .venv
```

Aktivieren Sie die virtuelle Umgebung.

```bash
.\.venv\Scripts\activate
```

Installieren Sie die verwendeten Pakete dieses Tutorials über

```bash
pip install -r requirements.txt
```

Nachfolgend wird immer davon ausgegangen, dass Sie python-Befehle in einem Terminal mit
dieser aktivierten virtuellen Umgebung ausführen.

# Installiere Neo4j Community Edition und OpenJdk 15

Für dieses Tutorial muss Neo4j Community und OpenJdk installiert sein. Hierfür sollte dem
nachfolgenden PDF-gefolgt werden.

[Install Guide - Neo4j Community und OpenJdk](tutorial/Installation-neo4j-communityServer-windows10.pdf)

**Achtung!** Beachten Sie, dass sich neo4j.exe auch wirklich unter C:\neo4j\neo4j-community-4.1.3\bin
befindet, wie in dem Install Guide beschrieben. Wenn Sie einen anderen Pfad verwenden, müssen Sie in der folgenden
Datei den Pfad zu Ihrem abändern.

[noxfile.py - Script Sammlung](noxfile.py)

![Neo4j - Path Änderung](./tutorial/images/noxfile_path.PNG)

Stimmt der Pfad mit Ihrem überein, so können Sie Neo4j auch mit Hilfe der Scriptsammlung dieses Tutorials starten:

```bash
nox -s neo4j
```

# Neo4j Web

Machen Sie sich mit Neo4js Weboberfläche vertraut, indem Sie folgendem Tutorial folgen.
Anschließend wird mit dem Ergebnis über Python weitergearbeitet.

[Erste Schritte - Neo4j Web](tutorial/Installation-neo4j-communityServer-windows10.pdf)

# Neo4j Python



[Erste Schritte - Neo4j Python](tutorial/Installation-neo4j-communityServer-windows10.pdf)


