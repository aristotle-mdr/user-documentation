from sphinx.writers.html import HTMLWriter, HTMLTranslator
from sphinx.builders.html import StandaloneHTMLBuilder


from sphinx.locale import admonitionlabels, _, __
from docutils import nodes

class AHTML(HTMLTranslator):
    def visit_admonition(self, node, name=''):
        # type: (nodes.Element, str) -> None
        
        admonition_map = {
            "note": "info",
            "hint": "warning",
            "warning": "danger",
        }
        
        admon_class = admonition_map.get(name, "dark")
        self.body.append(self.starttag(
            node, 'div', CLASS=('admonition alert alert-' + admon_class)))
        if name:
            node.insert(0, nodes.title(name, admonitionlabels[name]))
        self.set_first_last(node)


class ABuilder(StandaloneHTMLBuilder):
    name = 'ahtml'
    default_translator_class = AHTML


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.set_translator(name="html", translator_class=AHTML)

    return {
        'version': 1,
    }