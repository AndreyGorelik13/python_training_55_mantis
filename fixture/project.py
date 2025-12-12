from selenium.webdriver.common.by import By

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        self.click_create_new_project_button()
        self.fill_project_firm(project)
        self.click_add_project_button()
        self.open_projects_page()
        self.project_cache = None

    def go_to_project_page(self):
        self.open_manage_page()
        self.open_projects_page()

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php") and len(wd.find_elements(By.XPATH, "//h4[normalize-space()='Site Information']")) > 0):
           wd.find_element(By.XPATH, "//span[normalize-space()='Manage']").click()

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements(By.XPATH, "//button[normalize-space()='Create New Project']")) > 0):
            self.open_manage_page()
            wd.find_element(By.XPATH, "//a[normalize-space()='Projects']").click()

    def click_create_new_project_button(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[normalize-space()='Create New Project']").click()

    def filling_project_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def click_add_project_button(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()

    def fill_project_firm(self, project):
        wd = self.app.wd
        self.filling_project_field_value("name", project.name)
        self.filling_project_field_value("description", project.description)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.go_to_project_page()
            self.project_cache = []
            for element in (wd.find_elements(By.XPATH, "(//div[@class='col-md-12 col-xs-12']//div[contains(@class,'widget-box widget-color-blue2')]//table[contains(@class,'table-striped')])[1]/tbody/tr")):
                cells = element.find_elements(By.TAG_NAME, "td")
                name  = cells[0].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        self.open_project_by_name(name)
        self.click_delete_project_button()
        self.click_confirmation_delete_project_button()
        self.open_projects_page()
        self.project_cache = None

    def open_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//tbody//tr//td//a[contains(text(),'%s')]" %name).click()

    def click_delete_project_button(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[normalize-space()='Delete Project']").click()

    def click_confirmation_delete_project_button(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
