import random
import string

from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name=random_string("Project", 10), description=random_string("description",10)))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)






