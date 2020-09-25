
from distutils.core import setup
setup(
  name = 'ResumeAnalyzer',         # How you named your package folder (MyLib)
  packages = ['ResumeAnalyzer'],   # Chose the same as "name"
  version = '0.8',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An easy to use library to rank resumes',   # Give a short description about your library
  long_description="Full documentation at GitHub: https://github.com/Shivanandroy/Resume-Analyzer ",
  author = 'Shivanand Roy',                   # Type in your name
  author_email = 'Shivanandroy.official@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Shivanandroy/Resume-Analyzer',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/Shivanandroy/Resume-Analyzer/archive/v_01.tar.gz',    # I explain this later on
  #keywords = ['Resume', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'spacy',
          'textract',
          'dash',
          'dash_bootstrap_components',
          'jupyter_dash'
      ],
  dependency_links = ["https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz"],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
