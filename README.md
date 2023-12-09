
## Pydoc
Similar to the functionality of Perldoc within Perl and Javadoc within Java
<pre>
Pros:
  Part of the standard Python library, no additional installation required.
  Simple and straightforward for basic documentation needs.
Cons:
  Very basic, lacks features of more developed tools like Sphinx.
  Primarily for generating simple text or HTML pages.
</pre>

## Sphinx
<pre>
  Pros:
   Highly customizable and extensible.
   Supports reStructuredText with additional features specific to documentation.
   Integrated with Read the Docs for easy hosting.
   Supports autodoc for pulling documentation from docstrings.
   Can generate output in multiple formats, including HTML, PDF, and ePub.
Cons:
  Steeper learning curve due to its extensive features.
  reStructuredText can be more complex compared to Markdown.
</pre>

## MkDocs
<pre>
  Pros:
    Simple and easy to use.
    Uses Markdown, which is easier for many people compared to reStructuredText.
    Wide range of themes and plugins.
    Live preview server for documentation writing.

  Cons:
    Less customizable in comparison to Sphinx.
    Lacks some advanced features like automatic docstring integration.
</pre>


## Doxygen
<pre>
  Pros:
    Good for multi-language projects (C++, C, Java, Python, etc.).
    Can generate documentation from source code and comments.
    Supports various output formats.

  Cons:
    Less Python-specific features compared to Sphinx.
    The generated documentation style might feel outdated.

</pre>

## pdoc3
<pre>
  Pros:
    Lightweight and easy to use.
    Automatically generates API documentation from Python docstrings.
    Supports Markdown in docstrings.

  Cons:
    Less feature-rich and less customizable compared to Sphinx.
</pre>

## Our choice for python documentation is Sphinx
Sphinx is de facto standard for Python documentation, 
especially for larger projects or projects that require extensive customization
and advanced features.

However, for simpler needs or a preference for Markdown support, MkDocs or pdoc3 could be more suitable.

## Project structure
-  `tree -I 'venv'`
<pre>
py_and_docs/
        ├── README.md
        ├── docs
        │   ├── conf.py
        │   └── index.rst
        ├── py_docs_example
        │   ├── __init__.py
        │   ├── calc
        │   │   ├── __init__.py
        │   │   └── calculator.py
        │   └── utils
        │       ├── __init__.py
        │       └── string_utils.py
        ├── setup.py
        ├── sphinx-setup.md

</pre>

## See here, [Sphinx setup](sphinx-setup.md)

## Typical buildspec.yml
- **Install phase:** Sets the Python version to 3.10 and installs dependencies. Make sure your requirements.txt file includes all the necessary packages for your project.
- **Pre-build phase:** This is a placeholder for any steps you might want to run before the actual build process.
- **Build phase:** Generates the Sphinx documentation. Adjust the sphinx-build command to match your project's source and build directories.
- **Post-build phase:** A simple echo command to signify the end of the build process.
- **Artifacts:** Specifies the files to be output by the build process. This should include your Sphinx-generated HTML files.
- **Environment Variables:** This section is optional and can be used to define any environment variables needed for your build.

