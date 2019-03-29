import unittest

from twitter_fire_scraper.scraper import Scraper
from twitter_fire_scraper.twitter import TwitterAuthentication
from pymongo import MongoClient


class TestSimpleScraping(unittest.TestCase):

    def testCanScrapeTerm(self):
        """Tests that scraper can scrape one term."""

        twauth = TwitterAuthentication.autodetect_twitter_auth()

        scraper = Scraper(twitter_authentication=twauth)

        results = scraper.scrape_terms({"fire"}, count=1)

        assert('fire' in results)

        assert(isinstance(results['fire'], list))

        assert (len(results.keys()) == 1)

        assert (isinstance(results['fire'][0].text, str))

    def testCanScrapeAccount(self):
        """Tests that scraper can scrape one account."""
        twauth = TwitterAuthentication.autodetect_twitter_auth()

        scraper = Scraper(twitter_authentication=twauth)

        results = scraper.scrape_accounts({"@RedCross"}, count=1)

        assert ('@RedCross' in results)

        assert (len(results.keys()) == 1)

        assert(isinstance(results['@RedCross'], list))

        assert (isinstance(results['@RedCross'][0].text, str))

    def testCanScrapeMethod(self):
        """Tests that the Scraper's `scrape` method works."""

        twauth = TwitterAuthentication.autodetect_twitter_auth()

        scraper = Scraper(twitter_authentication=twauth)

        results = scraper.scrape(terms={"fire"}, accounts={"@RedCross"})

        assert('fire' in results.keys())
        assert('@RedCross' in results.keys())

        assert(len(results.keys()) == 2)

        assert(isinstance(results['fire'], list))
        assert(isinstance(results['@RedCross'], list))

    def testCanScrapeAndSave(self):
        """Tests if the Scraper can both scrape and save the results to a MongoDB database"""

        # Before starting, if the test database exists, remove it
        # TODO: standardize localhost string
        test_client = MongoClient()
        test_db = "testdb"
        test_client.drop_database(test_db)

        twauth = TwitterAuthentication.autodetect_twitter_auth()

        scraper = Scraper(twitter_authentication=twauth)

        results = scraper.scrape_and_save(terms={"fire"}, count=1, dbname="testdb")

        print(results)

        assert ('fire' in results.keys())

        assert (len(results.keys()) == 1)

        assert (isinstance(results['fire'], list))

        assert (test_client[test_db].get_collection("fire").count() == 1)
        test_client.drop_database(test_db)
