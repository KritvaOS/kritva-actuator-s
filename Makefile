# Kritva Actuator Kritva-S - checks
PYTHON ?= python3
ROOT := $(CURDIR)
.PHONY: check check-bom check-inputs check-status check-readme
check: check-bom check-inputs check-status  ## Run all checks
check-bom:  ## Validate the BOM schema
	$(PYTHON) scripts/check_bom.py --root $(ROOT)
check-inputs:  ## Validate sizing/inputs.json against the shared sizing engine keys
	$(PYTHON) scripts/check_inputs.py --root $(ROOT)

check-status:  ## Validate status/status.json (kritva-program status schema 2.0) against status/tasks.csv
	$(PYTHON) scripts/status/gen_status.py --root $(ROOT) --check

check-readme:  ## Check README.md against the Kritva README standard (structure, metadata, local links)
	$(PYTHON) scripts/check_readme.py README.md --root $(ROOT)
