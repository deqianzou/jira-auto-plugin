from AbstractFetcher import AbstractFetcher

from jira import JIRA

PROJECT_NAME = "project.name"

class UnassignedIssueFetcher(AbstractFetcher):

    def __init__(self, client, confs=None):
        print 'Fetcher instance: UnassignedIssueFetcher'
        self.client = client
        self.confs = confs

    def fetch(self):
        """
        :return: list of unassigned issue.
        """
        print "fetching unassigned issue"
        project = self.confs.get(PROJECT_NAME)[0]
        issues = self.client.search_issues('project={project} and assignee = null'.format(project=project))
        print "fetch done"
        return issues
