import unittest
import os
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs_asyncapi_tag.mkdocs_asyncapi_plugin import AsyncAPIPlugin

class TestAsyncAPIPlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = AsyncAPIPlugin()
        self.config = MkDocsConfig()
        self.config['docs_dir'] = 'docs'
        self.config['site_dir'] = 'site'
        self.config['use_directory_urls'] = False

        # Create a mock schema.json file
        os.makedirs(self.config['docs_dir'], exist_ok=True)
        with open(os.path.join(self.config['docs_dir'], 'schema.json'), 'w') as f:
            f.write('{}')

    def tearDown(self):
        # Clean up the mock file after tests
        os.remove(os.path.join(self.config['docs_dir'], 'schema.json'))

    def test_on_files(self):
        files = Files([])
        self.plugin.config['asyncapi_file'] = 'schema.json'
        result = self.plugin.on_files(files, self.config)
        
        # Check if the file was added to the Files object
        file_paths = [file.src_path for file in result]
        self.assertIn('schema.json', file_paths)

    def test_on_page_content(self):
        html = '<asyncapi-tag src="schema.json"></asyncapi-tag>'
        page = None
        files = None
        result = self.plugin.on_page_content(html, page, self.config, files)
        self.assertIn('schema.json', result)

if __name__ == '__main__':
    unittest.main()
