#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:15:21 2024

@author: paul
"""

import os

# Define the target directory
target_directory = "/Users/paulsharratt/Documents/Hertie/Semester 4/03 - Master's Thesis/starter-health-model_STF"

# Change the current working directory
os.chdir(target_directory)

# Verify the change
print(f"Current working directory: {os.getcwd()}")

from utils.repo_info import get_repo_info, fork_archive, get_org_repos
from utils.augur_connect import augur_db_connect
from metrics.closure_ratio import monthly_prs_closed
from metrics.release_frequency import get_release_data
from metrics.release_frequency import activity_release_graph

engine = augur_db_connect("config.json")

# Replace with actual values
repo_org = 'sequoia-pgp'
org_name  = 'sequoia-pgp'
repo_name = 'fast-forward'
repo_id =  '150824' 
start_date = '2020-01-01'
end_date =  '2024-01-01'

# Function & call
repo_info = get_repo_info(engine, repo_org, repo_name)

print(repo_info)

# Function & call
org_repos = get_org_repos(org_name, engine)

print(org_repos)


# Adapting org_repos to handle multiple organizations with a dictionary
org_names = ['fortran-lang', 'tc39']  # List of organization names, testing with php - should be in excess of 144 repos

all_org_repos = {}  # Dictionary to store repos for each org

for org_name in org_names:
    # Retrieve repos for each organization
    org_repos = get_org_repos(org_name, engine)
    all_org_repos[org_name] = org_repos
    print(f"Repositories for {org_name}:", org_repos)
## this works - except there were no repos for fortran-lang



### Sorting working directory

import os
print(os.getcwd())
# Define the target directory
target_directory = "/Users/paulsharratt/Documents/Hertie/Semester 4/03 - Master's Thesis/starter-health-model_STF/"

# Change the current working directory
os.chdir(target_directory)

# check the augur documentation


# this doesn't work yet: print(get_release_data(repo_id, start_date, end_date, engine))

# this doesn't work yet: activity_release_graph(repo_id, repo_name, org_name, start_date, end_date, engine, years)