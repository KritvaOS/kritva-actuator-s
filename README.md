# Kritva Actuator Kritva-S

> Mechanical design, sizing inputs, BOM, drawings and test plans for the Kritva-S variant of the Kritva actuator family. Child repository of the actuator parent. This is a private repository.

| Property | Value |
|---|---|
| Project | KritvaOS |
| Repository | `KritvaOS/kritva-actuator-s` |
| Repository Type | Mechanical (child of the actuator parent repository) |
| Visibility Class | PRIVATE (future private; ACT-DEC-023, D-037, D-039 in kritva-program) |
| GitHub Setting | PUBLIC (verified 2026-10-18; temporary, ACT-DEC-023 amendments and D-028: owner action returns it to private) |
| Lifecycle Status | ACTIVE (concept stage; no design artefact committed) |
| Repository Owner | Mechanical Intern 1 (role); Project Lead approves |
| Security Owner | Security Owner role ([SECURITY.md](SECURITY.md)) |
| Architecture | [Parent docs/architecture/ACTUATOR_FAMILY_SPEC.md](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/architecture/ACTUATOR_FAMILY_SPEC.md) and [parent docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md) |
| Milestones | [Parent planning/v1/MILESTONE.md](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v1/MILESTONE.md) and [parent planning/v2/ROADMAP_48_WEEKS.md](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v2/ROADMAP_48_WEEKS.md) |
| Tasks | [status/tasks.csv](status/tasks.csv) |
| Acceptance Criteria | [Parent audit/mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md](https://github.com/KritvaOS/kritva-actuator/blob/main/audit/mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md) |
| Status Reporting | [status/status.json](status/status.json) (generated) |
| License | [LICENSE](LICENSE) (proprietary, all rights reserved) |

This README follows the Kritva README standard (`v2/planning/standards/README_STANDARD.md` in [kritva-program](https://github.com/KritvaOS/kritva-program)). It is a navigation map; the documents it links own the detail. Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

## 1. Purpose and Scope

Child repository of `KritvaOS/kritva-actuator` (the parent). It owns the mechanical design of the Kritva-S variant: variant sizing inputs for the shared sizing engine, CAD, drawings, assembly procedure, mechanical BOM (item prefix `MB-S-NNN`), mechanical test plans and the evidence records. Kritva-S is about 2-5 N·m continuous, 5-10 N·m peak, about 60 RPM (provisional, not approved).

**Status: Concept.** `sizing/inputs.json` holds **placeholder** values: only the torque and speed fields differ from M. Arm and payload masses, shaft dimensions and the other fields are copied from M and must be replaced by S-specific values before they are used.

**Implementation state.** IMPLEMENTED today: the sizing inputs file `sizing/inputs.json` (PLACEHOLDER values copied from M; only the torque and speed fields are S-specific); the BOM schema check and an empty BOM file (header only, no item rows); the sizing-inputs check, the status generator and its tests, the commit message checker, the README check and the CI workflows. NOT YET IMPLEMENTED: all CAD (`cad/`), drawings, the assembly procedure, test plans, the variant design documents (`docs/`), every sizing result (`sizing/results/`) and every measurement (`results/`). A folder or document existing is not evidence that the design it names is built or accepted.

It does not own the common interface, the CAN protocol, units, the shared sizing engine or program-level decisions; the parent owns them and they are not redefined here. Read the parent's `docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md` first.

## 2. Position in the KritvaOS Ecosystem

This is the Kritva-S mechanical child of the actuator family. The parent `kritva-actuator` is intended to track it as a submodule (`mechanical/actuator-s`) and pin a reviewed commit; only the Project Lead updates that pointer. This README does not verify the current pointer. Four states are different: submodule configured in the parent's `.gitmodules`, pointer recorded by a parent commit, checkout initialised in a clone, and implementation verified. Work here goes on a branch in this repository; do not push to the parent. The roster and order of repositories in the program are owned by kritva-program (`v2/planning/repo-pipeline.json`), not by this README.

## 3. Architecture

The design is proposed, not frozen. The mechanical architecture, the family classes and the interface control document are owned by the parent and are not redefined here; this repository will hold the variant design that implements them. Nothing in the architecture is implemented as CAD or hardware in this repository yet.

- **Variant class.** Kritva-S: about 2-5 N·m continuous, 5-10 N·m peak, about 60 RPM. Provisional (ACT-DEC-025, PROPOSED), not an approved requirement.
- **Sizing.** `sizing/inputs.json` feeds the shared sizing engine in the parent (`mechanical/common-sizing/`). The engine and its golden-case checks live in the parent; `make check` here does not recalculate sizing.
- **Interfaces.** Mechanical, electrical and CAN interfaces come from the parent ICD.

### Variant classes (provisional)

| Class | Repository baseline (ACT-DEC-025, PROPOSED) | Wider planning range (under review, not approved) | Typical joints |
|---|---|---|---|
| Kritva-S | 2-5 N·m continuous, 5-10 N·m peak, about 60 RPM | 2-5 / 5-10 N·m | Wrist, neck |
| Kritva-M | 10 N·m continuous, 20-25 N·m peak, 45 RPM (elbow baseline and A0 reference, ACT-DEC-008) | 5-20 / 20-40 N·m | Elbow, shoulder (shoulder not yet in the spec) |
| Kritva-L | 25-40 N·m continuous, 50-80 N·m peak, about 20-40 RPM | 20-80 / 80-150 N·m | Hip, knee, ankle (ankle not yet in the spec) |

Use the repository baseline column for sizing and reviews. The wider range is a discussion input; it becomes a requirement only after the owner records it in `planning/v1/DECISIONS.md`. For L the two columns differ materially, so confirm the intended load cases first.

## 4. Documents to Read First

Read in this order. "parent" means a path inside the `kritva-actuator` parent repository (clone it with `--recurse-submodules`, see below); "this repo" means this repository. A label names a role, not an approval; the status a document declares is what counts, and each row shows the role first and the status after it. AUTHORITATIVE here marks the intended source of detail, not an approved baseline: design release, purchasing, fabrication and release stay subject to the recorded decisions and gates. Values marked PROPOSED, provisional or not yet defined are not approved requirements. Links to the parent point at its `main` branch (current links); the parent record's own status and revision control, not this README. Tool flows are proposed, not frozen. Passing checks does not close a gate.

### A. Before you start (first week)

| # | Document | Where | Label, status | What to take from it |
|---|---|---|---|---|
| 1 | [`README.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/README.md) | parent | AUTHORITATIVE | Stages A0/A1/A2, design baseline (proposed, not frozen), repository structure, roles, safety |
| 2 | `AGENTS.md` | this repo and parent | AUTHORITATIVE | Rules for people and AI agents: gates, what not to change, no waivers |
| 3 | [`planning/v1/DECISIONS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v1/DECISIONS.md) | parent | AUTHORITATIVE; each decision has its own status | Decision index and status. Read ACT-DEC-001 to 009, 014, 015, 024 to 033 and the pending list (section 5) before choosing parts |
| 4 | [`planning/v2/ROADMAP_48_WEEKS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v2/ROADMAP_48_WEEKS.md) | parent | REFERENCE (plan; read its own status line) | Current reforecast (P-weeks): A0 exit P12, Gate A, release gap, M fabrication, PCB spins, gates. Sections 3 to 5 |
| 5 | [`planning/v2/WORKSTREAMS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v2/WORKSTREAMS.md) | parent | REFERENCE (plan; read its own status line) | Who owns what, hand-offs between workstreams |
| 6 | [`docs/standards/SUBMODULE_WORKFLOW.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/SUBMODULE_WORKFLOW.md) | parent | REFERENCE | How child commits are pinned in the parent; branches and pull requests |

### B. Requirements, architecture and interfaces

| # | Document | Where | Label, status | What to take from it |
|---|---|---|---|---|
| 1 | [`requirements/SYSTEM_REQUIREMENTS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/requirements/SYSTEM_REQUIREMENTS.md) | parent | AUTHORITATIVE for the requirement; status per file | System limits: torque, speed, budget (SYS-REQ-100), provisional assumptions |
| 2 | [`requirements/MECHANICAL_REQUIREMENTS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/requirements/MECHANICAL_REQUIREMENTS.md) | parent | AUTHORITATIVE for the requirement; status per file | What the mechanical design must satisfy |
| 3 | [`requirements/SAFETY_REQUIREMENTS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/requirements/SAFETY_REQUIREMENTS.md) | parent | AUTHORITATIVE for the requirement; status per file | Safety limits; hard stops, restrained-fixture rule |
| 4 | [`requirements/INTERFACE_REQUIREMENTS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/requirements/INTERFACE_REQUIREMENTS.md) | parent | AUTHORITATIVE for the requirement; status per file | Mounting, shaft and connector interface requirements |
| 5 | [`requirements/ACTUATOR_SPECIFICATION.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/requirements/ACTUATOR_SPECIFICATION.md) | parent | AUTHORITATIVE for the requirement; status per file | Actuator-level specification |
| 6 | [`docs/architecture/ACTUATOR_ARCHITECTURE.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/architecture/ACTUATOR_ARCHITECTURE.md) | parent | REFERENCE | Actuator architecture and boundaries |
| 7 | [`docs/architecture/ACTUATOR_FAMILY_SPEC.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/architecture/ACTUATOR_FAMILY_SPEC.md) | parent | AUTHORITATIVE for the family classes; PROPOSED (ACT-DEC-025) | S/M/L classes (provisional, ACT-DEC-025). Repository baseline values are the ones to use |
| 8 | [`docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md) | parent | REFERENCE | The common interface; never redefine it in this repo |
| 9 | [`docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md) | parent | REFERENCE | Units, signs, conventions used in every calculation |

### C. Mechanical design and calculations

| # | Document | Where | Label, status | What to take from it |
|---|---|---|---|---|
| 1 | [`docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md) | parent | REFERENCE | Mechanical design baseline: housing, shaft, bearings, gearbox mount |
| 2 | [`mechanical/calculations/LOAD_CASES.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/mechanical/calculations/LOAD_CASES.md) | parent | REFERENCE (reference calculations; status per file) | Elbow load case and assumptions (centre of mass is provisional) |
| 3 | [`mechanical/calculations/TORQUE_AND_SPEED.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/mechanical/calculations/TORQUE_AND_SPEED.md) | parent | REFERENCE (reference calculations; status per file) | Torque and speed derivation |
| 4 | [`mechanical/calculations/SHAFT_STRENGTH.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/mechanical/calculations/SHAFT_STRENGTH.md) | parent | REFERENCE (reference calculations; status per file) | Shaft method: torsion, bending, combined, fatigue, deflection |
| 5 | [`mechanical/calculations/BEARING_SELECTION.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/mechanical/calculations/BEARING_SELECTION.md) | parent | REFERENCE (reference calculations; status per file) | Bearing loads, life, fits, preload |
| 6 | [`mechanical/calculations/GEARBOX_SELECTION.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/mechanical/calculations/GEARBOX_SELECTION.md) | parent | REFERENCE (reference calculations; status per file) | Gearbox limits and selection criteria (ACT-DEC-003) |
| 7 | [`mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md) | parent | REFERENCE (reference calculations; status per file) | Candidate motor and gearbox pairs |
| 8 | [`mechanical/common-sizing/README.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/mechanical/common-sizing/README.md) | parent | REFERENCE (reference calculations; status per file) | How to run the shared sizing engine with this repo's `sizing/inputs.json` |
| 9 | [`docs/mechanical/MATERIAL_SELECTION.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/mechanical/MATERIAL_SELECTION.md) | parent | REFERENCE | Material choices and rules |
| 10 | [`docs/mechanical/FABRICATION_GUIDELINES.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/mechanical/FABRICATION_GUIDELINES.md) | parent | REFERENCE | Manufacturing constraints before drawings are released |
| 11 | [`docs/mechanical/ASSEMBLY_PROCEDURE.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/mechanical/ASSEMBLY_PROCEDURE.md) | parent | REFERENCE | Assembly steps and inspection |

### D. Standards and tool flow

| # | Document | Where | Label, status | What to take from it |
|---|---|---|---|---|
| 1 | [`docs/standards/TOOLFLOW_MECHANICAL.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/TOOLFLOW_MECHANICAL.md) | parent | REFERENCE; PROPOSED (not frozen) | Your tool flow (FreeCAD, checks, Gate A, release). Toolchain is proposed, not frozen |
| 2 | [`docs/standards/OPEN_SOURCE_TOOLFLOW.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/OPEN_SOURCE_TOOLFLOW.md) | parent | REFERENCE; PROPOSED (not frozen) | Full tool reasoning, licences and the checked reference links (GitHub, YouTube) |
| 3 | [`docs/standards/CAD_NAMING_STANDARD.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/CAD_NAMING_STANDARD.md) | parent | REFERENCE | File, part and assembly naming |
| 4 | [`docs/standards/BOM_STANDARD.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/BOM_STANDARD.md) | parent | REFERENCE | BOM columns and rules (`make check` enforces them) |
| 5 | [`docs/standards/DESIGN_REVIEW_CHECKLIST.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/DESIGN_REVIEW_CHECKLIST.md) | parent | REFERENCE | Complete before Gate A; fabrication starts only after Gate A plus the release gap |
| 6 | [`docs/standards/RELEASE_CHECKLIST.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/RELEASE_CHECKLIST.md) | parent | REFERENCE | What a release needs |
| 7 | [`docs/standards/PROGRAM_ALIGNMENT.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/PROGRAM_ALIGNMENT.md) | parent | REFERENCE | How status reporting and HOLD relate to kritva-program |

### E. Validation, audit and planning

| # | Document | Where | Label, status | What to take from it |
|---|---|---|---|---|
| 1 | [`docs/validation/VALIDATION_PLAN.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/validation/VALIDATION_PLAN.md) | parent | REFERENCE | How the design will be validated |
| 2 | [`docs/validation/TEST_EQUIPMENT.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/validation/TEST_EQUIPMENT.md) | parent | REFERENCE | Fixtures and instruments; restrained-fixture testing (ACT-DEC-015) |
| 3 | [`audit/mechanical/MECHANICAL_RISK_REGISTER.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/audit/mechanical/MECHANICAL_RISK_REGISTER.md) | parent | REFERENCE (review criteria) | Known mechanical risks |
| 4 | [`audit/mechanical/MECHANICAL_DESIGN_AUDIT.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/audit/mechanical/MECHANICAL_DESIGN_AUDIT.md) | parent | REFERENCE (review criteria) | What the independent reviewer will check at M0 to M4 |
| 5 | [`audit/mechanical/MECHANICAL_RELEASE_CHECKLIST.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/audit/mechanical/MECHANICAL_RELEASE_CHECKLIST.md) | parent | REFERENCE (review criteria) | Release evidence list |
| 6 | [`planning/v1/MILESTONE.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v1/MILESTONE.md) | parent | REFERENCE (plan; read its own status line) | A0, A1, A2 scope and Gates A/B/C exit criteria |
| 7 | [`planning/v1/RISKS_AND_DEPENDENCIES.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v1/RISKS_AND_DEPENDENCIES.md) | parent | REFERENCE (plan; read its own status line) | Project risks and dependencies |
| 8 | [`planning/v1/tasks/ACT-02/README.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/planning/v1/tasks/ACT-02/README.md) | parent | REFERENCE (plan; read its own status line) | Mechanical task folder guide (legacy ACT-02 IDs map to ACT-M/S/L in `planning/v2/TASK_ID_MAPPING.csv`) |
| 9 | [`docs/training/README.md`](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/training/README.md) | parent | REFERENCE | Long project training reference: purpose, stages, workstreams, baseline plan. Read sections 1 to 4A and 5; use the rest as reference |

### F. Variant notes (Kritva-S)

Read the `kritva-actuator-m` repository first (its README, `sizing/inputs.json`, and any results): S starts from M's template only after M's sizing and design review pass (ACT-DEC-024 to 026). Then replace the placeholder values in your `sizing/inputs.json` with S-specific values and record the load case for your joint before selecting components. The S class (2-5 N·m continuous, 5-10 N·m peak, about 60 RPM) is provisional. Candidate applications outside the current spec need their own load cases.

If a document you need is missing or contradicts another, raise it with the Project Lead; do not change the interface, CAN protocol, units or decisions in this repository.

## 5. Repository Structure and File Responsibilities

Labels: INPUT is edited by hand and read by a tool or review; GENERATED is written by a tool and never edited; EVIDENCE supports a claim and is append-only; AUTHORITATIVE owns a rule; SNAPSHOT is a copy of facts owned elsewhere. A label is a role, not an approval. Only the files named in the implementation state (section 1) hold real content; the other folders are scaffolding.

| Path | Content | Label, status | Responsible | Notes |
|---|---|---|---|---|
| `sizing/inputs.json` | Variant inputs for the shared sizing engine | INPUT | Mechanical owner | Placeholder values; replace with variant-specific values before use |
| `sizing/results/` | Engine outputs, with the parent commit used | EVIDENCE; NOT YET IMPLEMENTED (empty) | Mechanical owner | Record the parent commit for every result |
| `cad/` | `housing/`, `shafts/`, `brackets/`, `encoder_mount/`, `assembly/` | INPUT; NOT YET IMPLEMENTED (empty) | Mechanical owner | Binaries via Git LFS; follow the parent CAD naming standard |
| `drawings/` | Released drawings (PDF plus native) | INPUT; NOT YET IMPLEMENTED (empty) | Mechanical owner | Released only after Gate A |
| `assembly/` | Assembly procedure for this variant | INPUT; NOT YET IMPLEMENTED (empty) | Mechanical owner | |
| `bom/MECHANICAL_BOM.csv` | Mechanical BOM, item prefix `MB-S-NNN` | INPUT; header only, no item rows | Mechanical owner | Checked by `check_bom.py` |
| `tests/` | Mechanical test plans (none yet); `tests/commit_message_check/` tests the commit checker | EVIDENCE | Mechanical owner | Loaded tests only on a restrained, guarded, instrumented fixture |
| `results/` | Raw evidence: measurements, inspection records | EVIDENCE; NOT YET IMPLEMENTED (empty) | Mechanical owner | |
| `docs/` | Variant design specification, design review checklist and result | AUTHORITATIVE as the intended source of design detail; NOT YET IMPLEMENTED (empty) | Mechanical owner, Project Lead reviews | |
| `scripts/check_bom.py`, `scripts/check_inputs.py` | Vendored BOM and inputs checks | INPUT; IMPLEMENTED (vendored copy) | Project Lead | Do not edit here; change them in the parent |
| `scripts/status/` | `gen_status.py` (writes and validates `status/status.json`) and its tests | INPUT; IMPLEMENTED | Project Lead | |
| `scripts/security/check_commit_messages.py` | Commit message checker used by CI | INPUT | Project Lead / Security Owner | |
| `scripts/check_readme.py` | README structure check | INPUT | Project Lead | Structural only |
| `status/tasks.csv` | Task facts (ID, execution, readiness, commit) | INPUT | Mechanical owner edits, Project Lead approves | Source for the status report |
| `status/status.json`, `status.schema.json`, `workstream.json` | Generated status report, vendored schema (with `.sha256`), workstream ID | GENERATED (`status.json`); SNAPSHOT (vendored schema) | Generated | Never hand-edit `status.json` |
| `Makefile` | `make check`, `check-bom`, `check-inputs`, `check-status`, `check-readme` | INPUT; IMPLEMENTED | Project Lead | |
| `.github/workflows/` | `checks.yml`, `commit-message-check.yml`, `secret-scan.yml` | AUTHORITATIVE | Project Lead | |
| `.github/CODEOWNERS` | Required reviewers | AUTHORITATIVE | Project Lead | Single owner today |
| `AGENTS.md`, `SECURITY.md`, `.gitattributes`, `.gitignore`, `LICENSE` | Contributor and AI-assistant rules, security reporting, LFS rules, ignored files, licence | AUTHORITATIVE | Project Lead | |

## 6. Toolchain and Development Workflow

| Tool | Purpose | Version | Check |
|---|---|---|---|
| git, GNU make | Version control, local commands | any recent | `git --version`, `make --version` |
| Python 3 | The checks (standard library only) | 3.11 in the `checks` workflow, 3.12 in `commit-message-check` | `python3 --version` |
| CAD, FEA and drawing tools | Mechanical design flow | PROPOSED in the parent, not frozen | not applicable yet |

### Setup

Required for the checks: `git`, `make`, `python3` (CI uses 3.11 for `checks` and 3.12 for `commit-message-check`), and `git-lfs` for CAD files. The checks use the Python standard library.

```bash
# Debian / Ubuntu
sudo apt install git git-lfs make python3
git lfs install
```

On Windows use WSL or Git Bash. Confirm with `python3 --version` and `make --version`.

Engineering tools are proposed in the parent: FreeCAD for CAD; CadQuery, OpenSCAD and CalculiX are optional. The toolchain is **not yet frozen**; read `docs/standards/TOOLFLOW_MECHANICAL.md` and `OPEN_SOURCE_TOOLFLOW.md` in the parent for the flow, licences and checked references, and do not install a different tool version for released work. Optional: gitleaks 8.18.4 to run the secret scan locally.

### Clone

```bash
# This repository only
git clone https://github.com/KritvaOS/kritva-actuator-s.git
cd kritva-actuator-s
git lfs install    # once per machine; CAD binaries (*.step, *.stp, *.FCStd, *.sldprt, *.sldasm, *.f3d) are stored with Git LFS
git lfs pull
# The whole actuator family (parent plus the four children as submodules)
git clone --recurse-submodules https://github.com/KritvaOS/kritva-actuator.git
```

`--recurse-submodules` initialises the child checkouts at the pointers the parent records and needs read access to each child repository; which commit you get depends on the parent's current pointers.

To push over SSH without changing the stored HTTPS URL, you can set a URL rewrite. The command below MODIFIES your global Git configuration (it affects every repository for your user): `git config --global url."git@github.com:".pushInsteadOf "https://github.com/"`. Inspect it with `git config --global --get-regexp pushinsteadof` and remove it with `git config --global --unset url."git@github.com:".pushInsteadOf`. To limit the rewrite to one repository, run the same command with `--local` inside it instead of `--global`. Never put credentials in a remote URL. Work in this repository on a branch; do not push to the parent. Only the Project Lead updates the parent's pointer to a child commit, and the parent is intended to pin a reviewed commit (parent `docs/standards/SUBMODULE_WORKFLOW.md`).

## 7. Dependencies and Interfaces

| Dependency | Direction | Kind | Contract | State |
|---|---|---|---|---|
| kritva-actuator (parent) | upstream | governance, requirements, interface, sizing engine | parent ICD, requirements, `mechanical/common-sizing/`, `planning/v1/DECISIONS.md` | ESTABLISHED as the owner of the interface; the pointer is intended to be pinned by the Project Lead (current pointer not verified here) |
| kritva-actuator-m (reference) | sibling | design reference | `sizing/inputs.json` structure and checklists | PLANNED: variants reuse M's structure only after M's sizing and design review pass (ACT-DEC-024 to 026) |
| kritva-actuator-embedded | sibling | electrical and firmware interface | parent interface documents | PLANNED: no mechanical-to-electronics interface is implemented |
| kritva-program | upstream | governance and status | status schema 2.0 (`status/`) | planning-only reporting; no program credit |
| CAD, FEA and drawing tools | upstream | tools | parent `TOOLFLOW_MECHANICAL.md` | PROPOSED, not frozen |

Five kinds of relationship are kept apart: program ordering, Git submodule (the parent configures and pins this repository), source or build dependency, runtime integration, and governance or status reporting. The interface documents the parent owns are PROPOSED until approved, and no test yet checks that this design conforms to them. A PROPOSED dependency is not an integration that exists.

## 8. Milestones and Implementation Plan

Stage scope is held in the parent `planning/v1/ROADMAP.md` and `planning/v1/MILESTONE.md`; the current reforecast is the parent `planning/v2/ROADMAP_48_WEEKS.md`. Stage names, budgets and dates here are provisional planning information, not approved requirements, and nothing here authorises purchase, fabrication or design freeze. Dates are planning targets, not commitments.

### Stage comparison: A0 and A1 (provisional planning information)

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
| Deliverable | Working motor-control platform with firmware, tests and documents | Target: an actuator ready for validation, with CAD, BOM, firmware and test reports. "Validated" is reserved for a specific unit and configuration whose acceptance evidence is recorded, and depends on the design being built, physical testing, independent review and Gates A, B and C; software checks alone cannot satisfy it |

Dates, phase numbers and checkpoints in the reforecast are proposed planning targets; read the parent roadmap for any date.
## 9. Tasks and Acceptance Criteria

- **Where tasks live.** [status/tasks.csv](status/tasks.csv) holds the task facts (`ACT-S-nnn`, with the legacy `ACT-02-nnn` IDs mapped in the parent `planning/v2/TASK_ID_MAPPING.csv`). The Mechanical owner edits it and the Project Lead approves.
- **Acceptance criteria.** The criteria for the mechanical gates (M0 to M4) are in the parent `audit/mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md`. Safety-relevant changes need the Independent Mechanical Reviewer (ACT-DEC-014).
- Work is not accepted because code, a commit, a merged pull request, a CAD file or a passing check exists. Acceptance is a recorded review decision, not a status field. The design status moves Concept, Designed, Fabricated, Bench-tested, Validated only by independent review; CI success does not promote a design.

## 10. Status Reporting and Program Integration

`status/status.json` (schema 2.0) is generated by `scripts/status/gen_status.py` from `status/tasks.csv`; never edit it by hand. The reports are planning-only: this repository reports facts only, its tasks are not in the approved program baseline, and nothing here creates program credit. Execution, evidence, acceptance and release readiness are kept apart:

| Dimension | Source record | Authority |
|---|---|---|
| Execution | `status/tasks.csv`, reported in `status/status.json` | The Mechanical owner records it; the Project Lead approves |
| Evidence | None is recorded today (`results/` and `sizing/results/` are empty). By type: a software test names the source commit, command and result; a calculation or simulation names the model, inputs and assumptions; a physical test names the hardware configuration, procedure, instruments and conditions, and result | The author records it; a reviewer other than the author checks it |
| Acceptance | The parent's gate and audit records (`audit/`) | The independent reviewer and the Project Lead, never a status report |
| Release readiness | The parent's Gates A, B and C | Project Lead with a qualified safety reviewer |

Evidence has types that are not interchangeable (software test, calculation, simulation, bench measurement, independently accepted physical test). `status/status.json` carries no evidence today, every task's execution is NOT_STARTED, and the readiness values PLANNABLE and HARDWARE-BLOCKED describe planning constraints, not safety or release approval. A generated view is a snapshot that can lag its inputs, cannot approve its own work, and does not establish physical safety or program credit. Regenerate it with `python3 scripts/status/gen_status.py --root .`.

## 11. Build, Test, Regression and Validation

CI runs three separate workflows (below). None is a design calculation, a CAD review or a physical test: `make check` does not recalculate sizing (the engine and its golden-case checks live in the parent), and a passing check does not close a gate.

| Workflow | Trigger | What it runs |
|---|---|---|
| `checks` | push to `main`; pull requests | `make check` (BOM schema, sizing inputs keys and status only) |
| `commit-message-check` | pull requests | the commit checker's unit tests, then the checker on the commits in the pull request (rejects session trailers and links only) |
| `secret-scan` | push to `main`; pull requests; manual dispatch | gitleaks over the git history |

| Check | Command | Effect | Runs in CI? |
|---|---|---|---|
| BOM schema | `make check-bom` | check | yes (`checks`) |
| Sizing inputs against the engine keys | `make check-inputs` | check | yes (`checks`) |
| Status report against `status/tasks.csv` | `make check-status` | check | yes (`checks`) |
| All of the above | `make check` | check | yes |
| README standard | `make check-readme` | check | no, run locally |
| README checker regression tests | `python3 -m unittest discover -s tests/readme_check -v` | check | no, run locally |
| Commit checker tests | `python3 -m unittest discover -s tests/commit_message_check -v` | check | yes (`commit-message-check`) |
| Status generator tests | `python3 -m unittest discover -s scripts/status -p "test_*.py" -v` | check | no, run locally |
| Regenerate the status report | `python3 scripts/status/gen_status.py --root .` | generate (rewrites `status/status.json`) | no |
| Install the local commit-msg hook | `printf ... > .git/hooks/commit-msg` (section 12) | modify (writes a local hook file) | no |

The Makefile has only the check targets above; there is no clean or generate target. Loaded, peak-torque and fault tests are never run in CI: they need a restrained, guarded, instrumented fixture with a test-readiness record (ACT-DEC-015), and a test that is not run is recorded as not run, never as passing.

### How to find out why a pull request failed

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

## 12. Git Workflow and Review

Repository convention: either subject form below (a task-ID prefix, or `type(scope): summary`, described in the parent `docs/standards/PROGRAM_ALIGNMENT.md`, section 3). CI enforces only that a commit carries no `Claude-Session:` trailer or `claude.ai/code/session` link; neither subject form is checked by CI. Local style checks (`scripts/security/check_commit_format.py`) are advisory. The Kritva commit standard in kritva-program (D-053: `type(scope): summary` with a `Task:` or `Tasks:` footer) is NOT adopted here (PD-019). `AGENTS.md` names the `type(scope): summary` form; the task-ID prefix is also accepted.

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

## 13. Safety and Security

This repository will hold the mechanical design of a load-bearing rotary actuator. It is experimental and not human-safe. Software checks, analytical calculations and simulation validate only the stated model, inputs and software properties. They do not establish physical safety, component suitability, design acceptance or readiness for human use, and they do not close a gate; physical test evidence, independent review and the applicable gate approvals are required separately. Never resist the actuator by hand or attach it to a person. Loaded, peak and fault tests happen only on a restrained, guarded, instrumented fixture.

The lifecycle status ACTIVE describes this repository, not hardware readiness. Lifting the mechanical HOLD (ACT-DEC-029) does not approve a design, waive a gate or authorise fabrication, procurement or loaded testing. The gates are defined in the parent (`planning/v1/MILESTONE.md` sections 6.4 and 8.4, records in `audit/release/`); the table below is this repository's gate summary, not the gate authority: it lists only the mechanical contribution to each gate and not the complete closure criteria, and it does not state current status. Closing a mechanical input does not close the parent gate or authorise the controlled activity; the parent record controls.

| Gate | Controls | Required closed inputs (mechanical) | Decision maker | Prohibited while open |
|---|---|---|---|---|
| A, design release | Release of the design for fabrication | M0, M1, M2; independent shaft, bearing and housing calculation review (SAF-REQ-044) | Project Lead | Procurement, design freeze and fabrication, and the first loaded test |
| B, bench validation | Claims that the bench performance targets are met | M3 | Project Lead | Treating any torque, speed, thermal or accuracy target as demonstrated |
| C, safety and release | Safety sign-off and release | M4; verification of every SAF-REQ item (SAF-REQ-080) | Project Lead with a qualified safety reviewer | Release, and any use outside the restrained, guarded, instrumented fixture |

The independent review (ACT-DEC-014, ACT-DEC-015) applies throughout.

**Reporting a vulnerability:** follow [`SECURITY.md`](SECURITY.md); its reporting route is not yet verified as a dedicated private channel, and it says so. Never put details of an unfixed vulnerability in a public issue, pull request or commit message.

- Never commit secrets, private keys, tokens, passwords, production data or personal data. Use obviously fake values and mark them as fake.
- If a secret is committed by mistake, tell the Security Owner at once; removing it in a later commit does not make it safe. Do not add `secret-scan` allowlist entries.

## 14. Release and Versioning

There is no design release, drawing release or version tag in this repository yet. Drawings are released only after Gate A. A release needs the parent's [release checklist](https://github.com/KritvaOS/kritva-actuator/blob/main/docs/standards/RELEASE_CHECKLIST.md) and the gates; a release is complete only when those criteria are met, not when a file is merged. This README records no release state.

## 15. Ownership and Escalation

| Role | Responsibility |
|---|---|
| Mechanical Intern 1 (repository owner) | Works the mechanical tasks; edits `status/tasks.csv` |
| Project Lead | Approves tasks, owns scripts and workflows, updates the parent's pointer to this repository |
| Independent Mechanical Reviewer | Reviews safety-relevant design and calculations (ACT-DEC-014) |
| Security Owner | Handles vulnerability reports and committed secrets |

If a document you need is missing or contradicts another, raise it with the Project Lead; do not change the interface, CAN protocol, units or decisions in this repository.

## 16. Related Repositories and References

| Repository | Relationship |
|---|---|
| [kritva-actuator](https://github.com/KritvaOS/kritva-actuator) | Parent: interface, CAN protocol, requirements, decisions, sizing engine, validation, audit |
| [kritva-actuator-s](https://github.com/KritvaOS/kritva-actuator-s), [kritva-actuator-m](https://github.com/KritvaOS/kritva-actuator-m), [kritva-actuator-l](https://github.com/KritvaOS/kritva-actuator-l) | The mechanical variants (this is one of them); M is the reference |
| [kritva-actuator-embedded](https://github.com/KritvaOS/kritva-actuator-embedded) | Firmware and controller hardware for the whole family |
| [kritva-program](https://github.com/KritvaOS/kritva-program) | Program plan, baseline, decisions, README standard |

## 17. License

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved. See [LICENSE](LICENSE).
