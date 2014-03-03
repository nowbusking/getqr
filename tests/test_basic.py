import pytest
import filecmp

from app import app

class TestBasic:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """

        app.config['TESTING'] = True
        self.app = app.test_client()


    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """

    def test_canonical_sample(self):
        rv = self.app.get('/qr?chl=Hello+World&chs=200x200')

        # Make sure you get the right status code
        assert rv.status_code == 200

        # Then the correct result
        with open('tests/helloworld.png') as f:
            assert rv.data == f.read()

