{% set title = "Welcome to {}'s documentation!".format(cookiecutter.project_name) -%}
{% for _ in title %}={% endfor %}
{{ title }}
{% for _ in title %}={% endfor %}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   modules

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
