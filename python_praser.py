from HTMLParser import HTMLParser


class AllLanguages(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inLink = False
        self.dataArray = []
        self.countLanguages = 0
        self.lasttag = None
        self.lastname = None
        self.lastvalue = None

    def handle_starttag(self, tag, attrs):
        self.inLink = False
        if tag == 'a':
            for name, value in attrs:
                if name == 'class' and value == 'Vocabulary':
                    self.countLanguages += 1
                    self.inLink = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "a":
            self.inlink = False

    def handle_data(self, data):
        if self.lasttag == 'a' and self.inLink and data.strip():


parser = AllLanguages()
parser.feed("""
<html>
<head><title>Test</title></head>
<body>

<a href="http://wold.livingsources.org/vocabulary/1" title="Swahili" class="Vocabulary">Swahili</a>
<a href="http://wold.livingsources.org/contributor#schadebergthilo" title="Thilo Schadeberg" class="Contributor">Thilo Schadeberg</a>
<a href="http://wold.livingsources.org/vocabulary/2" title="English" class="Vocabulary">English</a>
<a href="http://wold.livingsources.org/vocabulary/2" title="Russian" class="Vocabulary">Russian</a>
</body>
</html>""")