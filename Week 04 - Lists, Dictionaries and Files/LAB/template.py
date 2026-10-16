"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"

def check_record(value,limit):
    difference = limit-value 
    percent = (value/limit)*100
    status = status_of(percent)
    return difference, percent, status 

def print_report(label,value,limit,difference,percent,status):
    print()
    print("="*34)
    print(f"RECORD CHECK - {label}")
    print(f"difference : {difference:>.2f}")
    print(f"percent : {percent:>.2f}")
    print(f"status : {status:>.2f}")
    print()



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    records = []
    with open (path,"r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                    records.append({
                        "label": parts[0],
                        "value": float(parts[1]),
                        "limit": float(parts[2])
                    })
                    return records


with open("datasets_input.txt", "w") as f:
    f.write("survey_alpha,87.0,100.0\n")
    f.write("survey_beta,120.0,100.0\n")
    f.write("survey_gamma,95.0,100.0\n")

records = load_records("datasets_input.txt")

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

over_limit_count = 0
results_lines = []

for record in records:
    label = record["Label"]
    value = record["Value"]
    limit = record["Limit"]

    difference, percent, status = check_record(value,limit)
    print_report(label,value,limit,difference,percent,status)

    if status == "OVER LIMIT":
        over_limit_count += 1

    results_lines.append (f"{label},{status}\n")

with open("results.txt", "w") as f:
    f.writelines(results_lines)

print(f"Session finished. Total records OVER LIMIT: {over_limit_count}")



# ==========================================================================
# 4. Before you finish:
# 
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
