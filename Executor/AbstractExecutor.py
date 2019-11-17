class AbstractExecutor:

    def __init__(self, confs=None):
        self.confs = confs

    def execute(self, objects):
        """
        process the objects
        :param objects: list of objects to process.
        :return: null
        """

        raise NotImplementedError