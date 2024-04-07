#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:47:12 2024

@author: paulsharratt
"""
import os

# Define the target directory
target_directory = "/Users/paulsharratt/Documents/Hertie/Semester 4/03 - Master's Thesis/starter-health-model_STF/"

# Change the current working directory
os.chdir(target_directory)

# Verify the change
print(f"Current working directory: {os.getcwd()}")


from utils.augur_connect import augur_db_connect
import pandas as pd

engine = augur_db_connect("config.json")

urls = [
    "https://github.com/apache/logging-log4j2/",
    "https://github.com/curl/curl/",
    "https://github.com/fortran-lang/fpm",
    "https://github.com/GNOME/libxml2/",
    "https://github.com/GStreamer/qt-gstreamer",
    "https://github.com/Lullabot/drupal9ci",
    "https://github.com/NLnetLabs/domain/",
    "https://github.com/openjs-foundation/",
    "https://github.com/OpenMathLib/OpenBLAS/",
    "https://github.com/openmls/openmls",
    "https://github.com/openpgpjs/openpgpjs/",
    "https://github.com/pendulum-project/ntpd-rs",
    "https://github.com/php/web-pecl",
    "https://github.com/prefix-dev/rattler-build",
    "https://github.com/pyca/cryptography/",
    "https://github.com/qos-ch/logback",
    "https://github.com/rubygems/rubygems",
    "https://github.com/rustls/rustls",
    "https://github.com/systemd/systemd/",
    "https://github.com/tc39/test262",
    "https://github.com/uutils/coreutils",
    "https://github.com/w3c/activitypub",
    "https://github.com/sequoia-pgp/fast-forward"
]

# Remove duplicates and ensure each URL is processed only once
urls = list(set(urls))

# Process URLs to extract the organization and repository name
targets = []
for url in urls:
    # Remove trailing slash if present
    if url.endswith('/'):
        url = url[:-1]
    
    # Split the URL to extract org and repo names
    parts = url.split('/')
    if len(parts) >= 5:  # Expected format: ['https:', '', 'github.com', 'org', 'repo']
        org, repo = parts[3], parts[4]
        targets.append((org, repo))

def get_repo_id(engine, repo_name):
    """Retrieves the Augur repo_id (unique key) for a given repository name.

    Parameters
    ----------
    engine : sqlalchemy database object
    repo_name : str

    Returns
    -------
    repo_id : str or None if not found/error occurs.
    """
    try:
        get_id_query = f"""
            SELECT
                repo_id
            FROM
                augur_data.repo
            WHERE
                LOWER(repo_name) = LOWER('{repo_name}');
            """

        repo_id_df = pd.read_sql_query(get_id_query, con=engine)
        if len(repo_id_df) == 1:
            return repo_id_df.iloc[0]['repo_id']
        else:
            return None
    except Exception as e:
        print(f"Error retrieving ID for {repo_name}: {e}")
        return None

# Collect repo IDs for each target repository
results = []

for org, repo in targets:
    repo_id = get_repo_id(engine, repo)
    if repo_id is not None:
        results.append({"org": org, "repo": repo, "repo_id": repo_id})
    else:
        print(f"Repo ID not found for {org}/{repo}")
        
results_df = pd.DataFrame(results)

        
# Manually checked data on Augur db
manual_data = [
    {'repo_id': 193661, 'org': 'curl', 'repo': 'curl'},
    {'repo_id': 150977, 'org': 'pyca', 'repo': 'cryptography'}
]

# Creating a DataFrame from the new data
new_df = pd.DataFrame(manual_data)

# Append new_df to results_df
results_df = pd.concat([results_df, new_df], ignore_index=True)

# Display the updated DataFrame
print(results_df)

file_path_csv = "/Users/paulsharratt/Documents/Hertie/Semester 4/03 - Master's Thesis/thesis_stf/data/processed/target_group_repo_ids"

# Use the to_csv method to write the DataFrame to a CSV file
results_df.to_csv(file_path_csv, index=False)

file_path_xlsx = "/Users/paulsharratt/Documents/Hertie/Semester 4/03 - Master's Thesis/thesis_stf/data/processed/target_group_repo_ids.xlsx"

results_df.to_excel(file_path_xlsx, index=False, engine='openpyxl')





