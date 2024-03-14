git add .
echo 'Enter a commit message: '
read commitMessage
git commit -m "$commitMessage"
echo 'What branch should the commit be pushed to? '
read branch
git push origin "$branch"