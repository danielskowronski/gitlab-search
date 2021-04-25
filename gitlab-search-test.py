import unittest
import importlib

main_script=importlib.import_module('gitlab-search')
search = getattr(main_script, 'search')

api_debug_arg      = False
internal_debug_arg = False
gitlab_server_arg  = 'https://gitlab.com'
token_arg          = 'TOKEN_CHANGE_ME!'
group_arg          = 'test_group_for_gitlab-search_testing'

class TestGitlabSearch(unittest.TestCase):
    def test_01(self):
        regex_arg          = True
        file_filter_arg    = '.*'
        text_arg           = 'foobar00'
        project_filter_arg = None

        self.assertEqual(search(gitlab_server_arg, token_arg, file_filter_arg, text_arg, group_arg, project_filter_arg, api_debug_arg, internal_debug_arg, regex_arg), [{'file': 'README.md', 'project': 'test_project_3'}, {'project': 'test_project_2', 'file': 'test.txt'}, {'project': 'test_project_1', 'file': 'README.md'}, {'project': 'test_project_1', 'file': 'foobar_zero-zero-two'}])

    def test_02(self):
        regex_arg          = False
        file_filter_arg    = '.*'
        text_arg           = 'foobar00'
        project_filter_arg = None

        self.assertEqual(search(gitlab_server_arg, token_arg, file_filter_arg, text_arg, group_arg, project_filter_arg, api_debug_arg, internal_debug_arg, regex_arg), [])

    def test_03(self):
        regex_arg          = False
        file_filter_arg    = 'test.txt'
        text_arg           = 'foobar00'
        project_filter_arg = None

        self.assertEqual(search(gitlab_server_arg, token_arg, file_filter_arg, text_arg, group_arg, project_filter_arg, api_debug_arg, internal_debug_arg, regex_arg), [{'file': 'test.txt', 'project': 'test_project_2'}])

if __name__ == '__main__':
    unittest.main()