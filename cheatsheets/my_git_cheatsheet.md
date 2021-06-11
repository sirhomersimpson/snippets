Ref: https://about.gitlab.com/images/press/git-cheat-sheet.pdf

#Branches
### Local
git branch
### Remote
git branch -a


###remote
git push origin --delete rkisnah/alarmfixes

####local
git branch -d feature/login

## Create a branch
git checkout -b rkisnah/alarmfixes

### git log one 
git log --pretty=oneline

### delete branches
#### remote
git branch -a
 *master
 test
  remote/origin/master
  remote/origin/test

git push origin --delete test
  
#### local
  git branch -d rkisnah/test123
