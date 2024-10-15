from setuptools import setup, find_packages

setup(
    name='mkdocs-asyncapi-tag-plugin',
    version='1.0.0',
    description='MkDocs plugin to embed AsyncAPI HTML viewer in your markdown file.',
    author='Weesho Lapara',
    author_email='support@weesholapara..com',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.0.4',
        'beautifulsoup4>=4.6.0',
    ],
    entry_points={
        'mkdocs.plugins': [
            'asyncapi = mkdocs_asyncapi_tag_plugin.mkdocs_asyncapi_plugin:AsyncAPIPlugin',
        ]
    }
)