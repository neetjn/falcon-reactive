# falcon-reactive
Falcon plugin for handling reactive/async tasks with rxpy. ***This project is still experimental and has not been released for redistributed use.***

## About

**falcon-reactive** is an experimental plugin for the falcon Web/REST framework for Python. This project processes resources asynchronously using RxPy and includes automatic responders for checking job statuses.

## Use

This project should be compaitable with any version of Falcon. Support is available for both Python 2.7 and 3.4+.

**falcon-reactive** can be installed with pip like so:

```bash
pip install falcon-reactive
```

To ensure your resources are compatible, inherit from the provided resource:

```python
from falcon_reactive.resource import ReactiveResource


class MyResource(ReactiveResource):

  def on_get(self, req, res):
    ...

```

...

## Contributors

* **John Nolette** (john@neetgroup.net)

Contributing guidelines are as follows,

* Any new features added must also be unit tested in the `tests` subdirectory.
  * Branches for bugs and features should be structured like so, `issue-x-username`.
* Include your name and email in the contributors list.

---

Copyright (c) 2019 John Nolette Licensed under the MIT license.

