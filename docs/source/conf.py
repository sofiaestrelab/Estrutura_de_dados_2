import os
import sys

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.abspath('.'))

# Informações projeto
project = 'Estrutura de Dados 2'
copyright = '2026, Ciências da Computação, Sofia Estrela Bernardes'
author = 'Sofia Estrela Bernardes'

release = '2.0'
version = '2.0'

# Extensões
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

language = 'pt_BR'

# Caminhos
templates_path = ['_templates']
html_static_path = ['_static']

# HTML output
html_theme = 'sphinx_rtd_theme'

# Não incluir arquivos de build
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Arquivo principal
master_doc = 'index'

# Source file patterns
source_suffix = '.rst'

# html_theme_options = {
#     'logo_only': False,
#     'display_version': True,
# }
