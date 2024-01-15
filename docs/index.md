# Welcome to MkDocs (Chapter 0 index)

For full documentation visit [mkdocs.org](https://www.mkdocs.org) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## toctree samples

{{ toctree('.') }}

## toc ?

{% for page in navigation.pages %}
- {{ page.title }}, {{ page.file }}, {{ page.url }}, {{ page.file.src_uri }}
{% endfor %}

<!-- ## macro info -->

<!-- macros_info() -->
