# ! /bin/sh
TRAVIS_BRANCH=algebraic-geometry
TRAVIS_BUILD_DIR=/home/maximilian/LatexPackages


cd ${TRAVIS_BUILD_DIR}
rm -rf LatexPackagesBuild

git clone https://github.com/kesslermaximilian/LatexPackagesBuild.git LatexPackagesBuild
cd LatexPackagesBuild
REMOTE_BRANCH=$(git branch -a | sed -n '/remotes\/origin\/.*-build/p' | sed 's/remotes\/origin\///g' | sed 's/-build//g' | sed 's/[[:space:]]//g' | sed -n "/^${TRAVIS_BRANCH}$/p")

echo ${REMOTE_BRANCH}

if [ "$REMOTE_BRANCH" = "" ];then
    echo "This is the first build on this branch, creating new branch in build repository to push to"
    git checkout --orphan ${TRAVIS_BRANCH}-build
    ls -ra | sed '/^\.git$/d' | sed '/^\.\.$/d' | sed '/^\.$/d' |  xargs -r git rm --cached
    ls -ra | sed '/^\.git$/d' | sed '/^\.\.$/d' | sed '/^\.$/d' |  xargs -r rm -rf
else
    echo "Checking out remote branch from last build"
    git checkout -b ${REMOTE_BRANCH}-build origin/${REMOTE_BRANCH}-build
fi
