.PHONY: build
BUILD_FLAGS=--recursive --git-version --pytex-version --license --author "Maximilian Keßler" --pytex-info-text --extra-header ".build/header_info.txt" --name "prepend-author"
BUILD_DIRS= --source-dir src --build-dir build

build: .initsubmodulelock
	@python3 build.py ${BUILD_DIRS} ${BUILD_FLAGS}

dirty: .initsubmodulelock
	@python3 build.py ${BUILD_DIRS} ${BUILD_FLAGS} --allow-dirty

init: .initsubmodulelock .gitconfiglock

config: .gitconfiglock

.initsubmodulelock:
	@git submodule update --init
	@touch .initsubmodulelock

.gitconfiglock:
	@echo "[Make config] Setting git configs to prevent wrong pushes"
	@git config push.recurseSubmodules check
	@git config status.submodulesummary 1
	@echo "[Push annotated tags by default]"
	@git config push.followTags true
	@touch .gitconfiglock


clean:
	@-rm -r build/

travis:
	@python3 build.py --source-dir src --build-dir build/LatexPackagesBuild ${BUILD_FLAGS}
