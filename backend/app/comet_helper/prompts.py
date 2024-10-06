SYSTEM_PROMPT_TEMPLATE = """
Vous êtes un coach d'orientation expérimenté, spécialisé dans l'accompagnement des étudiants. Soyez informatif, serviable et encourageant.
"""

USER_PROMPT_TEMPLATE = """Répondez à la question encadrée par %%% en basant votre réponse sur le contexte fourni entre ### sous format HTML et au maximum h4 headings:

%%% QUESTION

{question}

%%%

###

{context}

###

Réponse:"""

HYDE_PROMPT_TEMPLATE = """Ecris un passage qui serait susceptible de répondre à la question suivante.

Question: {QUESTION}

Passage:"""


def prompt_format(
    user_question: str, context: str, system_template: str, user_template: str
) -> tuple[str, str]:

    system_prompt = system_template
    user_prompt = user_template.format(question=user_question, context=context)

    return system_prompt, user_prompt
