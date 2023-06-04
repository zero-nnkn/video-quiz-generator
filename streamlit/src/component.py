from config import app_settings

import streamlit as st


def quiz_config_component(type):
    """
    This function setup the streamlit UI component for quiz configuration based on quiz type

    Args:
      type: The type of quiz configuration component.

    Returns:
      A configuration dictionary.
    configuration.
    """
    if type == 'multiple_choice':
        num_quizzes = st.number_input(
            label='Number of quizzs', min_value=1, max_value=5, value=1, step=1
        )
        num_choices = st.number_input(
            label='Number of choices', min_value=2, max_value=5, value=4, step=1
        )
        return {'num_quizzes': num_quizzes, 'num_choices': num_choices}
    # elif type == 'true_false':
    #     num_quizzes = st.number_input(
    #         label='Number of quizzs', min_value=1, max_value=5, value=1, step=1
    #     )
    #     return {'num_quizzes': num_quizzes}
    # elif type == 'fill_the_blank':
    #     num_quizzes = st.number_input(
    #         label='Number of quizzs', min_value=1, max_value=5, value=1, step=1
    #     )
    #     num_blanks = st.number_input(
    #         label='Number of blanks', min_value=1, max_value=3, value=1, step=1
    #     )
    #     return {'num_quizzes': num_quizzes, 'num_blanks': num_blanks}


def audio_source_component():
    source_type = st.radio(label='Source type', options=app_settings.SOURCE_TYPE)
    if source_type == 'Youtube':
        source = st.text_input(label='YouTube link')
    elif source_type == 'Upload':
        source = st.file_uploader('Upload file', type=app_settings.AUDIO_EXTENSION)

    return source, source_type
