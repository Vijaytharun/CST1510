"""
RECORD CHECK  -  my version
===========================

Name  :Vijaytharun
Lane  :  AI / Cyber / IT      (delete two)
Date  :9/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Clean and parse a raw survey record line into a dictionary of fields."""
    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)
    survey_name = survey_part.strip().lower()
    
    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
        
    return {
        "survey": survey_name,
        "rating": fields.get("rating", 0.0),
        "age": fields.get("age", 0.0)
    }


def status_of(rating):
    """Return status classification based on survey rating threshold."""
    if rating < 3.0:
        return "FLAGGED"
    elif rating <= 3.5:
        return "WARNING"
    else:
        return "OK"


with open("survey_raw.txt", "w") as f:
    f.write("  Survey_2026 , rating=4 , age=23 \n")
    f.write("SURVEY_2027,rating=2,age=30\n")
    f.write(" survey_2028 , rating=3 , age=22 \n")
    f.write("SURVEY_2029,rating=5,age=40\n")
    f.write("  survey_2030  ,  rating=1  ,  age=19  \n")

raw_records = []
with open("survey_raw.txt", "r") as f:
    for line in f:
        raw_records.append(line)

flagged_count = 0
total_records = len(raw_records)

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["rating"])
    
    if status == "FLAGGED":
        flagged_count += 1
        
    print(f"Survey: {record['survey']} | Rating: {record['rating']} | Age: {record['age']} | Status: {status}")

print(f"\nSummary: {flagged_count} of {total_records} records were flagged.")