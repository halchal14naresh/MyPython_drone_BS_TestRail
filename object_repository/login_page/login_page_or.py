from object_repository.base_page.base_or import BasePageOR



class LoginPageOR(BasePageOR):

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        super().__init__(driver=self.driver, log=self.log)
