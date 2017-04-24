from world.script import *
import pytest

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    pass

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """
    pass
    
def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('Celine') == 'Hello Celine'


#############################################
################## AGENT ####################
#############################################

class TestAgent:
    AGENTTEST = Agent(3)
    # - Agent : 
    #   - récupérer un attribut position
    def test_set_position(self):
        self.AGENTTEST.position = 5
        assert self.AGENTTEST.position == 5

    #   - modifier un attribut position
    def test_get_position(self):
        assert self.AGENTTEST.position == 5

    #   - assigner un dictionnaire en tant qu'attributs
    def test_set_agent_attributes(self):
        dictionary = {"agreeableness": -0.8437190198916452}
        agent = Agent(3, **dictionary)
        assert agent.agreeableness == -0.8437190198916452


#############################################
################# POSITION ##################
#############################################

class TestPosition:
    POSITIONTEST = Position(100.85840672174572, 33.15219798270325)
    # - Position :
    #   - modifier un attribut longitude_degrees
    def test_longitude_degrees(self):
        assert self.POSITIONTEST.longitude_degrees == 100.85840672174572

    #   - modifier un attribut latitude_degrees
    def test_latitude_degrees(self):
        assert self.POSITIONTEST.latitude_degrees == 33.15219798270325

    #   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur. 
    def test_longitude_degrees_range(self):
        with pytest.raises(AssertionError):
            position = Position(200.85840672174572, 33.15219798270325)

    #   - modifier un attribut latitude_degrees avec une valeur supérieure à 90 renvoie une erreur. 
    def test_latitude_degrees_range(self):
        with pytest.raises(AssertionError):
            position = Position(100.85840672174572, 100.15219798270325)

    #   - récupérer une longitude
    def test_longitude(self):
        assert self.POSITIONTEST.longitude == 1.7603112756100432

    #   - récupérer une latitude
    def test_latitude(self):
        assert self.POSITIONTEST.latitude == 0.5786150090711938


#############################################
################### ZONE ####################
#############################################

class TestZone:
    POSITION1 = Position(100, 33)
    POSITION2 = Position(101, 34)
    ZONETEST = Zone(POSITION1, POSITION2)
    AGENT = Agent(POSITION1, **{"agreeableness": -0.8437190198916452})

    # - Zone :
    #   - récupérer un coin inférieur gauche (corner1)
    def test_zone_corner1(self):
        assert self.ZONETEST.corner1 == self.POSITION1

    #   - récupérer un coin supérieur droit (corner2)
    def test_zone_corner2(self):
        assert self.ZONETEST.corner2 == self.POSITION2

    #   - trouver une zone qui contient une position
    def test_find_zone_that_contains(self):
        found_zone = Zone.find_zone_that_contains(self.POSITION1)
        assert found_zone.corner1.longitude == self.ZONETEST.corner1.longitude

    #   - ajouter un habitant dans une zone
    def test_add_inhabitant_in_zone(self):
        init = self.ZONETEST.inhabitants
        self.ZONETEST.add_inhabitant(self.AGENT)
        assert len(self.ZONETEST.inhabitants) == 1

    #   - récupérer toutes les instances Zone (Zone.ZONES)
    # On devrait avoir exactement 64800 zones
    def test_get_zones(self):
        assert len(Zone.ZONES) == 64800

    #   - récupérer la densité de population d'une zone
    def test_get_population_density(self):
        assert self.ZONETEST.population_density() == 8.087793508722422e-05

#   - récupérer l'agréabilité moyenne d'une zone
    def test_get_average_agreeableness(self):
        assert self.ZONETEST.average_agreeableness() == -0.8437190198916452


class TestAgreeablenessGraph:
    TESTGRAPH = AgreeablenessGraph()
# - AgreeablenessGraph :

#   - récupérer un titre
    def test_title(self):
        assert self.TESTGRAPH.title == 'Nice people live in the countryside'

#   - récupérer x_label
    def test_x_label(self):
        assert self.TESTGRAPH.x_label == 'population density'

#   - récupérer y_label
    def test_y_label(self):
        assert self.TESTGRAPH.y_label == 'agreeableness'

#   - récupérer xy_values sous forme de tuples
    def test_xy_values(self):
        pass
        #assert len(self.XY_VALUES) == 2

#   - la première valeur de xy_values est la densité de population moyenne pour la première zone
    def test_average_population_density(self):
        # Initialize zones
        zone = Zone.ZONES[0]
        graph = AgreeablenessGraph()
        # # Add inhabitants
        for _ in range(0, 10):
            zone.add_inhabitant(Agent(Position(-180, -89), **{"agreeableness": -0.8437190198916452}))
        a = graph.xy_values(Zone.ZONES)
        assert graph.xy_values(Zone.ZONES)[0][0] == zone.population_density()

#   - la seconde valeur de xy_values est l'agréabilité moyenne
    def test_average_agreeableness(self):
        # Initialize zones
        zone = Zone.ZONES[0]
        graph = AgreeablenessGraph()
        # # Add inhabitants
        for _ in range(0, 10):
            zone.add_inhabitant(Agent(Position(-180, -89), **{"agreeableness": -0.8437190198916452}))
        a = graph.xy_values(Zone.ZONES)
        assert graph.xy_values(Zone.ZONES)[1][0] == zone.average_agreeableness()
