from models import Animal, Enclosure, Zookeeper

class TestAnimal:
    '''Class Animal in models.py'''

    def test_converts_to_dict(self):
        '''can convert Animal objects to dictionaries.'''
        a = Animal(name="Lion", species="Panthera leo", age=5)
        animal_dict = a.to_dict()
        assert animal_dict
        assert isinstance(animal_dict, dict)
        assert animal_dict['name'] == "Lion"
        assert animal_dict['species'] == "Panthera leo"
        assert animal_dict['age'] == 5


class TestEnclosure:
    '''Class Enclosure in models.py'''

    def test_converts_to_dict(self):
        '''can convert Enclosure objects to dictionaries.'''
        e = Enclosure(name="Savannah", size=1000)
        enclosure_dict = e.to_dict()
        assert enclosure_dict
        assert isinstance(enclosure_dict, dict)
        assert enclosure_dict['name'] == "Savannah"
        assert enclosure_dict['size'] == 1000


class TestZookeeper:
    '''Class Zookeeper in models.py'''

    def test_converts_to_dict(self):
        '''can convert Zookeeper objects to dictionaries.'''
        z = Zookeeper(name="John Doe", age=30)
        zookeeper_dict = z.to_dict()
        assert zookeeper_dict
        assert isinstance(zookeeper_dict, dict)
        assert zookeeper_dict['name'] == "John Doe"
        assert zookeeper_dict['age'] == 30
