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
    - serve dirty reload: `docker compose run --rm -it app -c mkdocs serve --dirtyreload`
    - build: `docker compose run --rm -it app build`
    - serve built site: `docker compose run --rm -it app -c python -m http.server`

## pip package management

This project using `pip-compile-multi`.

Please maintenance `requirements/requirements.in` and run `pip-compile-multi --live` to update `requirements/requirements.txt`.

Then, you can install updated `requirements/requirements.txt` by `pip install -r requirements/requirements.txt`.

It can be run with docker compose like below:

```
docker compose run --rm -it app -c 'pip-compile-multi --live'
cp requirements/requirements.txt docker/
docker compose build app
```
