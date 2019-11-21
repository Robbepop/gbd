# gbd (Global Benchmark Database)

## Installation
### Programming Language
Python 3

### Getting Started
- setup python3
- setup pip (pip3) and install required packages
    ```console
	    pip3 install flask_limiter global-benchmark-database-tool
	```
- clone repository
- make sure path for python 3 in cli.py is correct
  (default: #!/usr/bin/python3)
- make sure Python was compiled with SSL support
- create an executable link like so ```ln -s $respository/cli.py $bin/gbd```
- obtain a database from https://baldur.iti.kit.edu/gbd/ and safe them under /path/to/db/file.db
- execute ```export GBD_DB=/path/to/db/file.db``` and put it in your .bashrc or somewhere else
- run ```gbd init /path/to/cnf``` in order to reinitialize your benchmarks table
- run ```gbd get -r benchmarks``` to test the system

## Usage
- After getting started, you can use GBD from the command line as explained in the help section
- For starting the server on Linux, run ```sh run_server.sh /path/to/database```. If no path is given, the script uses
the path exported in the environment variable GBD_DB.
- For starting the server on Windows, run ```\path\to\python3\interpreter server.py -d /path/to/database```

### Help on basic commands
	./cli.py -h

### Help on specific command
	./cli.py [command] -h

### Initialize GBD
	./cli.py init [path]

## Documenation
GBD was initially presented at the Pragmatics of SAT (POS) Workshop 2018 hosted at FLoC 2018 in Oxford, UK. Thus, two resources can now be used as documentation of the system. 

### doc/
The directory contains the Latex source of the original paper published at POS 2018.

### presentation/ 
The directory contains the Latex source of the presentation slides as presented at POS 2018.
