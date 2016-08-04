from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_view_and_navigate_homepage(self):
        # Our user wants to scope out the information available,
        # so they stop by our site
        self.browser.get(self.server_url)

        # She sees the header, titlebar, and a list of news events
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('theDatabase', header_text)

        link = self.browser.find_element_by_link_text('My Beliefs').text
        self.assertEqual('My Beliefs', link)


    def test_can_navigate_to_organizations_page(self):
        # She notices a link to learn more about individual organizations, clicks it
        self.browser.get(self.server_url)
        self.browser.find_element_by_link_text('Organizations').click()

        # Now she sees the various organizations
        page_header = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Learn more about how your products are created.', page_header)

        # Todo
        self.fail('TODO')
