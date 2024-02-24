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

engine = augur_db_connect("config.json")

# Replace with actual values
repo_org = 'sequoia-pgp'
org_name  = 'sequoia-pgp'
repo_name = 'fast-forward'
repo_id =  '150824' 
#start_date = '202001' 
#end_date = '202301'

# Function & call
repo_info = get_repo_info(engine, repo_org, repo_name)

print(repo_info)

# Function & call
org_repos = get_org_repos(org_name, engine)

print(org_repos)

<<<<<<< Updated upstream
=======
#repo_prs = monthly_prs_closed(repo_id, repo_name, start_date, end_date, engine)

#print(repo_prs)

#YYYY-MM-DD HH:MM:SS


#150824

#dm_group_monthly

#dm_repo_monthly



#from metrics.closure_ratio import monthly_prs_closed

#from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

#Session = sessionmaker(bind=engine)
#session = Session()

#for pr_monthDF in session.query(pr_monthDF.start_date).all():
#    print(pr_monthDF.start_date)
    
>>>>>>> Stashed changes
