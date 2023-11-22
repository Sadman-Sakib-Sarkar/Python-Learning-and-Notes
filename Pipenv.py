## Pipenv is similar to venv and its easier to learn and implement
# Internally it uses pip and virtual environment

## At first need to install pipenv in terminal: pip3 install pipenv
# Now instead pip we will use pipenv like: pipenv install requests
# To see the path of the virtual environment: pipenv --venv
# We need to exclude the virtual environment from our project directory
# Now uninstall the request package: pipenv uninstall requests (we installed a dependency using pipenv)

## We need to activate the virtual environment
#: pipenv shell
# It will activate our virtual environment
# For deactivate it : exit

## In vs code: pipenv --venv
#: open
# inside the bin folder we got python3 (for windows python)
# we need to pass the python interpreter and give it to the code runner extension

# Back to vs code -> preferences -> settings -> click dotdotdot -> open settings.json
# Scroll down -> "coderunner.executorMap" -> "python": "instead python3 paste the path of virtual environment/bin/python3"
# Or if we cannot find the settings we can simply add the interpreter "paste the path of virtual environment/bin/python3"

# If no coderunner.executorMap found then write and press enter it will create by own
# to see changge while coding need to select the new interpreter
# if new interpreter is missing then -> open settings.json -> add "python.pythonPath": "paste the path of virtual environment/bin/python3",
# Then we need to restart the vs code
 