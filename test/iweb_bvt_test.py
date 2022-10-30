import time
from unittest import TestCase
from library.httpclient import HttpClient


class IWeb_BVT(TestCase):
    """Weather api test cases"""

    def setUp(self):
        """Setup of the test"""

        self.host = 'http://localhost:8111'
        self.ep_path = '/healthCheck'
        self.client = HttpClient()

    def test_health_api(self):
        self._test()

    def _test(self, timeout=120):
        url = f'{self.host}{self.ep_path}'

        # 轮询等待后端程序启动
        end = time.time() + timeout
        status = 404
        while time.time() <= end and status != 200:
            err_msg = 'The health api is not started, continue checking ...'
            try:
                self.response = self.client.Get(url)
                if self.response.status_code == 200:
                    status = 200
                else:
                    print(err_msg)
                    time.sleep(2)
            except Exception:
                print(err_msg)
                time.sleep(2)

        expect_value = 'Good'
        msg_value = f'Expect value = {expect_value}, while actual value = {self.response.text}'
        msg_status_code = f'Expect status = 200, while actual status = {self.response.status_code}'

        self.assertEqual(200, self.response.status_code, msg_status_code)
        print(msg_status_code)

        self.assertEqual(expect_value, self.response.text, msg_value)
        print(msg_value)
