
def setup(app):
    app.add_directive('screenshot', ScreenshotNoopDirective)
    return {'version': '0.1'}   # identifies the version of our extension


from docutils.parsers.rst import Directive

class ScreenshotNoopDirective(Directive):
    has_content = True

    def run(self):
        return []
