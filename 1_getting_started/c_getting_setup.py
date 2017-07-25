'Getting Setup to run this bootcamp'

'''
Requirements
--------------------------------------
git
Python3 - This bootcamp was built and tested with Python 3.6.1
DSaS account

Optional
=========
virtualenv - not required but recommended
Any Editor: Pycharm, Atom, VS Code Sublime Text, etc<br/>
Note: this bootcamp was built with SublimeText 3 using the OneDark
      theme for syntax highlighting - https://packagecontrol.io/packages/Theme%20-%20One%20Dark




Installation Steps - Mac/Linux
--------------------------------------

1. clone github repo
   git clone https://github.com/jeffthorne/sejam_python_bootcamp.git

2. Change into sejam_python_bootcamp dir and create virtualenv
   virtualenv -p python3 --no-site-packages venv

3. Activate virtualenv from within top level sejam_python_bootcamp
   . venv/bin/activate

4. Install bootcamp required python packages with pip
   pip install -r requirements.txt 

5. Make sure your editior if using one points to the Python Interpreter in your virtualenv
   
   In Sublime:

   1. tools > build system > new build system
   	  {
		"cmd": ["put_full_path_to_your_vene_interpreter_here", "-u", "$file"],
		"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
		"selector": "source.python"
	  }

	2. tools > build system > choose whatever you save your build system as.

6. Update config file with your AWS and DSAS information

7. To get the examples in chpt7 working please enter required info in config.py file.

8. You are good to go :-)


## Note: For those who have trouble getting this installed
An Ubuntu VirtualBox VM will be provided with everything set up.
A download link will be provided shortly.
'''