correct_password = "mohamed"
blocklist = ("lecture", "lesson", "lesson1", "lesson2", "lesson3", "lesson4", "lesson5", "lesson6", "lesson7")
promo_codes = ("new_buyer", "second_purchase")
threshold_text = 450
cart_total = 200

access_issues = 0
financial_issues = 0
promo_issues = 0
security_issues = 0

# check if the password is correct
code = input("give me the passwd: ")
if code != correct_password:
    print("access_denied")
    access_issues = access_issues + 1
    exit()
else:
    print("access_granted")

# check if the account is in the blocklist
account = input("give me the account mail: ")
if account in blocklist:
    print("access_denied")
    access_issues = access_issues + 1
    exit()
else:
    print("access_granted")

# check if the threshold text is valid
threshold_text = int(input("give me the threshold text: "))
if threshold_text > 0 and threshold_text < 450:
    print("perfect")
else:
    print("number is not valid must be greater than 0")
    financial_issues = financial_issues + 1

# check if the cart total is valid
cart_total = float(input("number of items: "))
if cart_total > 0 and cart_total < 200:
    print("number is valid")
else:
    print("number is not valid must be greater than 0")
    financial_issues = financial_issues + 1

# check if the promo code is valid
promo_code = input("give me the promo code: ")
if promo_code in promo_codes:
    print("promo code is valid, discount applied")
else:
    print("promo code is not valid")
    promo_issues = promo_issues + 1 


code_report = {
    "access_issues": access_issues,
    "financial_issues": financial_issues,
    "promo_issues": promo_issues,
    "security_issues": security_issues
}
print ("access issues: ")
print(code_report["access_issues"])

print("financial issues: ")
print(code_report["financial_issues"])

print("promo_issues : " )
print(code_report["promo_issues"])

print("security_issues : " )
print(code_report["security_issues"])
