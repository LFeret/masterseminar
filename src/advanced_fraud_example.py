import random
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

addresses = [ f'Musterstraße {i}' for i in range(1, random.randrange(5, 14))]
accounts = [ f'Bank Account {i}' for i in range(1, random.randrange(5, 14))]
phones = [f'Phone Number {i}' for i in range(1, random.randrange(5, 14))]
creditcards = [f'Credit Card Number {i}' for i in range(1, random.randrange(5, 14))]
socialsecuritynumbers = [f'SSN {i}' for i in range(1, random.randrange(5, 14))]


nodes = {
    'Person':('name', persons),
    'Address':('address', addresses),
    'BankAccount':('account', accounts),
    'CreditCard':('number', creditcards),
    'SSN':('ssn', socialsecuritynumbers)
}


relationships = {
    'HAS_ADDRESS':(('Person', 'name', persons), ('Address', 'address', addresses)),
    'HAS_BANKACCOUNT':(('Person', 'name', persons), ('BankAccount', 'account', accounts)),
    'HAS_CREDITCARD':(('Person', 'name', persons), ('CreditCard', 'number', creditcards)),
    'HAS_SSN':(('Person', 'name', persons), ('SSN', 'ssn', socialsecuritynumbers))
}


if __name__ == "__main__":
    scheme = "neo4j"
    host_name = "localhost"
    port = 7687

    url = f"{scheme}://{host_name}:{port}"
    user = 'neo4j'
    password = 'neo4j'
    db_helper = DbHelper(url, user, password)

    # 01. clear db
    db_helper.run_query(
        'MATCH (n) DETACH DELETE n'
    )

    # 02. fill database
    for Label, values in nodes.items():
        PropertyKey = values[0]
        for PropertyValue in values[1]:
            # Auch über eine Query Syntax mit Create (), (), () möglich!
            db_helper.run_query(
                'CREATE (node:' + Label + ' {' + PropertyKey + ': "' + PropertyValue + '" }) RETURN node.' + PropertyKey
            )

    # 03. create random relationships
    for RelationshipType, values in relationships.items():
        node1 = values[0]
        node2 = values[1]
        Label1 = node1[0]
        Label2 = node2[0]
        PropertyKey1 = node1[1]
        PropertyKey2 = node2[1]
        nodes1 = node1[2]
        nodes2 = node2[2]
        random.shuffle(nodes1)
        random.shuffle(nodes2)

        itermax = len(nodes1) if len(nodes1) > len(nodes2) else len(nodes2) 

        PropertyValue1 = None
        PropertyValue2 = None

        for i in range(itermax):
            try:
                PropertyValue1 = nodes1[i]
            except IndexError:
                PropertyValue1 = nodes1[-1]
            
            try:
                PropertyValue2 = nodes2[i]
            except IndexError:
                PropertyValue2 = nodes2[-1]

            query = 'MATCH '
            query += f'(a:{Label1}),(b:{Label2}) '
            query += f'WHERE a.{PropertyKey1} = "{PropertyValue1}" AND b.{PropertyKey2} = "{PropertyValue2}" '
            query += f'CREATE (a)-[r:{RelationshipType}]->(b) '
            query += 'RETURN type(r)'

            db_helper.run_query(
                query
            )
    
    # 04. look for frauds
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
