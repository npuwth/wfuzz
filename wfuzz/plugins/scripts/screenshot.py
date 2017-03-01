from wfuzz.plugin_api.base import BasePlugin
from wfuzz.externals.moduleman.plugin import moduleman_plugin

import subprocess
import tempfile
import pipes

@moduleman_plugin
class screenshot(BasePlugin):
    name = "screenshot"
    author = ("Xavi Mendez (@xmendez)",)
    version = "0.1"
    summary = "Performs a screen capture using linux cutycapt tool"
    category = ["active"]
    priority = 99
    
    def validate(self, fuzzresult):
	return fuzzresult.code not in [404]

    def process(self, fuzzresult):
	(fd, filename) = tempfile.mkstemp()

	subprocess.call(['cutycapt', '--url=%s' % pipes.quote(fuzzresult.url), '--out=%s.png' % filename])
	self.add_result("Screnshot taken, output at %s.png" % filename)