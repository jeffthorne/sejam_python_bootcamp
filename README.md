![Alt text](https://dl.dropboxusercontent.com/u/19596584/dsp3_logo3.jpg "Optional title")

SE JAM Python Bootcamp
====


Requirements
=========
1. git
2. Python3 - This bootcamp was built and tested with Python 3.6.1
3. virtualenv - not required but recommended
4. DSaS account



<b>Optional</b><br/>
5. Any Editor: Pycharm, Atom, VS Code Sublime Text, etc<br/><br/>
   Note: this bootcamp was built with SublimeText 3 using the OneDark<br/>
   theme for syntax highlighting - https://packagecontrol.io/packages/Theme%20-%20One%20Dark


<b>Note: For those who have trouble getting this installed</b><br/>
An Ubuntu VirtualBox VM will be provided with everything set up.<br/>
A download link will be provided shortly.<br/><br/>


<b>Windows Python3 and virtualenv installation instructions</b><br/>
Not completed at this time.



Bootcamp Install Steps [assumes git, python, and virtualenv installed - Mac/Linux
---------------------------------------------------------------------------------

1. clone github repo. 
   git clone https://github.com/jeffthorne/sejam_python_bootcamp.git

2. Change into sejam_python_bootcamp dir and create virtualenv. 
   virtualenv -p python3 --no-site-packages venv

3. Activate virtualenv from within top level sejam_python_bootcamp. 
   . venv/bin/activate

4. Install bootcamp required python packages with pip. 
   pip install -r requirements.txt 

5. Make sure your editior if using one points to the Python Interpreter in your virtualenv. 
   
   In Sublime:  
   tools > build system > new build system<br/> 
   	  {<br/> 
		"cmd": ["put_full_path_to_your_vene_interpreter_here", "-u", "$file"],<br/>
		"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",<br/>
		"selector": "source.python"<br/>
	  }<br/>
		<br/>
	tools > build system > choose whatever you save your build system as.<br/>
    <br/>
6. Update config file with your AWS and DSAS information
7. To get the examples in chpt7 working please enter required info in config.py file.
8. You are good to go :-)





Documentation
=========
DSP3 - http://dsp3.readthedocs.io 