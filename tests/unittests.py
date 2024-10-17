import unittest
from mkdocs_asyncapi_tag.mkdocs_asyncapi_plugin import AsyncAPIPlugin

class TestSimple(unittest.TestCase):
    def test_module_path(self):
        path = AsyncAPIPlugin.getModulePath()
        print(path)
        self.assertEqual(testModule.name, "test-module")
    if __name__ == '__main__':
        unittest.main()