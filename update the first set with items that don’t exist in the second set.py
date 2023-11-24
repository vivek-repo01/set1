# Update the first set with items that don’t exist in the second set

set1 = {10, 20, 30}
set2 = {20, 40, 50}

# Expected output set1 {10, 30}

set1.difference_update(set2)

set1

