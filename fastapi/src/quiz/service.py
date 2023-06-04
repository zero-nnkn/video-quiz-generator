from abc import abstractmethod

import openai
from bardapi import Bard


class QuizzPromptGenerator:
    @abstractmethod
    def generate_prompt():
        raise NotImplementedError


class MultipleChoicePromptGenerator(QuizzPromptGenerator):
    example = 'What is the capital of France?; A) Berlin; B) Rome; C) Paris (Correct); D) Amsterdam'

    @classmethod
    def generate_prompt(cls, num_quizzes, num_choices):
        require = (
            f'Please create a practice test with {num_quizzes} multiple-choice questions'
            + f'each with {num_choices} possible answers (mark the correct answers)'
            + 'about the following text.'
        )
        prompt = f'{require} in this form {cls.example}.'
        return prompt


def get_quiz_prompt_generator(type) -> QuizzPromptGenerator:
    """
    Factory: This function returns a quiz prompt generator based on the type specified.

    Args:
      type: The type of quiz prompt generator to create.

    Returns:
      a QuizzPromptGenerator object based on the type parameter passed to it.
    """
    quiz_prompt_generators = {
        'multiple_choice': MultipleChoicePromptGenerator,
    }
    return quiz_prompt_generators[type]


class LLMService:
    @abstractmethod
    def call_service(key, prompt):
        raise NotImplementedError


class OpenAIGPT(LLMService):
    @staticmethod
    def call_service(key, prompt):
        openai.api_key = key
        response = openai.Completion.create(
            engine='gpt-3.5-turbo',
            prompt=prompt,
            max_tokens=1000,
            temperature=0.8,
        )['choices'][0]['text']
        return response


class GoogleBard(LLMService):
    @staticmethod
    def call_service(key, prompt):
        bard = Bard(key)
        response = bard.get_answer(prompt)['content']
        return response


def get_llm_service(type) -> LLMService:
    """
    Factory: This function returns an instance of LLM service based on the type parameter passed to
    it.

    Args:
      type: The type of LLM service

    Returns:
      an instance of a LLM service class that use to call service.
    """
    llm_services = {
        'OpenAIGPT': OpenAIGPT,
        'GoogleBard': GoogleBard,
    }
    return llm_services[type]
