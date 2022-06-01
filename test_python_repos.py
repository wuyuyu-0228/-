import unittest
import python_repos as pr

class MyTestCase(unittest.TestCase):

    def setUp(self):
        """创建一个调查对象和一组答案, 供使用的测试方法使用"""
        url='https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.r=pr.get_response(url)
        self.response_dict=self.r.json()
        self.repo_dicts=pr.get_repo_dicts(self.r)
        self.repo_dict=self.repo_dicts[0]
    def test_get_status_code(self):
        """API调用后，status_code是否为200"""
        my_status_code=self.r.status_code
        self.assertEqual(str(my_status_code), "200")  # add assertion here

    def test_get_repos_returned_number(self):
        """测试返回条目数是否为30"""
        self.assertEqual(len(self.repo_dicts),30)

    def test_get_repos_number(self):
        """测试仓库总数是否超过500000"""
        my_respos_number=self.response_dict['total_count']
        self.assertEqual(my_respos_number,500000)

if __name__ == '__main__':
    unittest.main()
