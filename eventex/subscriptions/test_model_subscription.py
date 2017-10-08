from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionMOdelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Victor Acioly',
            cpf = '12345678901',
            email = 'victor_acioly@hotmail.com',
            phone = '84-99653-0011'
        )

        self.obj.save () #Criando uma linha no banco de dados
        def test_create(self):
            self.assertTrue(Subscription.objects.exists())

        def test_created_at(self):
            """"Subscription must have an auto created_at attr."""
            if __name__ == '__main__':
                self.assertInstance(self.obj.created_at,datetime)

