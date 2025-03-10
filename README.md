# mkdocs-asyncapi-plugin

The `mkdocs-asyncapi-tag-plugin` helps render AsyncAPI schemas in your MkDocs markdown pages. It uses the AsyncAPI Standalone React component to render your AsyncAPI schema files. This plugin supports both `.json` and `.yml` files.

## Installation

To install the plugin, run:

```sh
pip install mkdocs-asyncapi-tag-plugin
```

Then, include the plugin in the `plugins` property of your `mkdocs.yml` file:

```sh
    plugins:
        - asyncapi-tag
```

## Usage

To render your schema, use the <asyncapi-tag> in your markdown files:

```HTML
    <asyncapi-tag src="/path/to/schema.json"/>
```

## Accepted values
In addition to the `src` attribute, the following attributes can be used with the `<asyncapi-tag>`:

| Action | Attribute | Accepted values |
|---|---|---|
| Show or hide | `sidebar` | `true` or `false` |
| Show or hide | `info` | `true` or `false` |
| Show or hide | `servers` | `true` or `false` |
| Show or hide | `operations` | `true` or `false` |
| Show or hide | `messages` | `true` or `false` |
| Show or hide | `schemas` | `true` or `false` |
| Show or hide | `errors` | `true` or `false` |
| expand or collapse | `messageExamples` | `true` or `false` |
| sidebar configuration| `showServers` | `byDefault` or `bySpecTags` or `byServersTags` |
| sidebar configuration| `showOperations` | `byDefault` or `bySpecTags` or `byServersTags` |
| asyncapi parser configuration | `parserOptions` | See available [options here](https://github.com/asyncapi/parser-js/blob/master/API.md#module_@asyncapi/parser..parse) |
| label customization | `publishLabel` | Any string value |
| label customization | `subscribeLabel` | Any string value |