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
        agent = script.Agent(3, agreeableness=-1)
        assert agent.agreeableness == -1


#############################################
################# POSITION ##################
#############################################

class TestPosition:
    POSITIONTEST = script.Position(100, 33)
    # - Position :
    #   - modifier un attribut longitude_degrees
    def test_longitude_degrees(self):
        assert self.POSITIONTEST.longitude_degrees == 100

    #   - modifier un attribut latitude_degrees
    def test_latitude_degrees(self):
        assert self.POSITIONTEST.latitude_degrees == 33

    #   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur.
    def test_longitude_degrees_range(self):
        with pytest.raises(AssertionError):
            script.Position(200, 33)

    #   - modifier un attribut latitude_degrees avec une valeur supérieure à 90 renvoie une erreur.
    def test_latitude_degrees_range(self):
        with pytest.raises(AssertionError):
            script.Position(100, 100)

    #   - récupérer une longitude
    def test_longitude(self):
        assert self.POSITIONTEST.longitude == 1.7453292519943295

    #   - récupérer une latitude
    def test_latitude(self):
        assert self.POSITIONTEST.latitude == 0.5759586531581288


#############################################
################### ZONE ####################
#############################################

class TestZone:
    POSITION1 = script.Position(100, 33)
    POSITION2 = script.Position(101, 34)
    ZONE = script.Zone(POSITION1, POSITION2)

    # - Zone :
    def test_zone_that_contains(self):
        position = self.POSITION1
        found_zone = script.Zone.find_zone_that_contains(position)
        assert position.longitude >= min(found_zone.corner1.longitude, found_zone.corner2.longitude)
        assert position.longitude < max(found_zone.corner1.longitude, found_zone.corner2.longitude)
        assert position.latitude >= min(found_zone.corner1.latitude, found_zone.corner2.latitude)
        assert position.latitude < max(found_zone.corner1.latitude, found_zone.corner2.latitude)


    #   - trouver une zone qui contient une position
    def test_find_zone_that_contains(self):
        found_zone = script.Zone.find_zone_that_contains(self.POSITION1)
        assert found_zone.contains(self.POSITION1)

    #   - récupérer toutes les instances Zone (Zone.ZONES)
    # On devrait avoir exactement 64800 zones
    def test_get_zones(self):
        assert len(script.Zone.ZONES) == 64800

    #   - ajouter un habitant dans une zone
    def test_add_inhabitant_in_zone(self):
        agent = script.Agent(self.POSITION1, agreeableness=1)
        self.ZONE.add_inhabitant(agent)
        assert len(self.ZONE.inhabitants) == 1


    #   - récupérer la densité de population d'une zone
    def test_get_population_density(self):
        assert self.ZONE.population_density() == 8.087793508722422e-05

#   - récupérer l'agréabilité moyenne d'une zone
    def test_get_average_agreeableness(self):
        assert self.ZONE.average_agreeableness() == 1
