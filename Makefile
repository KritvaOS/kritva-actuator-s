# Kritva Actuator Kritva-S - checks
PYTHON ?= python3
ROOT := $(CURDIR)
.PHONY: check check-bom check-inputs
check: check-bom check-inputs  ## Run all checks
check-bom:  ## Validate the BOM schema
	$(PYTHON) scripts/check_bom.py --root $(ROOT)
check-inputs:  ## Validate sizing/inputs.json against the shared sizing engine keys
	$(PYTHON) scripts/check_inputs.py --root $(ROOT)
