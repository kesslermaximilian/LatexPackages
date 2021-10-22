cd .travis
export COMMIT_MSG=$(python3 print_deploy_message.py)
cd ..
make travis
cd build
zip -r LatexPackages.zip LatexPackagesBuild
tree -H '.' -I "index.html" -D --charset utf-8 -T "LatexPackages" > index.html
cd ..
