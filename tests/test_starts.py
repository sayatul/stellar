import pytest
import stellar
import tempfile


class TestCase(object):
    @pytest.yield_fixture(autouse=True)
    def config(self):
        self._config = stellar.config.config
        with tempfile.NamedTemporaryFile() as tmp:
            new_config = {
                'stellar_url': 'sqlite://%s' % tmp.name,
                'url': 'sqlite://%s' % tmp.name,
                'project_name': 'test_project',
                'tracked_databases': ['test_database'],
                'TEST': True
            }
            stellar.config.config = new_config
            yield
        stellar.config.config = self._config


class Test(TestCase):
    def test_setup_method_works(self):
        assert stellar.config.config['TEST']

    def test_shows_not_enough_arguments(self):
        with pytest.raises(SystemExit) as e:
            stellar.command.main()