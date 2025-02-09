def calculate_coverage():
    # Input the side of the box and calculate its area
    side = float(input())
    box_area = 6 * (side ** 2)

    # Input the number of sheets and initialize the covered area
    n_sheets = int(input())
    covered_area = 0

    # Process each sheet
    for i in range(1, n_sheets + 1):
        # Input the area of each sheet
        sheet_area = float(input())

        # Check conditions for sheet coverage reduction
        if i % 5 == 0:
            # Every fifth sheet is crumpled and unusable
            continue
        elif i % 3 == 0:
            # Every third sheet only covers 75% of its area
            covered_area += sheet_area * 0.75
        else:
            # Full area of other sheets
            covered_area += sheet_area

    # Determine if we have enough coverage
    if covered_area >= box_area:
        # Calculate unused paper percentage
        unused_percentage = ((covered_area - box_area) / covered_area) * 100
        print(f"You've covered the gift box!\n{unused_percentage:.2f}% wrap paper left.")
    else:
        # Calculate the uncovered box area percentage
        uncovered_percentage = ((box_area - covered_area) / box_area) * 100
        print(f"You are out of paper!\n{uncovered_percentage:.2f}% of the box is not covered.")


# Run the function to start the program
calculate_coverage()