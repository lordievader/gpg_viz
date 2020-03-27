# GPG Visualize

This python library easily lets you visualize GPG pathfinder output from
https://pgp.cs.uu.nl/

## Requirements

These can easily be installed with `pipenv`. In the root of this repo run:

```
pipenv --three
pipenv install
```

## Usage

After installing the requirements the module can be used as follows:

```
pipenv run python3 -m gpg_viz <json-file>.json
```

This will create a `graph.png` in the current directory.
