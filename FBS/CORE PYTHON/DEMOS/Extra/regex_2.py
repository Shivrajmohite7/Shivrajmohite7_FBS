import re

text = "Contact us at support@example.com or sales@company.org by 2026-11-13."

# 1. Find all matches (returns a list of strings)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Emails:", emails)
# Output: ['support@example.com', 'sales@company.org']

# 2. Search for the first match (returns a Match object or None)
date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)
if date_match:
    print("First date found:", date_match.group())
# Output: 2026-11-13

# 3. Replace matched patterns
masked_text = re.sub(r"\d{4}-\d{2}-\d{2}", "[DATE]", text)
print("Masked:", masked_text)
# Output: Contact us at support@example.com or sales@company.org by [DATE].

# 4. Split a string by a pattern
parts = re.split(r"\s+or\s+", "apples or oranges or bananas")
print("Split:", parts)
# Output: ['apples', 'oranges', 'bananas']
