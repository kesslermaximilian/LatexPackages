# ! /bin/sh
TRAVIS_BRANCH=algebraic-geometr

rm -rf LatexPackagesBuild

git clone https://github.com/kesslermaximilian/LatexPackagesBuild.git LatexPackagesBuild
cd LatexPackagesBuild
FOUND=$(git branch -a | sed -n '/remotes\/origin\/.*-build/p' | sed 's/remotes\/origin\///g' | sed 's/-build//g' | sed 's/[[:space:]]//g' | sed -n "/^${TRAVIS_BRANCH}$/p")

echo ${FOUND}

if [ "$FOUND" = "" ];then
    git checkout --orphan ${TRAVIS_BRANCH}-build
    ls -ra | sed '/^\.git$/d' | sed '/^\.\.$/d' | sed '/^\.$/d' |  xargs -r git rm --cached
    ls -ra | sed '/^\.git$/d' | sed '/^\.\.$/d' | sed '/^\.$/d' |  xargs -r rm -rf
else
    echo "found"
    git checkout -b ${FOUND}-build origin/${FOUND}-build
fi
