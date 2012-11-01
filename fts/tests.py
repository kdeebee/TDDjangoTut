"""
This is the test information from the TDD tutorial.
- We use a LiveServerTestCase which is a new test case provided by Django 1.4, which starts up a test web server with our Django site on it, in a separate thread, for the tests to run against.
- The special methods setUp and tearDown are executed before and after each test. We're using them to start up and shut down our Selenium WebDriver browser instance.
- The implicitly_wait call tells webdriver to use a 3-second timeout when performing its actions - it doesn't slow things down though, because it's a maximum timeout: if Selenium can tell that the page has loaded and any javascript processing is done, it will move on before the end.

"""

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PollsTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/admin')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # She types in her username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)

        # her username and password are accepted, and she is taken to
        # the Site Administration page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # She now sees a couple of hyperlink that says "Polls"
        polls_links = self.browser.find_elements_by_link_text('Polls')
        self.assertEquals(len(polls_links), 2)

        # The second one looks more exciting, so she clicks it
        polls_links[1].click()

        # She is taken to the polls listing page, which shows she has
        # # no polls yet
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 polls', body.text)

        # She sees a link to 'add' a new poll, so she clicks it
        new_poll_link = self.browser.find_element_by_link_text('Add poll')
        new_poll_link.click()



        # TODO: use the admin site to create a Poll
        self.fail('finish this test')
