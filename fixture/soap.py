from suds.client import Client
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self, username, password):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
        project_data = client.service.mc_projects_get_user_accessible(username, password)
        projects = []

        for p in project_data:
            projects.append(
                Project(
                    id=int(p.id),
                    name=p.name,
                    description=p.description if p.description else ""
                )
            )
        return projects