def main():
    n = int(input().strip())  # Number of rows
    rows = []
    
    gender_map = {"female": 0, "man": 1}
    consumption_map = {"low": 1, "normal": 2, "high": 3}
    
    for _ in range(n):
        parts = input().strip().split(",")
        d = {
            "patient_id": parts[0],
            "gender": gender_map.get(parts[1].lower(), None),
            "age": int(parts[2]) if parts[2].isdigit() else None,
            "cancer": int(parts[3]) if parts[3].isdigit() else None,
            "consumption": consumption_map.get(parts[4].lower(), None)
        }
        if d["consumption"] is None:
            raise ValueError("Error: Missing consumption level in input!")
        rows.append(d)

    # Handling missing values by checking 4 neighbors
    for i in range(n):
        if rows[i]["consumption"] is None:
            idxs = [i - 2, i - 1, i + 1, i + 2]
            neighbors = [rows[j]["consumption"] for j in idxs if 0 <= j < n and rows[j]["consumption"] is not None]
            rows[i]["consumption"] = max(set(neighbors), key=neighbors.count) if neighbors else 2

    # Prediction function
    def predict(consumption, cancer):
        if consumption == 1 and cancer == 0:
            return "mahshare"
        elif consumption == 1 and cancer == 1:
            return "probably healthy"
        elif consumption == 2:
            return "sick"
        elif consumption == 3 and cancer == 0:
            return "severe illness"
        elif consumption == 3 and cancer == 1:
            return "khoda yani be khod A"
     

    for row in rows:
        row["prediction"] = predict(row["consumption"], row["cancer"])
        print(row["prediction"])

if __name__ == "__main__":
    main()