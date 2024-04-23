from typing import List
from . import CLIENT
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionMessageParam,
)


def generate_answer(
    text: str, deployment_name="gpt-35-turbo", language="english"
) -> None | str:
    """
    Generate an answer from a given text using OpenAI's API.

    Parameters
    ----------
    text : str
        The text to generate the answer from.

    deployment_name : str, optional
        The name of the deployed model to use for the answer generation. The default is "gpt-35-turbo".

    language : str, optional
        The language to translate the answer to written in natural english language (no abbreviations).
        The default is "english".

    Returns
    -------
    str
        The generated answer.
    """

    system_message: str = (
        "You are a helpful chatbot that tries to answer questions to the best of your ability."
        "As your answers are used to generate speech, you should answer as short as possible."
        f"Make sure to translate your answer to {language}"
    )

    # TODO: Play with additional parameters like temperature, max_tokens, etc.

    messages: List[ChatCompletionMessageParam] = []

    # Add the system message to the messages list
    messages.append(
        ChatCompletionSystemMessageParam(content=system_message, role="system")
    )

    messages.append(ChatCompletionUserMessageParam(content=text, role="user"))

    response = CLIENT.chat.completions.create(model=deployment_name, messages=messages)

    return response.choices[0].message.content
