RAW_EXAMPLE_USER = {
    "FILIERE 1": "DROIT",
    "FILIERE 2": "SC. POLITIQUES RI",
    "INTERNATIONAL/ANGLAIS": 0,
    "Maths": 0,
    "PC": 0,
    "SVT": 0,
    "NSI": 0,
    "HLP": 2,
    "LLCE": 0,
    "AMC": 0,
    "HGGSP": 1,
    "SES": 2,
    "ARTS PLASTIQUES": 0,
    "DROIT ET GRANDS ENJEUX": 3,
    "MATHS COMPLEMENTAIRES": 0,
    "MATHS EXPERTES": 0,
    "STMG": 0,
    ">> moyenne": 0,  # 0
    ">= moyenne": "X",  # 1
    "<= moyenne": 0,  # 2
    "<< moyenne": 0,  # 3
    "moyenne générale <10": 0,
    "moyenne générale entre 10 et 12": 0,
    "moyenne générale entre 12 et 14": 0,
    "moyenne générale entre 14 et 16": 1,  # should be 15
    "moyenne générale >16": 0,
    "moyenne de français <10": 0,
    "moyenne de français entre 10 et 12": 0,
    "moyenne de français entre 12 et 14": 0,
    "moyenne de français entre 14 et 16": 1,  # should be 15
    "moyenne de français >16": 0,
    "moyenne de français >18": 0,
}

CLEANED_EXAMPLE_USER = {
    "FILIERE 1": "DROIT",
    "FILIERE 2": "SC. POLITIQUES RI",
    "INTERNATIONAL/ANGLAIS": 0,
    "Maths": 0,
    "PC": 0,
    "SVT": 0,
    "NSI": 0,
    "HLP": 1,
    "LLCE": 0,
    "AMC": 0,
    "HGGSP": 1,
    "SES": 1,
    "ARTS PLASTIQUES": 0,
    "DROIT ET GRANDS ENJEUX": 1,
    "MATHS COMPLEMENTAIRES": 0,
    "MATHS EXPERTES": 0,
    "STMG": 0,
    ">> moyenne": 0,  # 0
    ">= moyenne": 1,  # 1
    "<= moyenne": 0,  # 2
    "<< moyenne": 0,  # 3
    "moyenne générale <10": 0,
    "moyenne générale entre 10 et 12": 0,
    "moyenne générale entre 12 et 14": 0,
    "moyenne générale entre 14 et 16": 1,  # should be 15
    "moyenne générale >16": 0,
    "moyenne de français <10": 0,
    "moyenne de français entre 10 et 12": 0,
    "moyenne de français entre 12 et 14": 0,
    "moyenne de français entre 14 et 16": 1,  # should be 15
    "moyenne de français >16": 0,
    "moyenne de français >18": 0,
}

PARSED_CLEANED_EXAMPLE_USER = {
    "FILIERE 1": "DROIT",
    "FILIERE 2": "SC. POLITIQUES RI",
    "INTERNATIONAL/ANGLAIS": 0,
    "Maths": 0,
    "PC": 0,
    "SVT": 0,
    "NSI": 0,
    "HLP": 1,
    "LLCE": 0,
    "AMC": 0,
    "HGGSP": 1,
    "SES": 1,
    "ARTS PLASTIQUES": 0,
    "DROIT ET GRANDS ENJEUX": 1,
    "MATHS COMPLEMENTAIRES": 0,
    "MATHS EXPERTES": 0,
    "STMG": 0,
    "moyenne": 1,
    "moyenne générale": 15,
    "moyenne de français": 15,
}

STREAMLIT_EXAMPLE_USER_INPUT = {
    "FILIERE 1": "DROIT",
    "FILIERE 2": "SC. POLITIQUES RI",
    "Selected Subjects": ["HLP", "HGGSP", "SES"],
    "moyenne générale": 15,
    "moyenne de français": 15,
}
