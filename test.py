#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:15:21 2024

@author: paul
"""


from repo_info import get_repo_info, fork_archive, get_org_repos
from augur_connect import augur_db_connect


engine = augur_db_connect("/Users/paul/Documents/08 - Hertie/config/config.json")

# Replace with actual values
repo_org = 'sequoia-pgp'
org_name  = 'sequoia-pgp'
repo_name = 'fast-forward'

# Function & call
repo_info = get_repo_info(engine, repo_org, repo_name)

print(repo_info)

# Function & call
org_repos = get_org_repos(org_name, engine)

print(org_repos)
