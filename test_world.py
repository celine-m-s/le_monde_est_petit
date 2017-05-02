import program.world as script
import pytest

def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('Celine') == 'Hello Celine'

# - Agent : 
#   - récupérer un attribut position
def test_set_position():
    agent = script.Agent(3)
    agent.position = 5
    assert agent.position == 5

#   - modifier un attribut position
def test_get_position():
    agent = script.Agent(3)
    assert agent.position == 3

#   - assigner un dictionnaire en tant qu'attributs
def test_set_agent_attributes():
    agent = script.Agent(3, agreeableness=1)
    assert agent.agreeableness == 1

# - Position :
#   - modifier un attribut longitude_degrees
def test_longitude_degrees():
    position = script.Position(100, 34)
    assert position.longitude_degrees == 100

#   - modifier un attribut latitude_degrees
def test_latitude_degrees():
    position = script.Position(100, 34)
    assert position.latitude_degrees == 34

#   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur. 
def test_longitude_degrees_range():
    with pytest.raises(AssertionError):
        position = script.Position(200, 33)

#   - modifier un attribut latitude_degrees avec une valeur supérieure à 90 renvoie une erreur. 
def test_latitude_degrees_range():
    with pytest.raises(AssertionError):
        position = script.Position(100, 100)

#   - récupérer une longitude
def test_longitude():
    position = script.Position(100, 33)
    # print('longitude', position.longitude)
    assert position.longitude == 1.7453292519943295

#   - récupérer une latitude
def test_latitude():
    position = script.Position(100, 33)
    # print('latitude', position.latitude)
    assert position.latitude == 0.5759586531581288






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