# gitlab-search
Python's script to search texts in any project

# Requirements
The script has been executed successfully with Python 3.8.5

# Installation
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

# Usage example:

```bash
python3 gitlab-search.py https://your-gitlab-server.com/ your_gitlab_user_token_key name_of_file_to_search_into text_to_search group project_filter
```
