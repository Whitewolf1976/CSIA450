# -*- coding: utf-8 -*-
"""
Created on Wed May 20 03:07:46 2020
@author: CharlesKaneaster
"""
'''
Charles Kaneaster
CSIA 450
Spring 2020
Project 2
'''

# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess

os.chdir('C:\\Users\\charleskaneaster')
cwd = os.getcwd()
print(cwd)

# SET VARIABLES
my_dir = 'C:\\Users\\charleskaneaster\\Downloads\\Logon ID'
date_str = date.today().strftime("%m%d%y")
my_pickle = 'C:\\Users\\charleskaneaster\\Downloads\\Logon ID\\%s.pickle' % date_str
my_json = 'C:\\Users\\charleskaneaster\\Downloads\\Logon ID\\%s.json' % date_str
port_list = ['192.168.1.22:80', '192.168.1.22:23', '192.168.1.22:22']
nmap_path = 'C:\\Program Files (x86)\\Nmap\\nmap.exe'
nmap_network = '192.168.1.22/24'

def create_directory():   
    if(os.path.isdir(my_dir)) == False:
        try:  
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir) 
        except OSError:  
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir) 
        
def create_date_string():
    date_str = date.today().strftime("%m%d%y")
    print("Date String:", date_str)

def write_files():
    # write the pickle file
    with open(my_pickle, 'wb') as fp:
        pickle.dump(port_list, fp)
    fp.close()
    
    # write the json file
    with open(my_json, 'w') as fp:  
        json.dump(port_list, fp)
    fp.close()

def read_files():
    port_list = []
    
    # read the pickle file
    with open (my_pickle, 'rb') as fp:
        port_list = pickle.load(fp)
    fp.close()
    
    print("pickle:", port_list)
    
    port_list = []
    
    # read the json file
    with open(my_json, 'r') as fp:  
        port_list = json.load(fp)
    fp.close()
    
    print("json:", port_list)

def run_nmap():
    nmap_out = subprocess.run([nmap_path, "-T4", nmap_network], capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    print(nmap_data)

create_directory()
create_date_string()
write_files()
read_files()
run_nmap() 
