class AbstractFetcher:

    def __init__(self, confs=None):
        self.confs = confs

    def fetch(self, config):
        """
        fetch objects.
        :config: Configuration. user configuration
        :return: list of objects (typically issues)
        """

        raise NotImplementedError