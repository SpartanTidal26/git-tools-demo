echo "# git-tools demo" >> README.md
git init
git config --global user.name "Robert Johnson"
git config --global user.email "robertpjohnson1220@gmail.com"
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/SpartanTidal26/git-tools-demo.git
git remote -v
git push -u origin main