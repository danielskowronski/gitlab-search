#!/usr/bin/python3
import gitlab
import sys
import argparse


def search(gitlab_server, token, file_filter, text, group=None, project_filter=None):
    return_value = []
    gl = gitlab.Gitlab(gitlab_server, private_token=token)
    if (project_filter == '' or project_filter==None) and (group == '' or group==None):
        projects = gl.projects.list(all=True)
    else:
        group_object = gl.groups.get(group)
        group_projects = group_object.projects.list(search=project_filter)
        projects = []
        for group_project in group_projects:
            projects.append(gl.projects.get(group_project.id))
    print("Number of projects:", len(projects))
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


parser = argparse.ArgumentParser()
parser.add_argument("GITLAB_SERVER",     nargs=1,   help="URL of Gitlab server, eg. https://gitlab.com/")
parser.add_argument("GITLAB_USER_TOKEN", nargs=1,   help="Access token with api_read access")
parser.add_argument("FILE_FILTER",       nargs=1,   help="Filter for filenames to search in")
parser.add_argument("TEXT_TO_SEARCH",    nargs=1,   help="Text to find in files")
parser.add_argument("GROUP",             nargs='?', help="Group to search for projects in, can be subgroup eg. parent_group/subgroup/another_subgroup")
parser.add_argument("PROJECT_FILTER",    nargs='?', help="Filter for project names to look into")
args = parser.parse_args()

gitlab_server_arg  = args.GITLAB_SERVER[0]
token_arg          = args.GITLAB_USER_TOKEN[0]
file_filter_arg    = args.FILE_FILTER[0]
text_arg           = args.TEXT_TO_SEARCH[0]
group_arg          = None if args.GROUP          == None else args.GROUP
project_filter_arg = None if args.PROJECT_FILTER == None else args.PROJECT_FILTER

print(search(gitlab_server_arg, token_arg, file_filter_arg, text_arg, group_arg, project_filter_arg))