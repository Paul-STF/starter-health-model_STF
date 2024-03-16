#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:15:21 2024

@author: paul
"""

# import sys
# sys.path.append('/Users/paul/Documents/08 - Hertie/starter-health-model_STF/utils')

from utils.repo_info import get_repo_info, fork_archive, get_org_repos
from utils.augur_connect import augur_db_connect
from metrics.closure_ratio import monthly_prs_closed
from metrics.release_frequency import get_release_data

engine = augur_db_connect("config.json")

# Replace with actual values
repo_org = 'sequoia-pgp'
org_name  = 'sequoia-pgp'
repo_name = 'fast-forward'
repo_id =  '150824' 


# Function & call
repo_info = get_repo_info(engine, repo_org, repo_name)

print(repo_info)

# Function & call
org_repos = get_org_repos(org_name, engine)

print(org_repos)



### Sorting working directory

import os
print(os.getcwd())
# Define the target directory
target_directory = "/Users/paulsharratt/Documents/Hertie/Semester 4/03 - Master's Thesis/starter-health-model_STF/"

# Change the current working directory
os.chdir(target_directory)

# check the augur documentation


get_release_data(repo_id, start_date, end_date, engine):