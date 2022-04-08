# Steps to clone project starter and push to project repo

1. Clone the starter repo
2. REMOVE the existing `.git` directory!
    - This will remove the git history associated with the a/A starter repo. Do not push to the a/A starter repo!
3. `git init`
    - Reinitialize git in your local repo if you haven't already
4. `git remote add origin <your_repo_here>`
    - Add your project repo as the origin fork
5. `git add .`
    - Add all the files to the staging area
6. `git commit -m “first commit”`
    - Commit all the files to your branch
7. `git push -u origin main`
    - Push to main!