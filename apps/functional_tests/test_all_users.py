from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase  
from django.utils.translation import activate
from datetime import date
from django.utils import formats


class HomeNewVisitorTest(LiveServerTestCase): 

    def setUp(self):
        activate('en')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        activate('en')
        self.browser.get(self.get_full_url("home"))
        self.assertIn("Home - django boilerplate App", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgb(33, 37, 41)")

    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)

    def test_internasionalization(self):
        for lang, h1_text in [('en', 'Hello World!'), ('id', 'Halo Dunia!')]:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h1 = self.browser.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, h1_text)
	
    def test_localization(self):
        today = date.today()
        for lang in ['en', 'id']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            local_date = self.browser.find_element_by_id("local-date")
            non_local_date = self.browser.find_element_by_id("non-local-date")
            self.assertEqual(formats.date_format(today, use_l10n=True),
                                local_date.text)
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)
