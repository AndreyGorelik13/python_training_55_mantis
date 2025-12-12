import random
import string

from model.project import Project

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_new_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    project = Project(name=random_string("Project", 10), description=random_string("description",10))
    old_projects = app.soap.get_project_list(username, password)
    app.project.create_project(project)
    new_projects = app.soap.get_project_list(username, password)
    for p in new_projects:
        if p.name == project.name:
            project.id = p.id
            break
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)