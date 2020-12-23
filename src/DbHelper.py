import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable


class DbHelper:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self.__run, query
            )
            for record in result:
                print(record)

    @staticmethod
    def __run(tx, query):
        result = tx.run(query)
        try:
            return [record for record in result]
        except ServiceUnavailable as ex:
            logging.error(f"{query} raised an error: \n {ex}")
            raise
