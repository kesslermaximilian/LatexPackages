.PHONY: build

build: .initsubmodulelock
	@python3 build.py

init: .initsubmodulelock .gitconfiglock

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
