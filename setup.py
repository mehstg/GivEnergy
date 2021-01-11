 
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
  name = 'GivNRG',         # How you named your package folder (MyLib)
  packages = ['GivNRG'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='apache-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A third party library to interface with the GivEnergy API',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Paul Braham',                   # Type in your name
  author_email = '',      # Type in your E-Mail
  url = 'https://github.com/mehstg/GivNRG',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['GivEnergy', 'solar', 'battery'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'datetime',
          'requests',
          'json',
          'logging',
          'pytest'
          ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)