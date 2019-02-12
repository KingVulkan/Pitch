import unittest
from app.models import Pitch,User
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_manow = User(username = 'manow',password = '1234')
        self.new_pitch = Pitch(name='zee',title='Money',description='moneyreview',user =self.user_manow, category='Finance')

    # def tearDown(self):
    #     Pitch.query.delete()
    #     User.query.delete()

    def test_check_instance_variable(self):
        self.assertEquals(self.new_pitch.name,'zee')
        self.assertEquals(self.new_pitch.title,'Money')
        self.assertEquals(self.new_pitch.description,'moneyreview')
        self.assertEquals(self.new_pitch.category, 'Finance')
        # self.assertEquals(self.new_pitch.user,self.user_manow)  

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitch) > 0)    