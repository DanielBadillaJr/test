

if __name__ == "__main__":

    patient = {
        "id": 101,
        "age": 65,
        "conditions": ["hypertension", "arrhythmia"]
    }

    print(f"patient: {patient}\n")
    print("Adding condition")
    patient["conditions"].append("Afib")
    print(f"patient: {patient}\n")
    print("Removing hypertension")
    patient["conditions"].remove("hypertension")
    print(f"patient: {patient}\n")
    for key, val in patient.items():
        print(f"key: {key}")
        print(f"value: {val}")