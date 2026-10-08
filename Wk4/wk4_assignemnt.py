
# ---------------------------------------------------------------------------
# TASK 1 - Functional cleaning and fee calculation
# ---------------------------------------------------------------------------
def clean_transactions(amounts, min_threshold=10.0):

    return list(
        filter(
            lambda amount: amount > 0 and amount >= min_threshold,
            amounts,
        )
    )


def apply_service_fee(amounts, fee_rate=0.02):
    return list(
        map(
            lambda amount: round(amount * (1 - fee_rate), 2),
            amounts,
        )
    )

# ---------------------------------------------------------------------------
# TASK 2 - Recursive nested-total engine
# ---------------------------------------------------------------------------
def calculate_nested_total(data):
    # Base case 1: a single numeric value ends the recursion.
    if isinstance(data, (int, float)):
        return float(data)

    # Base case 2: an empty list contributes nothing.
    if isinstance(data, list):
        if len(data) == 0:
            return 0.0

        # Recursive step: resolve the head and the tail separately, then add.
        head = data[0]
        tail = data[1:]
        return calculate_nested_total(head) + calculate_nested_total(tail)

    # Anything that is not a number or a list is treated as no value.
    return 0.0


# ---------------------------------------------------------------------------
# DEMO - small self-contained audit run so the output can be captured
# ---------------------------------------------------------------------------
def main():
    """Run a demonstration batch through the complete audit pipeline."""
    print("=" * 62)
    print(" DIGITAL BANKING AUDIT TOOL - DEMONSTRATION RUN")
    print("=" * 62)
    # ---- Task 1 demo -----------------------------------------------------
    raw_batch = [120.0, -15.5, 0, 8.75, 250.0, 42.5, -3.2, 1000.0, 9.99, 75.0]
    print("\n[1] Raw batch received from the batch file:")
    print("   ", raw_batch)
    cleaned = clean_transactions(raw_batch)
    print("\n[2] Valid transactions after clean_transactions()")
    print("    (non-positive and below-threshold amounts removed):")
    print("   ", cleaned)
    processed = apply_service_fee(cleaned)
    print("\n[3] Amounts after apply_service_fee() - 2% fee deducted:")
    print("   ", processed)
    print("\n    Removed by the filter :",
          [amount for amount in raw_batch if amount not in cleaned])
    # ---- Task 2 demo -----------------------------------------------------
    nested_batch = [100, [50, 25], [[10, 5], 40]]
    print("\n" + "-" * 62)
    print("[4] Nested transaction batch (high-value operation):")
    print("   ", nested_batch)

    total = calculate_nested_total(nested_batch)
    print("\n[5] calculate_nested_total() traced every layer:")
    print("    100 + 50 + 25 + 10 + 5 + 40 =", total)
    # ---- Edge cases ------------------------------------------------------
    print("\n[6] Edge cases handled by the base cases:")
    print("    empty list []                  ->", calculate_nested_total([]))
    print("    single float 250.75            ->",
          calculate_nested_total(250.75))
    print("    deeply nested [[[1, 2], 3], 4] ->",
          calculate_nested_total([[[1, 2], 3], 4]))
    # ---- Combined audit total -------------------------------------------
    grand_total = calculate_nested_total(processed) + total
    print("\n" + "-" * 62)
    print("[7] Combined audited value of both batches:", grand_total)
    print("=" * 62)


if __name__ == "__main__":
    main()
