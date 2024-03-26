from . import CLIENT


def generate_answer(text: str, deployment_name="gpt-35-turbo") -> None | str:
    """
    Generate an answer from a given text using OpenAI's API.

    Parameters
    ----------
    text : str
        The text to generate the answer from.

    deployment_name : str, optional
        The name of the deployed model to use for the answer generation. The default is "gpt-35-turbo".

    Returns
    -------
    str
        The generated answer.
    """

    # TODO: Play with additional parameters like temperature, max_tokens, etc.

    response = CLIENT.chat.completions.create(
        model=deployment_name,
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
    )

    return response.choices[0].message.content
