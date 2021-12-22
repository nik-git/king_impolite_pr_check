# Intro
We would like to make the world a better place, a little bit more polite at least - and we can use
automation to make it happen. This is a form of automation for a GitHub project that will prevent
merging impolite pull requests.
The impolite pull request can be detected as the one that has no “please”, “appreciate”,
“would be great” phrases in the description.

# Objective
This solution is implemented using webhook in GitHub repo.
This repo contains the code for flask app that will check if a PR created for this repo in polite or not. If not then close the PR.
This flask app is hosted on "http://nikhilguptamyid.pythonanywhere.com"
To view the code of this flask app, please see file "check_impolite_pr.py"

# Steps to test this automation
DOC : https://github.com/nik-git/king_impolite_pr_check/blob/main/Steps%20to%20test%20Nice%20Pull%20Request%20Challenge.pdf 

a. Fork the repo nik-git/king_impolite_pr_check

b. Create a new PR from your fork to merge in nik-git/king_impolite_pr_check Main branch.

c. While creating PR, do not add any words such as Please, appreciate or would be great in description of PR.

d. Click on Create Pull Request button.

e. After few seconds, your PR will be deleted.

f. If you add word please in PR, PR will not be deleted.

See this file for steps with screenshots.

Steps to test Nice Pull Request Challenge.pdf

# Workflow
1. In this repo : nik-git/king_impolite_pr_check, a webhook is created for PR events.
2. Whenever a new PR is created, PR event will be generated and this webhook will be tiggered.
3. This webhook will call API http://nikhilguptamyid.pythonanywhere.com/impolite_pr
4. This API will check that in PR body any of the polite word is present or not.
5. If not then that PR will be deleted.
