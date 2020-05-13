import allure
import pytest


class TestAllure:

    def setup(self):
        print('---> setup')

    def teardown(self):
        print('teardown')

    @pytest.mark.parametrize(argnames=('a'), argvalues=[1, 2, 3])
    @allure.step('测试步骤001')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_a(self, a):
        print('test_a')
        allure.attach('title 啦', '这个是执行详细步骤结果')
        assert a != 2

    def test_b(self):
        print('test_b')
        assert 0
