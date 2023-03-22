from prototype_auto_cloud.data.report import TypeReport
import allure


class Report:
    def __init__(self) -> None:
        self.result = ''
        pass

    def create(self, type_report: TypeReport):
        with allure.step(f'Create {type_report.value}'):
            self.result = 'create'
        return self

    def shoud_result(self, result):
        with allure.step('Should created report'):
            assert result == self.result
        return self
