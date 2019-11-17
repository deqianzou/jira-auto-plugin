from AbstractExecutor import AbstractExecutor

SLAVE = 'slaves'

class LoopAssignExecutor(AbstractExecutor):

    def __init__(self, client, confs=None):
        print 'Executor instance: LoopAssignedExecutor'
        self.client = client
        self.confs = confs

    def execute(self, objects):
        """
        loop assign issues.
        :param objects:
        :return: null
        """
        print 'assigning issues looply'
        mod = len(objects)
        if 0==mod:
            print 'no ticket to assign.'
        else:
            slaves = self.confs.get(SLAVE)
            if not slaves:
                print '???? no slave?'
                return
            else:
                l = len(slaves)
                from datetime import datetime
                dt = datetime.now()
                t = dt.microsecond % l
                while objects:
                    issue = objects.pop()
                    self.client.assign_issue(issue, slaves[t])
                    t += 1
                    t %= l
        print 'assign done.'