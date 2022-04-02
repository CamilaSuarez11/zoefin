import unittest
from zoefin.src import reschedule_page
from zoefin.utilities import utilities


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = utilities
        self.zoefin = reschedule_page

    def test_reschedule(self):
        self.zoefin.click_date_reschedule()
        self.assertEqual(self.zoefin.validation_day(), "Wed, Apr 6th 2022")
        self.zoefin.select_time()
        self.assertEqual(self.zoefin.validation_time(), "1:00 pm")
        self.zoefin.click_type_of_call()
        self.assertEqual(self.zoefin.validation_type_of_call(), "Phone Call")
        self.zoefin.click_reschedule()
        self.assertEqual(self.zoefin.validation_pop_up_window(), "Wednesday, Apr 6 2022")
        self.assertEqual(self.zoefin.validation_hour(), "1:30 PM - 2:30 PM EDT")
        self.assertEqual(self.zoefin.validation_duration(), "60 Minutes")
        self.assertEqual(self.zoefin.validation_type(), "Phone")
        self.zoefin.click_confirm()
        self.assertEqual(self.zoefin.validation_reschedule_successfully(), "Successfully rescheduled!")

    def tearDown(self):
        self.driver.close()
        if __name__ == '__main__':
            unittest.main()
