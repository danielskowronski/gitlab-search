#!/usr/bin/python3
import gitlab
import sys


def search(gitlab_server, token, file_filter, text, group=None, project_filter=None):
    return_value = []
    gl = gitlab.Gitlab(gitlab_server, private_token=token)
    if (project_filter == '') and (group == ''):
        projects = gl.projects.list(all=True)
    else:
        projects = gl.projects.list(search=project_filter, group=group)
    for project in projects:
        files = []
        try:
            files = project.repository_tree(recursive=True, all=True)
        except Exception as e:
            print(str(e), "Error getting tree in project:", project.name)
        for file in files:
            if file_filter == file['name']:
                file_content = project.files.raw(file_path=file['path'], ref='master')
                if text in str(file_content):
                    return_value.append({
                        "project": project.name,
                        "file": file['path']
                    })
    return return_value


gitlab_server_arg = sys.argv[1]
token_arg = sys.argv[2]
file_filter_arg = sys.argv[3]
text_arg = sys.argv[4]
group_arg = sys.argv[5]
project_filter_arg = sys.argv[6]

if len(sys.argv) < 4 or gitlab_server_arg == '' or token_arg == '' or file_filter_arg == '' or text_arg == '':
    print('Missing mandatory fields. usage:')
    print('./gitlab-search.py GITLAB_SERVER GITLAB_USER_TOKEN FILE_FILTER TEXT_TO_SEARCH [GROUP] [PROJECT_FILTER]')
else:
    print(search(gitlab_server_arg, token_arg, file_filter_arg, text_arg, group_arg, project_filter_arg))
