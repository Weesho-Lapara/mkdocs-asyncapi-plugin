import unittest
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from asyncapi_plugin import AsyncAPIPlugin

class TestAsyncAPIPlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = AsyncAPIPlugin()
        self.config = MkDocsConfig()
        self.config['docs_dir'] = 'docs'
        self.config['site_dir'] = 'site'
        self.config['use_directory_urls'] = False

    def test_on_files(self):
        files = Files([])
        self.plugin.config['asyncapi_file'] = 'schema.json'
        result = self.plugin.on_files(files, self.config)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].path, 'schema.json')

    def test_on_page_content(self):
        html = '<asyncapi-tag src="schema.json"></asyncapi-tag>'
        page = None
        files = None
        result = self.plugin.on_page_content(html, page, self.config, files)
        self.assertIn('schema.json', result)

if __name__ == '__main__':
    unittest.main()
