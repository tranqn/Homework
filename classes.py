class Certificate:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Certificate('{}')".format(self.name)