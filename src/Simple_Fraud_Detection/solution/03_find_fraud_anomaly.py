import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)

from src.DbHelper import DbHelper


if __name__ == "__main__":
    scheme = "neo4j"
    host_name = "localhost"
    port = 7687

    url = f"{scheme}://{host_name}:{port}"
    user = 'neo4j'
    password = 'neo4j'
    db_helper = DbHelper(url, user, password)

    # WITH --> Erlaubt es Cypher Befehle miteinander zu verbinden, indem der Output des vorigen Befehls in den nachfolgenden übernommen wird! (Piping)
    # ORDER BY --> Ordnet die Ausgabe nach dem gegebenen Feld in Ab- oder Aufsteigender Reihenfolge (Analog zu SQL)
    # WHERE --> Filtert Werte auf Grundlage von gesetzten Regeln (Analog zu SQL)
    query = '''
    MATCH       (person:Person)-[]->(contactInformation)
    WITH        contactInformation,
                count(person) AS RingSize
    MATCH       (contactInformation)<-[]-(person)
    WITH        collect(person.name) AS persons,
                contactInformation, RingSize
    WHERE       RingSize > 1
    RETURN      persons AS FraudRing,
                labels(contactInformation) AS ContactType,
                RingSize
    ORDER BY    RingSize DESC 
    '''

    db_helper.run_query(
        query
    )

    db_helper.close()
