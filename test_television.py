import unittest
from television import *

class TestTelevision(unittest.TestCase):
    """
    sets up testing class for television
    """
    def setUp(self):
        """
        sets up a class in television
        :return: None
        """
        self.t1 = Television()

    def tearDown(self):
        """
        tears down a class from television
        :return: None
        """
        del self.t1
    def test_init(self):
        """
        tests if television original variables apply
        :return: None
        """
        self.assertEqual(self.t1.__str__(),'Power = False, Channel = 0, Volume = 0')

    def test_power(self):
        """
        tests values when power is off then on
        :return: None
        """
        self.assertEqual(self.t1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.t1.power()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 0')

    def test_mute(self):
        """
        tests when power is on,volume is up 1, then muted
        tests when unmuted
        tests when muted then turned off
        tests when turned if it can be muted
        :return: None
        """
        self.t1.power()
        self.t1.volume_up()
        self.t1.mute()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 0')
        self.t1.mute()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 1')
        self.t1.mute()
        self.t1.power()
        self.assertEqual(self.t1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.t1.mute()
        self.assertEqual(self.t1.__str__(), 'Power = False, Channel = 0, Volume = 0')

    def test_channel_up(self):
        '''
        tests when tv is off then channel up 1
        tests when tv is on then channel up 1
        tests when channel is maxed then increased
        :return: None
        '''
        self.t1.channel_up()
        self.assertEqual(self.t1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.t1.power()
        self.t1.channel_up()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 1, Volume = 0')
        self.t1.channel_up()
        self.t1.channel_up()
        self.t1.channel_up()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 0')

    def test_channel_down(self):
        """
        Tests when tv is off and channel down 1
        Tests when tv is on and channel down from minimum
        :return: None
        """
        self.t1.channel_down()
        self.assertEqual(self.t1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.t1.power()
        self.t1.channel_down()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 3, Volume = 0')

    def test_volume_up(self):
        """
        Tests when tv is off then volume up 1
        Tests when tv is on then volume up 1
        Tests when tv is muted then volume up 1
        Tests when volume up when maxed
        :return: None
        """
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.t1.power()
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 1')
        self.t1.mute()
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 2')
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 2')

    def test_volume_down(self):
        """
        Tests when tv is off and volume down 1
        Tests when tv is on and volume down 1 after maxed
        Tests when muted then volume down 1
        Tests when volume down 1 at minimum
        :return: None
        """
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.t1.power()
        self.t1.volume_up()
        self.t1.volume_up()
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 1')
        self.t1.mute()
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 0')
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'Power = True, Channel = 0, Volume = 0')







if __name__ == '__main__':
    unittest.main()