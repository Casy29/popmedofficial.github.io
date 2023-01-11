import os, sys

###########################ADDON############################
try:
    import easydev
    from easydev import get_path_sphinx_themes
except
    print "Install easydev or set your PYTHONPATH properly"
    raise Exception


version = "0.9.3"
release = "0.9"
project = u'Sphinx and the RST syntax'