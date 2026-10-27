"""Platform-tolerant check of contrast_search.json (numerical evidence only).
Part 2 (R*, a bisection) must match the shipped value within 1e-6 relative.
Part 1 (multistart SLSQP) is platform-sensitive: the shipped value 14.41 was
obtained on macOS arm64; other BLAS/CPU builds may differ or find no successful
start (inf). It must never fall below the certified 14.1734 of Proposition 4
by more than the search tolerance, which would contradict nothing proved but
would change the evidence reported in Section 8, so it is flagged.
Usage: python3 -I check_search.py NEW.json SHIPPED.json"""
import json
import sys

new, old = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
r_new, r_old = new["part2_rare_patch_limit_threshold_Rstar"], old["part2_rare_patch_limit_threshold_Rstar"]
if abs(r_new - r_old) > 1e-6 * r_old:
    sys.exit(f"MISMATCH R*: {r_new} vs {r_old}")
p1 = new["part1_best_contrast_found"]
print(f"R* matches ({r_new}); part1 best contrast on this platform: {p1} (shipped {old['part1_best_contrast_found']}, starts {new['part1_starts']})")
if p1 < 14.17:
    sys.exit("FLAG: search found a contrast below 14.17; Section 8 evidence would change")
