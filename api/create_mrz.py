from calculate_check_digit import calculate_check_digit

def create_mrz(fields):
    passport_type = fields['passport_type']
    issuing_country = fields['issuing_country']
    surname = fields['surname']
    given_names = fields['given_names']
    passport_number = fields['passport_number']
    nationality = fields['nationality']
    dob = fields['dob']
    sex = fields['sex']
    expiry_date = fields['expiry_date']
    personal_number = fields['personal_number']
    
    # Prepare name field with fillers
    name_field = f"{surname}<<{given_names}".upper()
    name_field = re.sub(r'[^A-Z<]', '', name_field)[:39]
    name_field += '<' * (39 - len(name_field))
    
    # Prepare passport number field with check digit
    passport_number_field = re.sub(r'[^A-Z0-9]', '', passport_number).upper()
    passport_number_field += '<' * (9 - len(passport_number_field))
    passport_number_check = calculate_check_digit(passport_number_field)
    
    # Prepare dob field with check digit
    dob_check = calculate_check_digit(dob)
    
    # Prepare expiry date field with check digit
    expiry_date_check = calculate_check_digit(expiry_date)
    
    # Prepare personal number field with check digit
    personal_number_field = re.sub(r'[^A-Z0-9<]', '', personal_number).upper()
    personal_number_field += '<' * (14 - len(personal_number_field))
    personal_number_check = calculate_check_digit(personal_number_field)
    
    # Prepare composite check digit
    composite_data = passport_number_field + passport_number_check + dob + dob_check + expiry_date + expiry_date_check + personal_number_field
    composite_check = calculate_check_digit(composite_data)
    
    mrz = (
        f"P<{issuing_country}{name_field}\n"
        f"{passport_number_field}{passport_number_check}{nationality}{dob}{dob_check}{sex}{expiry_date}{expiry_date_check}{personal_number_field}{personal_number_check}{composite_check}"
    )
    return mrz
