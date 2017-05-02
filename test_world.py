import program.world as script
import pytest
    
def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('Celine') == 'Hello Celine'


#############################################
################## AGENT ####################
#############################################

class TestAgent:
    AGENT = script.Agent(3)
    # - Agent : 
    #   - récupérer un attribut position
    def test_set_position(self):
        self.AGENT.position = 5
        assert self.AGENT.position == 5

    #   - modifier un attribut position
    def test_get_position(self):
        assert self.AGENT.position == 5

    #   - assigner un dictionnaire en tant qu'attributs
    def test_set_agent_attributes(self):
        agent = script.Agent(3, agreeableness=1)
        assert agent.agreeableness == 1


#############################################
################# POSITION ##################
#############################################

class TestPosition:
    POSITION = script.Position(100, 33)
    # - Position :
    #   - modifier un attribut longitude_degrees
    def test_longitude_degrees(self):
        assert self.POSITION.longitude_degrees == 100

    #   - modifier un attribut latitude_degrees
    def test_latitude_degrees(self):
        assert self.POSITION.latitude_degrees == 33

    #   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur. 
    def test_longitude_degrees_range(self):
        with pytest.raises(AssertionError):
            position = script.Position(200, 33)

    #   - modifier un attribut latitude_degrees avec une valeur supérieure à 90 renvoie une erreur. 
    def test_latitude_degrees_range(self):
        with pytest.raises(AssertionError):
            position = script.Position(100, 100)

    #   - récupérer une longitude
    def test_longitude(self):
        assert self.POSITION.longitude == 1.7453292519943295

    #   - récupérer une latitude
    def test_latitude(self):
        assert self.POSITION.latitude == 0.5759586531581288


#############################################
################### ZONE ####################
#############################################

class TestZone:
    POSITION1 = script.Position(100, 33)
    POSITION2 = script.Position(101, 34)
    ZONE = script.Zone(POSITION1, POSITION2)
    AGENT = script.Agent(POSITION1, agreeableness=1)

    # - Zone :
    #   - récupérer un coin inférieur gauche (corner1)
    def test_zone_corner1(self):
        assert self.ZONE.corner1 == self.POSITION1

    #   - récupérer un coin supérieur droit (corner2)
    def test_zone_corner2(self):
        assert self.ZONE.corner2 == self.POSITION2

    #   - trouver une zone qui contient une position
    def test_find_zone_that_contains(self):
        found_zone = script.Zone.find_zone_that_contains(self.POSITION1)
        assert found_zone.corner1.longitude == self.ZONE.corner1.longitude

    #   - ajouter un habitant dans une zone
    def test_add_inhabitant_in_zone(self):
        init = self.ZONE.inhabitants
        self.ZONE.add_inhabitant(self.AGENT)
        assert len(self.ZONE.inhabitants) == 1

    #   - récupérer toutes les instances Zone (Zone.ZONES)
    # On devrait avoir exactement 64800 zones
    def test_get_zones(self):
        assert len(script.Zone.ZONES) == 64800

    #   - récupérer la densité de population d'une zone
    def test_get_population_density(self):
        assert self.ZONE.population_density() == 8.087793508722422e-05

#   - récupérer l'agréabilité moyenne d'une zone
    def test_get_average_agreeableness(self):
        assert self.ZONE.average_agreeableness() == 1


class TestAgreeablenessGraph:
    GRAPH = script.AgreeablenessGraph()
# - AgreeablenessGraph :

#   - récupérer un titre
    def test_title(self):
        assert self.GRAPH.title == 'Nice people live in the countryside'

#   - récupérer x_label
    def test_x_label(self):
        assert self.GRAPH.x_label == 'population density'

#   - récupérer y_label
    def test_y_label(self):
        assert self.GRAPH.y_label == 'agreeableness'

#   - récupérer xy_values sous forme de tuples
    def test_xy_values(self):
        pass
        #assert len(self.XY_VALUES) == 2

#   - la première valeur de xy_values est la densité de population moyenne pour la première zone
    def test_average_population_density(self):
        # Initialize zones
        zone = script.Zone.ZONES[0]
        graph = script.AgreeablenessGraph()
        # # Add inhabitants
        for _ in range(0, 10):
            zone.add_inhabitant(script.Agent(script.Position(-180, -89), agreeableness=1))
        a = graph.xy_values(script.Zone.ZONES)
        assert graph.xy_values(script.Zone.ZONES)[0][0] == zone.population_density()

#   - la seconde valeur de xy_values est l'agréabilité moyenne
    def test_average_agreeableness(self):
        # Initialize zones
        zone = script.Zone.ZONES[0]
        graph = script.AgreeablenessGraph()
        # # Add inhabitants
        for _ in range(0, 10):
            zone.add_inhabitant(script.Agent(script.Position(-180, -89), **{"agreeableness": -0.8437190198916452}))
        a = graph.xy_values(script.Zone.ZONES)
        assert graph.xy_values(script.Zone.ZONES)[1][0] == zone.average_agreeableness()
