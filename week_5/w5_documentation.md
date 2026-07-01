# Defining the problem
### Cafe sells:
| Item     | Price   |
| -------- | ------- |
| Coffee   | RM8.50  |
| Tea      | RM6.00  |
| Sandwich | RM12.00 |

### The cashier enters:
- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity

### The program should calculate:
Total =
(coffee × 8.50)
+
(tea × 6.00)
+
(sandwich × 12.00)
Then print a receipt.

# Split the work
Instead of writing everything in one file:
###utils.py###

Contains functions only.

Example:
calculate_total() and print_receipt()

No user input here.

### main.py

This is where the program starts.

It should;
Ask user for inputs.
Call functions from utils.py.
Display the result.

