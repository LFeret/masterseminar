from DbHelper import DbHelper

persons = [
    'Lucy',
    'Franz',
    'Susanne',
    'Jonathan',
    'Max',
    'Stephan',
    'Julian',
    'Frederike',
    'Amy',
    'Miriam',
    'Jonas',
    'Anna',
    'Sebastian'
]


if __name__ == "__main__":
    # See https://neo4j.com/developer/aura-connect-driver/ for Aura specific connection URL.
    scheme = "neo4j"  # Connecting to Aura, use the "neo4j+s" URI scheme
    host_name = "localhost"
    port = 7687  # Bolt Port https://neo4j.com/docs/operations-manual/current/configuration/ports/ | .NET | Java | JavaScript | Go | Python

    url = f"{scheme}://{host_name}:{port}"
    user = 'neo4j'
    password = 'neo4j'
    db_helper = DbHelper(url, user, password)

    for name in persons:
        db_helper.run_query(
            'CREATE (person:Person {name: "' + name + '" }) RETURN person.name'
        )

    db_helper.close()
