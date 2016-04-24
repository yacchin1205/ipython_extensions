def _jupyter_server_extension_paths():
    return [{
        "module": "nbextension_toc"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        src="static",
        dest="nbextension_toc",
        require="nbextension_toc/toc")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("ToC nbextension enabled!")