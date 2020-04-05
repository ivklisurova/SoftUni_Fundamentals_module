size_side = float(input())
sheets_paper = int(input())
covered_area_per_sheet = float(input())

SIDES = 6

area_box = size_side * size_side * SIDES

area_covered = 0

for i in range(1,sheets_paper+1):
    if i % 3 == 0:
        area = covered_area_per_sheet * 0.25
        area_covered += area
    else:
        area_covered += covered_area_per_sheet

percentage = (area_covered/area_box) * 100
print(f'You can cover {percentage:.2f}% of the box.')