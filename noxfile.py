NEO4JPATH = 'C:\\neo4j\\neo4j-community-4.1.3\\bin'

import nox
import os

@nox.session(name='neo4j')
def start_neo4j(session):
    print('Startup Neo4j')
    session.run('cmd', '/c', f'{NEO4JPATH}\\neo4j console', external=True)

basedirectory = os.path.dirname(os.path.abspath(__file__))

@nox.session(name='fraud_ex_1')
def start_neo4j(session):
    print('Create the Fraud-Exercise Nodes')
    session.install('-r', 'requirements.txt')
    session.run('python', os.path.join(basedirectory, 'src', 'Simple_Fraud_Detection', 'to_complete', '01_fill_fraud_db_with_nodes.py'))

@nox.session(name='fraud_ex_2')
def start_neo4j(session):
    print('Create the Fraud-Exercise Relationships')
    session.install('-r', 'requirements.txt')
    session.run('python', os.path.join(basedirectory, 'src', 'Simple_Fraud_Detection', 'to_complete', '02_add_relationships_to_nodes.py'))

@nox.session(name='fraud_ex_3')
def start_neo4j(session):
    print('Check for Anomaly')
    session.install('-r', 'requirements.txt')
    session.run('python', os.path.join(basedirectory, 'src', 'Simple_Fraud_Detection', 'to_complete', '03_find_fraud_anomaly.py'))

@nox.session(name='fraud_sol_1')
def start_neo4j(session):
    print('Create the Fraud-Exercise Nodes')
    session.install('-r', 'requirements.txt')
    session.run('python', os.path.join(basedirectory, 'src', 'Simple_Fraud_Detection', 'solution', '01_fill_fraud_db_with_nodes.py'))

@nox.session(name='fraud_sol_2')
def start_neo4j(session):
    print('Create the Fraud-Exercise Relationships')
    session.install('-r', 'requirements.txt')
    session.run('python', os.path.join(basedirectory, 'src', 'Simple_Fraud_Detection', 'solution', '02_add_relationships_to_nodes.py'))

@nox.session(name='fraud_sol_3')
def start_neo4j(session):
    print('Check for Anomaly')
    session.install('-r', 'requirements.txt')
    session.run('python', os.path.join(basedirectory, 'src', 'Simple_Fraud_Detection', 'solution', '03_find_fraud_anomaly.py'))
