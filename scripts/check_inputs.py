#!/usr/bin/env python3
"""Check sizing/inputs.json has every key the shared sizing engine expects.

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.
The engine itself lives in the parent repository (mechanical/common-sizing/).
Standard library only. Exit 0 ok, 1 errors.
"""
import argparse, json, sys
from pathlib import Path

REQUIRED = ["E_steel_GPa", "G_steel_GPa", "Kt_keyway", "Kt_shoulder", "T_cont_Nm", "T_peak_min_Nm", "T_peak_stretch_Nm", "alpha_examples", "bumper_stroke_mm", "d_shaft_mm", "eta_gb", "life_hours_target", "m_arm_kg", "m_pay_kg", "mean_speed_rpm", "n_out_rpm", "overhang_a_mm", "r_arm_m", "r_pay_m", "ratios", "s0_required", "shaft_free_len_mm", "span_L_mm", "speed_margin", "stop_radius_mm", "v_bus", "v_usable_frac"]
NUMERIC_LISTS = {"ratios", "alpha_examples"}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    a = ap.parse_args(argv)
    p = Path(a.root) / "sizing" / "inputs.json"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"ERROR: cannot read {p}: {e}")
        return 1
    errors = [f"missing key {k}" for k in REQUIRED if k not in data]
    for k, v in data.items():
        if k in NUMERIC_LISTS:
            ok = isinstance(v, list) and v and all(isinstance(x, (int, float)) for x in v)
        else:
            ok = isinstance(v, (int, float)) and not isinstance(v, bool)
        if not ok and k in REQUIRED:
            errors.append(f"bad value for {k}")
    for e in errors:
        print("ERROR:", e)
    print(f"check_inputs: {len(data)} key(s), {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
