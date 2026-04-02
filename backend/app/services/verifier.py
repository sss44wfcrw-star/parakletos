from z3 import Real, Solver, sat

PHI = 1.618033988749895
RESONANCE = 432.0

def verify_volume(volume_id: int, content_length: int) -> dict:
    solver = Solver()
    v = Real("volume_id")
    n = Real("content_length")

    solver.add(v == volume_id)
    solver.add(n == content_length)
    solver.add(v >= 1, v <= 200)
    solver.add(n > 0)

    is_valid = solver.check() == sat

    return {
        "valid": is_valid,
        "mode": "LAMINAR_FLOW" if is_valid else "REPAIR_REQUIRED",
        "phi": PHI,
        "resonance": RESONANCE,
    }
