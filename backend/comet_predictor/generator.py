from backend.comet_predictor.generator_utils import (
    prepare_csv,
    prepare_profile_dictionnary,
)


def can_apply(student_dict, df):

    # List to store applicable formations
    applicable_formations = []

    # Metadata columns to exclude from requirement comparison
    metadata_columns = [
        "Sélectivité",
        "Intitulé de la formation",
        "Université/Ecole",
        "LIEU",
    ]

    for index, row in df.iterrows():
        can_apply = True

        for requirement_type, student_row in student_dict.items():
            if requirement_type in metadata_columns:
                continue

            student_value = student_row.values[0]
            requirement_value = row[requirement_type]

            if isinstance(student_value, (int, float)) and isinstance(
                requirement_value, (int, float)
            ):
                if student_value < requirement_value:
                    can_apply = False
                    break

            if isinstance(student_value, (str)) and isinstance(
                requirement_value, (str)
            ):
                if student_value != requirement_value:
                    can_apply = False
                    break

        # If the student qualifies for this formation, add it to the list
        if can_apply:
            formation_info = f"{row['Intitulé de la formation']} - {row['Université/Ecole']} ({row['LIEU']})"
            applicable_formations.append(formation_info)

    return applicable_formations


if __name__ == "__main__":

    requirements = prepare_csv()
    profiles = prepare_profile_dictionnary()

    possible_wish_list = can_apply(profiles, requirements)

    for possible_wish in possible_wish_list:
        print("\n", possible_wish)
