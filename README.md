# Fishlib

`fishlib` is the package

`communication` and `movement` are subpackages

`communication.py`, `utils.py`, etc. are modules

## Install

`python setup.py develop`

This installs the fishlib package locally (like pip) so it can be used anywhere. Using `develop` means that you can keep editing the code and the globally installed version will automagically use that.

## Usage

After installation you can used it like this

### Import the main package utils:

- `from fishlib import utils` -> `utils.set_color('blue')` (creates ambiguity)
- `import fishlib.utils` -> `fishlib.utils.set_color('blue')`
- `import fishlib.utils as fish_utils` -> `fish_utils.set_color('blue')`

### Import a subpackage:

- `from fishlib import movement` -> `movement.utils.move('left')`, `movement.move_left()`
  (This is what I usually do)
- `import fishlib.movement` -> `fishlib.movement.utils.move('left')`, `fishlib.movement.move_left()`


## Best practice

- Using a lot of imports in the `__init__` files makes it hard to keep track of structure
- Keep everything contained to a virtual environment (easier to keep track of stuff/permissions even if it's the only thing you're using)
- Avoid wildcard imports (e.g., `from utils import *`) because it obfuscates the source of the code and can cause conflicts