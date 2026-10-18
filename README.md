# Kritva Actuator Kritva-S

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

Child repository of `KritvaOS/kritva-actuator` (the parent). Owner: Mechanical Intern 1.

**Status: Concept.** `sizing/inputs.json` holds **placeholder** values: only the torque and speed fields differ from M. Arm and payload masses, shaft dimensions and the other fields are copied from M and must be replaced by S-specific values.

The common interface, CAN protocol, units and the shared sizing engine are owned by the parent and are **not** redefined here. Read `docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md` in the parent first.

## Variant class (provisional, parent ACT-DEC-025)

S: about 2-5 N·m continuous, 5-10 N·m peak, about 60 RPM (provisional, not approved).

## Stages and variant classes

**Status: provisional planning information. Not approved requirements.** Stage scope is held in `planning/v1/ROADMAP.md` and `planning/v1/MILESTONE.md`; class ranges in `docs/architecture/ACTUATOR_FAMILY_SPEC.md` (ACT-DEC-025, PROPOSED). Budgets are provisional. Nothing here authorises purchase, fabrication or design freeze.

### Stage comparison: A0 and A1

| Item | A0: Educational Motor Control | A1: Humanoid Smart Actuator |
|---|---|---|
| Primary objective | Learn and validate motor control; build the reusable electronics and firmware base | Working actuator module: motor, gearbox, output shaft and bearings, output encoder, controller, CAN |
| Motor | Low-cost commercial BLDC/PMSM | Commercial BLDC/PMSM selected from the sizing results (ACT-DEC-003, 008 pending) |
| Controller | Motor-control development board (about ₹3,000-₹5,000) | Custom controller PCB (repository baseline) |
| Position control | FOC with current sensing; basic closed-loop position and speed | Position, velocity and torque control on the actuator |
| Encoder | Motor-side feedback | Motor-side feedback plus output-side encoder |
| Communication | USB/UART | CAN (firmware and protocol per the parent ICD) |
| Diagnostics | Basic status, faults, logging | Fault handling, thermal and current limits, CAN diagnostics |
| Mechanical design | Mounting and bench fixture only | Commercial planetary gearbox, independent output shaft and bearings, housing (HOLD lifted by ACT-DEC-029; Gate A still required) |
| Validation | Bench tests on a restrained fixture | Elbow load case; Gates A/B/C with independent review (ACT-DEC-014, 015) |
| Budget (provisional) | ₹10,000-₹15,000 | ₹20,000-₹30,000, cumulative including A0 |
| Deliverable | Working motor-control platform with firmware, tests and documents | Validated actuator with CAD, BOM, firmware, test reports |

Planning status (2026-10-18): A0 exits at P12 (10 Jan 2027), six weeks later than the original week-6 target (ACT-DEC-032). The M prototype checkpoint is P23 (22-28 Mar 2027), after Gate A (by P14) and a two-week release and procurement gap (ACT-DEC-033). The custom controller PCB and CAN firmware stay the A1 baseline; a development-board substitute is a reviewed deviation. Stage names above are the official names. Reforecast: `planning/v2/ROADMAP_48_WEEKS.md` (P1 = 19 Oct 2026; 58-week horizon ending 28 Nov 2027 is proposed, awaiting Project Lead confirmation).

### Variant classes (provisional)

| Class | Repository baseline (ACT-DEC-025, PROPOSED) | Wider planning range (under review, not approved) | Typical joints |
|---|---|---|---|
| Kritva-S | 2-5 N·m continuous, 5-10 N·m peak, about 60 RPM | 2-5 / 5-10 N·m | Wrist, neck |
| Kritva-M | 10 N·m continuous, 20-25 N·m peak, 45 RPM (elbow baseline and A0 reference, ACT-DEC-008) | 5-20 / 20-40 N·m | Elbow, shoulder (shoulder not yet in the spec) |
| Kritva-L | 25-40 N·m continuous, 50-80 N·m peak, about 20-40 RPM | 20-80 / 80-150 N·m | Hip, knee, ankle (ankle not yet in the spec) |

Use the repository baseline column for sizing and reviews. The wider range is a discussion input; it becomes a requirement only after the owner records it in `planning/v1/DECISIONS.md`. For L the two columns differ materially, so confirm the intended load cases first.

## Documents to read

Read in this order. "parent" means a path inside the `kritva-actuator` parent repository (clone it with `--recurse-submodules`, see below); "this repo" means this repository. Statuses in the documents matter: values marked PROPOSED, provisional or TBD are not approved requirements. Tool flows are proposed, not frozen. Passing checks does not close a gate.

### A. Before you start (first week)

| # | Document | Where | What to take from it |
|---|---|---|---|
| 1 | `README.md` | parent | Stages A0/A1/A2, design baseline (proposed, not frozen), repository structure, roles, safety |
| 2 | `AGENTS.md` | this repo and parent | Rules for people and AI agents: gates, what not to change, no waivers |
| 3 | `planning/v1/DECISIONS.md` | parent | Decision index and status. Read ACT-DEC-001 to 009, 014, 015, 024 to 033 and the pending list (section 5) before choosing parts |
| 4 | `planning/v2/ROADMAP_48_WEEKS.md` | parent | Current reforecast (P-weeks): A0 exit P12, Gate A, release gap, M fabrication, PCB spins, gates. Sections 3 to 5 |
| 5 | `planning/v2/WORKSTREAMS.md` | parent | Who owns what, hand-offs between workstreams |
| 6 | `docs/standards/SUBMODULE_WORKFLOW.md` | parent | How child commits are pinned in the parent; branches and pull requests |

### B. Requirements, architecture and interfaces

| # | Document | Where | What to take from it |
|---|---|---|---|
| 1 | `requirements/SYSTEM_REQUIREMENTS.md` | parent | System limits: torque, speed, budget (SYS-REQ-100), provisional assumptions |
| 2 | `requirements/MECHANICAL_REQUIREMENTS.md` | parent | What the mechanical design must satisfy |
| 3 | `requirements/SAFETY_REQUIREMENTS.md` | parent | Safety limits; hard stops, restrained-fixture rule |
| 4 | `requirements/INTERFACE_REQUIREMENTS.md` | parent | Mounting, shaft and connector interface requirements |
| 5 | `requirements/ACTUATOR_SPECIFICATION.md` | parent | Actuator-level specification |
| 6 | `docs/architecture/ACTUATOR_ARCHITECTURE.md` | parent | Actuator architecture and boundaries |
| 7 | `docs/architecture/ACTUATOR_FAMILY_SPEC.md` | parent | S/M/L classes (provisional, ACT-DEC-025). Repository baseline values are the ones to use |
| 8 | `docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md` | parent | The common interface; never redefine it in this repo |
| 9 | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | parent | Units, signs, conventions used in every calculation |

### C. Mechanical design and calculations

| # | Document | Where | What to take from it |
|---|---|---|---|
| 1 | `docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md` | parent | Mechanical design baseline: housing, shaft, bearings, gearbox mount |
| 2 | `mechanical/calculations/LOAD_CASES.md` | parent | Elbow load case and assumptions (centre of mass is provisional) |
| 3 | `mechanical/calculations/TORQUE_AND_SPEED.md` | parent | Torque and speed derivation |
| 4 | `mechanical/calculations/SHAFT_STRENGTH.md` | parent | Shaft method: torsion, bending, combined, fatigue, deflection |
| 5 | `mechanical/calculations/BEARING_SELECTION.md` | parent | Bearing loads, life, fits, preload |
| 6 | `mechanical/calculations/GEARBOX_SELECTION.md` | parent | Gearbox limits and selection criteria (ACT-DEC-003) |
| 7 | `mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md` | parent | Candidate motor and gearbox pairs |
| 8 | `mechanical/common-sizing/README.md` | parent | How to run the shared sizing engine with this repo's `sizing/inputs.json` |
| 9 | `docs/mechanical/MATERIAL_SELECTION.md` | parent | Material choices and rules |
| 10 | `docs/mechanical/FABRICATION_GUIDELINES.md` | parent | Manufacturing constraints before drawings are released |
| 11 | `docs/mechanical/ASSEMBLY_PROCEDURE.md` | parent | Assembly steps and inspection |

### D. Standards and tool flow

| # | Document | Where | What to take from it |
|---|---|---|---|
| 1 | `docs/standards/TOOLFLOW_MECHANICAL.md` | parent | Your tool flow (FreeCAD, checks, Gate A, release). Toolchain is proposed, not frozen |
| 2 | `docs/standards/OPEN_SOURCE_TOOLFLOW.md` | parent | Full tool reasoning, licences and the checked reference links (GitHub, YouTube) |
| 3 | `docs/standards/CAD_NAMING_STANDARD.md` | parent | File, part and assembly naming |
| 4 | `docs/standards/BOM_STANDARD.md` | parent | BOM columns and rules (`make check` enforces them) |
| 5 | `docs/standards/DESIGN_REVIEW_CHECKLIST.md` | parent | Complete before Gate A; fabrication starts only after Gate A plus the release gap |
| 6 | `docs/standards/RELEASE_CHECKLIST.md` | parent | What a release needs |
| 7 | `docs/standards/PROGRAM_ALIGNMENT.md` | parent | How status reporting and HOLD relate to kritva-program |

### E. Validation, audit and planning

| # | Document | Where | What to take from it |
|---|---|---|---|
| 1 | `docs/validation/VALIDATION_PLAN.md` | parent | How the design will be validated |
| 2 | `docs/validation/TEST_EQUIPMENT.md` | parent | Fixtures and instruments; restrained-fixture testing (ACT-DEC-015) |
| 3 | `audit/mechanical/MECHANICAL_RISK_REGISTER.md` | parent | Known mechanical risks |
| 4 | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` | parent | What the independent reviewer will check at M0 to M4 |
| 5 | `audit/mechanical/MECHANICAL_RELEASE_CHECKLIST.md` | parent | Release evidence list |
| 6 | `planning/v1/MILESTONE.md` | parent | A0, A1, A2 scope and Gates A/B/C exit criteria |
| 7 | `planning/v1/RISKS_AND_DEPENDENCIES.md` | parent | Project risks and dependencies |
| 8 | `planning/v1/tasks/ACT-02/README.md` | parent | Mechanical task folder guide (legacy ACT-02 IDs map to ACT-M/S/L in `planning/v2/TASK_ID_MAPPING.csv`) |
| 9 | `docs/training/README.md` | parent | Long project training reference: purpose, stages, workstreams, baseline plan. Read sections 1 to 4A and 5; use the rest as reference |

### F. Variant notes (Kritva-S)

Read the `kritva-actuator-m` repository first (its README, `sizing/inputs.json`, and any results): S starts from M's template only after M's sizing and design review pass (ACT-DEC-024 to 026). Then replace the placeholder values in your `sizing/inputs.json` with S-specific values and record the load case for your joint before selecting components. The S class (2-5 N·m continuous, 5-10 N·m peak, about 60 RPM) is provisional. Candidate applications outside the current spec need their own load cases.

If a document you need is missing or contradicts another, raise it with the Project Lead; do not change the interface, CAN protocol, units or decisions in this repository.

## Clone

```bash
# This repository only
git clone https://github.com/KritvaOS/kritva-actuator-s.git
cd kritva-actuator-s
git lfs install    # once per machine; CAD binaries (*.step, *.stp, *.FCStd, *.sldprt, *.sldasm, *.f3d) are stored with Git LFS
git lfs pull
# The whole actuator family (parent plus the four children as submodules)
git clone --recurse-submodules https://github.com/KritvaOS/kritva-actuator.git
```

To push over SSH without changing the stored HTTPS URL, run once: `git config --global url."git@github.com:".pushInsteadOf "https://github.com/"`. Never put credentials in a remote URL. Work in this repository on a branch; do not push to the parent. Only the Project Lead updates the parent's pointer to a child commit, and the parent pins a reviewed commit (parent `docs/standards/SUBMODULE_WORKFLOW.md`).

## Folder structure and responsibilities

| Path | Content | Responsible | Notes |
|---|---|---|---|
| `sizing/inputs.json` | Variant inputs for the shared sizing engine | Mechanical owner | Placeholder values; replace with S-specific values before use |
| `sizing/results/` | Engine outputs, with the parent commit used | Mechanical owner | Record the parent commit for every result |
| `cad/` | `housing/`, `shafts/`, `brackets/`, `encoder_mount/`, `assembly/` | Mechanical owner | Binaries via Git LFS; follow the parent CAD naming standard |
| `drawings/` | Released drawings (PDF plus native) | Mechanical owner | Released only after Gate A |
| `assembly/` | Assembly procedure for this variant | Mechanical owner | |
| `bom/MECHANICAL_BOM.csv` | Mechanical BOM, item prefix ``MB-S-NNN`` | Mechanical owner | Checked by `check_bom.py` |
| `tests/` | Mechanical test plans; `tests/commit_message_check/` tests the commit checker | Mechanical owner | Loaded tests only on a restrained, guarded, instrumented fixture |
| `results/` | Raw evidence: measurements, inspection records | Mechanical owner | |
| `docs/` | Variant design specification, design review checklist and result | Mechanical owner, Project Lead reviews | |
| `scripts/check_bom.py`, `scripts/check_inputs.py` | Vendored BOM and inputs checks | Project Lead | Do not edit here; change them in the parent |
| `scripts/status/` | `gen_status.py` (writes and validates `status/status.json`) and its tests | Project Lead | |
| `scripts/security/check_commit_messages.py` | Commit message checker used by CI | Project Lead / Security Owner | |
| `status/tasks.csv` | Task facts (ID, execution, readiness, commit) | Mechanical owner edits, Project Lead approves | Source for the status report |
| `status/status.json`, `status.schema.json`, `workstream.json` | Generated status report, vendored schema (with `.sha256`), workstream ID | Generated | Never hand-edit `status.json` |
| `Makefile` | `make check`, `check-bom`, `check-inputs`, `check-status` | Project Lead | |
| `.github/workflows/` | `checks.yml`, `commit-message-check.yml`, `secret-scan.yml` | Project Lead | |
| `.github/CODEOWNERS` | Required reviewers | Project Lead | Single owner today |
| `AGENTS.md`, `SECURITY.md` | Rules for contributors and AI assistants; how to report security issues | Project Lead | |
| `.gitattributes`, `.gitignore`, `LICENSE` | LFS rules, ignored files, licence | Project Lead | |

## Tool installation

Required for the checks: `git`, `make`, `python3` (CI uses 3.11 for `checks` and 3.12 for `commit-message-check`), and `git-lfs` for CAD files. The checks use the Python standard library.

```bash
# Debian / Ubuntu
sudo apt install git git-lfs make python3
git lfs install
```

On Windows use WSL or Git Bash. Confirm with `python3 --version` and `make --version`.

Engineering tools are proposed in the parent: FreeCAD for CAD; CadQuery, OpenSCAD and CalculiX are optional. The toolchain is **not yet frozen**; read `docs/standards/TOOLFLOW_MECHANICAL.md` and `OPEN_SOURCE_TOOLFLOW.md` in the parent for the flow, licences and checked references, and do not install a different tool version for released work. Optional: gitleaks 8.18.4 to run the secret scan locally.

## Checks, unit tests and regression

```bash
make check                                  # BOM schema, sizing inputs, status (what CI runs)
python3 -m unittest discover -s tests/commit_message_check -v     # commit checker tests (run by CI)
python3 -m unittest discover -s scripts/status -p "test_*.py" -v  # status generator tests (run locally; not in CI yet)
```

Regression here means all three groups pass before every pull request, and again in CI on every pull request and on every push to `main`. `make check` does not recalculate sizing: the engine and its golden-case checks (`check_calcs`) live in the parent, where the variant inputs are used with `--inputs`. Record the parent commit when you store results. Passing checks is not evidence of mechanical safety or design acceptance.

## Workflow

1. Work on a branch; open a pull request; the owner and reviewer approve.
2. `make check` must pass (BOM schema, sizing inputs, status).
3. Status moves Concept, Designed, Fabricated, Bench-tested, Validated only by independent review. CI success does not promote a design.
4. Loaded, peak-torque and fault tests only on a restrained, guarded, instrumented fixture with a test-readiness record (ACT-DEC-015).
5. Do not edit common interface documents here; raise a design change request in the parent.
6. The mechanical HOLD was lifted in the parent (ACT-DEC-029, 2026-10-18). That does not authorise fabrication, procurement or loaded testing on its own: Gate A and independent review still apply. `AGENTS.md` in this repository was updated to match.

## Git branch, commit and pull request rules

### Branch names

Never commit to `main`; it is protected. Branch from an up-to-date `main`:

```bash
git switch main && git pull --ff-only
git switch -c <type>/<TASK-ID>-<short-topic>      # task work
git switch -c chore/<short-topic>                 # repository housekeeping
```

Examples: `feat/ACT-S-003-shaft-stress-check`, `docs/ACT-S-003-assembly-notes`, `chore/status-regenerate`. Use lowercase and hyphens. The `ACT-S` task IDs are in `status/tasks.csv`. These names are a recommendation that matches the existing `chore/...` branches; CI does not enforce them.

### Commit messages

Use a short imperative subject in one of these forms (parent `docs/standards/PROGRAM_ALIGNMENT.md`, section 3):

```text
ACT-S-003: add shaft stress check inputs        <- preferred when the work belongs to a task
type(scope): summary                            <- repository style, for example chore(status): regenerate status.json
```

Suggested `type` values: `feat`, `fix`, `docs`, `test`, `chore`, `design` (CAD or drawings). One atomic change per commit. Do not claim a test, review or acceptance that did not happen. Do not rewrite or renumber history.

What CI **does** enforce (`commit-message-check`): a commit must not contain a `Claude-Session:` trailer or a `claude.ai/code/session` link. A `Co-Authored-By:` line is allowed. Everything else above is a convention.

To catch a rejected message before pushing, install the local hook once (from the repository root):

```bash
printf '#!/bin/sh\npython3 scripts/security/check_commit_messages.py --file "$1"\n' > .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

### Pull requests

1. Push the branch and open a pull request into `main`.
2. Run `make check` first (see Checks above).
3. `main` requires `secret-scan`, `commit-message-check` and Code Owner review (owner statement; see `AGENTS.md`). With one owner, the PR author cannot approve their own PR: ask the owner to merge using the bypass, or add a second reviewer.
4. Status moves only through independent review. A green CI run never promotes a design or closes a gate.

## How to find out why a pull request failed

1. Open the pull request, scroll to the checks box at the bottom (or open the **Checks** tab). A red cross marks the failed check.
2. Click **Details** next to it and expand the failed step. The error line is usually at the end of that step.
3. Or from a terminal with the GitHub CLI: `gh pr checks <PR-number>`, then `gh run list --branch <branch>` and `gh run view <run-id> --log-failed`.
4. Reproduce it locally with the command in the table, fix, commit, and push to the same branch; the checks rerun.

| Failed check | What it ran | Reproduce locally | Usual cause and fix |
|---|---|---|---|
| `checks` | `make check`: BOM schema, sizing inputs, status | `make check` (or one target: `make check-bom`, `make check-inputs`, `make check-status`) | `check-bom`: wrong column or duplicate item ID in `bom/MECHANICAL_BOM.csv`. `check-inputs`: a key is missing or not a number in `sizing/inputs.json`. `check-status`: `status/status.json` is out of date; run `python3 scripts/status/gen_status.py --root .` and commit the result (never edit it by hand) |
| `commit-message-check` | Unit tests of the checker, then the checker on every commit in the PR | `python3 -m unittest discover -s tests/commit_message_check -v` then `python3 scripts/security/check_commit_messages.py --range origin/main..HEAD` | A commit carries a `Claude-Session:` trailer or session link. Amend the latest unpushed commit (`git commit --amend`). For commits already pushed, ask the owner before rewriting history |
| `secret-scan` | gitleaks 8.18.4 over the full git history | Install gitleaks 8.18.4, then `gitleaks detect --source . --redact --verbose --exit-code 1` | A credential, key or token is in the history. Do not add an allowlist entry. Tell the Security Owner (Dinesh) at once; the secret must be revoked or rotated, and removing it in a later commit is not enough |

If the failure is in a step you did not touch, rerun the job once from the Actions page; if it fails again, ask the owner. If the log shows a missing tool or Python module, the runner image changed: report it rather than disabling the check.
