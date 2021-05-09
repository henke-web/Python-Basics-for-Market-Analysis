# Instructions how to build and active virtual enviroment, and run the application code.(venv)

- Open command prompt in the dictionary where you want to create your virtual enviroment.

- Type in command prompt: `python -m venv (+ name of enviroment eksemple:) env.`

- Active the virtual enviroment type in prompt: `(name) env\scripts\activate`

- If this is done correctly your prompt should look something like this: (env) C:\Users\Admin\ etc...

- If you run pip list to see what packages thats running you should only see the default ones.

- For deactivate the virtual enviroment type deactivate in prompt

- To share your project or run it on another machine you can create a requirement.txt file witch will contain all packages of your project.

- How to create the .txt file you have to first active virtual enviroment, then you will have to type in prompt: `pip freeze > requirement.txt` This will create a text file with all requirements.

- To run the .txt file type in prompt: `pip install -r (and name of the .txt file) requirement.txt`
