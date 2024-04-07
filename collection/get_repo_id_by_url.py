#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:38:29 2024

@author: paulsharratt
"""

def get_repo_id_by_url(engine, repo_url):
    """Retrieves the Augur repo_id (unique key) for a given repository URL.

    Parameters
    ----------
    engine : sqlalchemy database object
    repo_url : str

    Returns
    -------
    repo_id : str
    """
    import pandas as pd

    try:
        get_id_query = f"""
            SELECT
                repo_id
            FROM
                repo
            WHERE
                LOWER(repo_git) = LOWER('{repo_url}');
            """

        repo_id_df = pd.read_sql_query(get_id_query, con=engine)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

    if len(repo_id_df) == 1:
        repo_id = repo_id_df.iloc[0]['repo_id']
    else:
        print("Missing or invalid repository URL.")
        sys.exit()

    return repo_id
