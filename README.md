## Paperbank 

Paperbank is a web application library designed to help store, manage and share pdfs documents.
The platform can be deployed as a web application online, or It can be deployed as a local
library within a local network.

It is written in python using the Django web framework(more info: www.djangoproject.com),

## Done
* Ability for visitors to get pdf documents

## To be done
* User managements  and permissions.

A working version of the library. can be found at www.paperbank.net

## Setting up development

1. Start by cloning the repo
'''bash
$ git clone 
'''

2. Setup a virtualenv\
'''bash
$ virtualenv paperbank
'''
3. Install requirements
'''bash
$ pip install -r requirements.txt
''''

4. Setup environment variables
'''bash
$ export paperbank_debug=True
$ export paperbank_rollbar_key='secret'
$ export paperbank_secret_key='secret'
'''

You can put the environment variables in .bashrc to automatically load on a linux system.
