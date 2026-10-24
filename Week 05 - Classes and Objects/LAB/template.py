
class Record:
    def __init__(self, label, value, limit):
        """Store the record details."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Calculate the percentage."""
        return (self.value / self.limit) * 100

    def status(self):
        """Check the record status."""
        p = self.percent()

        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Load records from a file."""
    records = []
    file = open(path, "r")

    for line in file:
        data = line.strip().split(",")
        r = Record(data[0], float(data[1]), float(data[2]))
        records.append(r)

    file.close()
    return records


records = load_records("records_sample.txt")

count = 0

for record in records:
    print()
    print("=" * 34)
    print("  RECORD CHECK -", record.label)
    print("=" * 34)

    print("  Value:", record.value)
    print("  Limit:", record.limit)
    print("  Percentage:", record.percent())
    print("  Status:", record.status())

    print("=" * 34)

    if record.status() == "OVER LIMIT":
        count += 1

print()
print(count, "of", len(records), "were OVER LIMIT")
