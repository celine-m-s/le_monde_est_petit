from world.script import *

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    print("before: ", function)

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """
    print("after:", function)

def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('Celine') == 'Hello Celine'

# - Agent : 
#   - récupérer un attribut position
def test_set_position():
    agent = Agent(3)
    agent.position = 5
    assert agent.position == 5

#   - modifier un attribut position
def test_get_position():
    agent = Agent(3)
    assert agent.position == 3

#   - assigner un dictionnaire en tant qu'attributs
def test_set_agent_attributes():
    dictionary = {"agreeableness": -0.8437190198916452}
    agent = Agent(3, **dictionary)
    assert agent.agreeableness == -0.8437190198916452

# - Position :
#   - modifier un attribut longitude_degrees
def test_longitude_degrees():
    position = Position(100.85840672174572, 33.15219798270325)
    assert position.longitude_degrees == 100.85840672174572

#   - modifier un attribut latitude_degrees
def test_latitude_degrees():
    position = Position(100.85840672174572, 33.15219798270325)
    assert position.latitude_degrees == 33.15219798270325

#   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur. 
def test_longitude_degrees_range():
    try:
        position = Position(200.85840672174572, 33.15219798270325)
    except AssertionError:
        assert True

#   - modifier un attribut latitude_degrees avec une valeur supérieure à 90 renvoie une erreur. 
def test_latitude_degrees_range():
    try:
        position = Position(100.85840672174572, 100.15219798270325)
    except AssertionError:
        assert True

#   - récupérer une longitude
def test_longitude():
    position = Position(100.85840672174572, 33.15219798270325)
    # print('longitude', position.longitude)
    assert position.longitude == 1.7603112756100432

#   - récupérer une latitude
def test_latitude():
    position = Position(100.85840672174572, 33.15219798270325)
    # print('latitude', position.latitude)
    assert position.latitude == 0.5786150090711938






# - Zone :
#   - récupérer un coin inférieur gauche (corner1)
#   - récupérer un coin supérieur droit (corner2)
#   - modifier un coin inférieur gauche (corner1)
#   - modifier un coin supérieur droit (corner2)
#   - trouver une zone qui contient une position
#   - ajouter un habitant dans une zone
#   - récupérer toutes les instances Zone (Zone.ZONES)
#   - récupérer la densité de population d'une zone
#   - récupérer l'agréabilité moyenne d'une zone
#   - récupérer le revenu moyen d'une zone
#   - récupérer l'âge moyen d'une zone

# - AgreeablenessGraph :
#   - récupérer un titre
#   - récupérer x_label
#   - récupérer y_label
#   - récupérer xy_values sous forme de tuples
#   - la première valeur de xy_values est la densité de population moyenne
#   - la seconde valeur de xy_values est l'agréabilité moyenne

# - IncomeGraph :
#   - récupérer un titre
#   - récupérer x_label
#   - récupérer y_label
#   - récupérer xy_values sous forme de tuples
#   - la première valeur de xy_values est le revenu
#   - la seconde valeur de xy_values est l'âge