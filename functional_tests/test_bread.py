from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random
import datetime



# Based on this number, what should the day and slot be?
random = random.randrange(0,14) # There are 7 days and 2 slots per day, so we need to choose a random order link
today = datetime.date.today()
corresponding_day = today + datetime.timedelta(days=random // 2)
if random % 2 == 0:
    corresponding_slot = 'morning'
else:
    corresponding_slot = 'evening'

class MakeOrders(FunctionalTest):

    def test_order_slot_and_date_corresponds_with_location_in_table_from_which_is_choosen(self):
        self.browser.get(self.server_url + '/bread')

        # Our user chooses a order slot and date
        self.browser.find_elements_by_link_text('Order')[random].click()

        # Then they see that the forms is prepopulated correctly
        form_order_slot_prepop_text = self.browser.find_element_by_id('id_order_slot').get_attribute('value')
        form_order_date_prepop_text = self.browser.find_element_by_id('id_order_date').get_attribute('value')
        self.assertEqual(form_order_date_prepop_text, corresponding_day.isoformat()) # Set the format to match that displayed on the page
        self.assertEqual(form_order_slot_prepop_text, corresponding_slot)



    def test_6_orders_and_order_link_disappears(self):
        # After our users make 6 orders for a particular slot, say morning, the link should disappear.
        self.browser.get(self.server_url + '/bread')

        # They make 6 orders for today, morning, this should be the first such link
        for i in range(6):
            self.browser.find_elements_by_link_text('Order')[0].click()
            self.browser.find_element_by_id('id_customer').send_keys('testcustomer')
            self.browser.find_element_by_id('id_order_details').send_keys('test')
            self.browser.find_element_by_id('save_btn').click()

        # Now check the link is gone, and now says, no orders
        table_option = self.browser.find_elements_by_tag_name('td')[1].text
        self.assertEqual(table_option, "Sorry, all loafs are reserved")
