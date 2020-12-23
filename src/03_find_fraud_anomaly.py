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

addresses = [ f'Musterstraße {i}' for i in range(1,11)]
accounts = [ f'Bank Account {i}' for i in range(1, 14)]
phones = [f'Phone Number {i}' for i in range(1,12)]
creditcards = [f'Credit Card Number {i}' for i in range(1,7)]
socialsecuritynumbers = [f'SSN {i}' for i in range(1,12)]


relationships = {
    'HAS_ADDRESS':(('Person', 'name', persons), ('Address', 'address', addresses)),
    'HAS_BANKACCOUNT':(('Person', 'name', persons), ('BankAccount', 'account', accounts)),
    'HAS_CREDITCARD':(('Person', 'name', persons), ('CreditCard', 'number', creditcards)),
    'HAS_SSN':(('Person', 'name', persons), ('SSN', 'ssn', socialsecuritynumbers))
}


if __name__ == "__main__":
    # See https://neo4j.com/developer/aura-connect-driver/ for Aura specific connection URL.
    scheme = "neo4j"  # Connecting to Aura, use the "neo4j+s" URI scheme
    host_name = "localhost"
    port = 7687  # Bolt Port https://neo4j.com/docs/operations-manual/current/configuration/ports/ | .NET | Java | JavaScript | Go | Python

    url = f"{scheme}://{host_name}:{port}"
    user = 'neo4j'
    password = 'neo4j'
    db_helper = DbHelper(url, user, password)

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
