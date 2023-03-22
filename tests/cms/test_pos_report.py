from prototype_auto_cloud.model.app import cms
from prototype_auto_cloud.data.report import connect_report
import allure


@allure.tittle('Create report')
def test_create_connections_report():
    create_result = 'create'
    cms.report.create(connect_report)\
        .shoud_result(create_result)
