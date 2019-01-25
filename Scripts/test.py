import allure


class Test_allure():
    @allure.step(title="test_02")
    def test_01(self):
        print("111")
        assert True

    @allure.step(title="test_02")
    def test_02(self):
        print("222")
        assert False
