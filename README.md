# mkdocs-material

Based on [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

Main contents are in `docs/*.md`

## some commands

- with mkdocs ( Installed by `pip install mkdocs-material` )
  - `mkdocs serve`
  - `mkdocs serve --dirtyreload`
    - for quick and partial build
  - `mkdocs build`
  - `cd site; python -m http.server`
    - serve built site
- with docker compose
  - serve: `docker compose up`
  - serve dirty reload: `docker compose run --rm -it app serve --dirtyreload`
  - build: `docker compose run --rm -it app build`
  - serve built site: `docker compose run --rm -it --entrypoint python app -m http.server`
