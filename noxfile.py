NEO4JPATH = 'C:\\neo4j\\neo4j-community-4.1.3\\bin'

import nox

@nox.session(name='neo4j')
def start_neo4j(session):
    print('Startup Neo4j')
    session.run('cmd', '/c', f'{NEO4JPATH}\\neo4j console', external=True)
