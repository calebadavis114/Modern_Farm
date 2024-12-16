from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Animals

# Create your tests here.
class animals_test(TestCase):

    def test_01_create_animal_instance(self):
        # Valid animal instance (assuming 'cow' is a valid name)
        new_animal = Animals(name='Cow')
        
        try:
            new_animal.full_clean()  # This will run validation checks
            self.assertIsNotNone(new_animal)  # Assert that the animal instance is created
        except ValidationError:
            self.fail("ValidationError was raised unexpectedly.")
        
    def test_02_create_animal_with_invalid_name(self):
        # Invalid animal instance (empty name or improperly formatted name)
        new_animal = Animals(name='392ieid')
        
        # Assert that a ValidationError is raised
        with self.assertRaises(ValidationError):
            new_animal.full_clean()