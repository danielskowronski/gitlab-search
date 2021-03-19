# gitlab-search
Python's script to search texts in any project

## Requirements
The script has been executed successfully with Python 3.8.5

## Installation
In order to do work the script you can create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Alternatively, if you are working on Ubuntu or similar you can install required package:

```bash
sudo apt install python3-gitlab
```

## Usage

```
usage: gitlab-search.py [-h] [--api-debug] [--internal-debug] [--filename-is-regex]
                        GITLAB_SERVER GITLAB_USER_TOKEN FILE_FILTER TEXT_TO_SEARCH [GROUP] [PROJECT_FILTER]

positional arguments:
  GITLAB_SERVER        URL of Gitlab server, eg. https://gitlab.com/
  GITLAB_USER_TOKEN    Access token with api_read access
  FILE_FILTER          Filter for filenames to search in
  TEXT_TO_SEARCH       Text to find in files
  GROUP                Group to search for projects in, can be subgroup eg. parent_group/subgroup/another_subgroup
  PROJECT_FILTER       Filter for project names to look into

optional arguments:
  -h, --help           show this help message and exit
  --api-debug          Show all API calls
  --internal-debug     Show all iterated items and other dubugv info
  --filename-is-regex  FILE_FILTER become Python regular expressions, so it can be '.*\.cpp' to search for all files with extension cpp
```

### Example
```
$ python3 gitlab-search.py 'https://gitlab.com' $API_TOKEN '.*' 'foobar00' test_group_for_gitlab-search_testing --filename-is-regex --internal-debug    
Number of projects that will be searched: 2
Project:  test_project_2
  File:  test.txt
Project:  test_project_1
  File:  README.md
  File:  foobar_zero-zero-two
[{'project': 'test_project_2', 'file': 'test.txt'}, {'project': 'test_project_1', 'file': 'README.md'}, {'project': 'test_project_1', 'file': 'foobar_zero-zero-two'}]
$
```

## Development
### Testing
Use [gitlab-search-test.py](gitlab-search-test.py) - replace `'TOKEN_CHANGE_ME!'` with same token used for main script and just call `python3 gitlab-search-test.py`

This script uses this Gitlab group - [https://gitlab.com/test_group_for_gitlab-search_testing/](https://gitlab.com/test_group_for_gitlab-search_testing/)
