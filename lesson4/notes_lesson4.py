# git & github

# Version control tools

# Recap
# Agile = small steps,fast feedback, welcome changes
# Scrum roles: PO, Scrum master, Devs
# Events: Sprint, Planning, Daily, Review, Retrospective
# Artifacts: Product backlog, Spring backlog, Increment
# kanban: a board, WIP limits, continuos flow

# Version control
# What, who, when and why
# go back in history
# many people in the same project, at the same time

# Git
# program in your computer
# work without internet
# saves history code

# GitHub
# website that stores git repositories
# lets teams share code online
# Adds pull request. reviews, issues, boards
# Similar: GitLab, Bitbucket

# Three places for your code
# working directory (your file) - > git add -> staging area (ready to save) - > git commit -> Repository (history)


# Some useful commands
# git status --> what has changed?
# git log --oneline  --> show the history
# git diff  ---> show exactly what changed


# Commit messages
# Write meaningful comment about the commit
# start with a verb add, remove, fix

# Gitignore
# list files git should ignore when commiting

# Branch
# git switch -c feature/login  - > creates a new branch feature/login and move into it
# git switch main - move to main branch
# git merge feature/search - > merges into the branch you are on


# Workflow
# get latest main: git switch main - git pull
# create a branch: git switch -c feature/branch
# push branch: git push -u origin feature/branch
# work and commit: git add, git commit -m "message", git push
# open pull request
# teammate review
# merge to main
# delete feature/branch
# pull from main


# Naming branches
# new feature: feature/product-search
# fix bug: bugfix/cart-total
# small fix: fix/typo-in-readme
# with issue number: feature/12-order-history

# Pull request
# write a title and description
# write what issue it close: "closes #12"
# automatic checks can run
# show changes
# ask for review
# resolve teammate comments

# Protect main -  so main always works
# no push directly to main-> always create a pull request
# At least one approval before merging
# All checks must pass


# Undoing things
# git restore main.py -> throw away my changes in a file
# git restore --stage main.py -> unstage it (keep changes)
# git commit --amend -m "..." -> fix the last commit message before push
# git revert xxxxx -> undo a commit with a new commit

