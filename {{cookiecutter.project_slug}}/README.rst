{% set is_open_source = cookiecutter.license != 'KB license' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

* Free software: {{ cookiecutter.license }}

