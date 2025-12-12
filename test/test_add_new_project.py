import random
import string

from model.project import Project

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_new_project(app):
    project = Project(name=random_string("Project", 10), description=random_string("description",10))
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)