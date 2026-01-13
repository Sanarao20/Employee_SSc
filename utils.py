from datetime import datetime


def get_designation(years):
    if years < 3:
        return "System Engineer"
    elif 3 <= years <= 5:
        return "Data Engineer"
    elif 5 < years <= 10:
        return "Senior Data Engineer"
    else:
        return "Lead"


def normalize_employee_data(emp):
    # Handle missing data (Test Case 5)
    required_fields = ["first_name", "last_name", "email", "phone",
                       "gender", "age", "job_title",
                       "years_of_experience", "salary", "department"]

    for field in required_fields:
        if field not in emp or emp[field] is None:
            raise ValueError(f"Missing field: {field}")

    phone = emp["phone"]
    if "x" in str(phone):
        phone = "Invalid Number"
    else:
        phone = int(phone)

    years = int(emp["years_of_experience"])

    return {
        "full_name": f"{emp['first_name']} {emp['last_name']}",
        "email": str(emp["email"]),
        "phone": phone,
        "gender": str(emp["gender"]),
        "age": int(emp["age"]),
        "job_title": str(emp["job_title"]),
        "years_of_experience": years,
        "designation": get_designation(years),
        "salary": int(emp["salary"]),
        "department": str(emp["department"])
    }


def format_date(date_str):
    if not date_str:
        return None
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
