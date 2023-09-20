import requests
from audio import get_audio_file
from component import audio_source_component, quiz_config_component
from config import app_settings, settings

import streamlit as st

# Set page config
st.set_page_config(
    page_title='VideoQuizGenerator',
    page_icon=app_settings.PAGE_EMOJI,
    layout='wide',
)


# Column layout
transcript_col, quiz_col = st.columns(2)
transcript_col.title('💬 Transcript')
quiz_col.title('❓ Quiz')


# Uploade audio menu
with transcript_col:
    st.write('### 🔊 Audio')
    with st.expander(label='Add audio', expanded=True):
        audio_source, source_type = audio_source_component()
        add_audio = st.button(label='Add Audio')

        if add_audio and audio_source:
            audio = get_audio_file(audio_source=audio_source, source_type=source_type)
            st.session_state.audio = audio
            st.session_state.audio_play_time = 0
            st.experimental_rerun()

# Display audio
if 'audio' in st.session_state:
    with st.sidebar:
        st.audio(st.session_state.audio, start_time=st.session_state.audio_play_time)


# Transcribe menu
with st.sidebar.expander(label='💬 Transcribe', expanded=True):
    if st.button(label='Transcribe'):
        if 'audio' in st.session_state:
            # Post request to transcribe endpoint
            try:
                response = requests.post(
                    settings.TRANSCRIBE_ENDPOINT, files={'audio_file': st.session_state.audio}
                )
            except Exception:
                response = None
                st.error('Server is busy. Please try again later', icon='🚨')

            if response:
                if response.status_code != 200:
                    st.error(response.json()['detail'], icon='🚨')
                elif response.json()['message'] != 'success':
                    st.error(response.json()['message'], icon='🚨')
                else:
                    st.session_state.transcribe_results = response.json()['transcripts']


# Quiz generation menu
with st.sidebar.expander(label='❓ Quiz generation', expanded=True):
    service = st.radio(
        label='Service', options=app_settings.LLM_SERVICES.keys(), label_visibility='collapsed'
    )
    service_key = st.text_input(
        label=app_settings.LLM_SERVICES[service],
        type='password',
        placeholder='Enter your API/Cookie key',
    )
    quiz_type = st.selectbox(
        label='Quiz types',
        options=list(app_settings.DEFAULT_QUIZ_TYPES_CONFIG.keys()),
        index=list(app_settings.DEFAULT_QUIZ_TYPES_CONFIG.keys()).index(
            app_settings.DEFAULT_QUIZ_TYPE
        ),
    )
    quiz_config = quiz_config_component(type=quiz_type)

    if st.button(label='Generate'):
        if service_key:
            if 'transcript' in st.session_state:
                # Post request to quiz generation endpoint
                try:
                    response = requests.post(
                        f'{settings.QUIZ_GENERATION_ENDPOINT}'
                        + f'?content={st.session_state.transcript}&quiz_type={quiz_type}',
                        json={
                            'service_info': {
                                'service': service,
                                'service_key': service_key,
                            },
                            'quiz_config': quiz_config,
                        },
                    )
                except Exception:
                    response = None
                    st.error('Server is busy. Please try again later', icon='🚨')

                if response:
                    if response.status_code != 200:
                        st.error(response.json()['detail'], icon='🚨')
                    elif response.json()['message'] != 'success':
                        st.error(response.json()['message'], icon='🚨')
                    else:
                        st.session_state.quizzes = response.json()['generated_quiz']


# Results
# Transcript
with transcript_col:
    if 'transcribe_results' in st.session_state:
        info = st.session_state.transcribe_results['info']
        segments = st.session_state.transcribe_results['segments']

        # Display full transcript
        st.write('### 📝 Transcript')
        with st.expander(label='', expanded=True):
            st.subheader('Language: %s' % info['language'])
            text = ''.join([segment['text'] for segment in segments])
            st.session_state.transcript = text
            st.write(text)

        # Display transcript with timestamp
        st.write('### 🕒 Time stamp')
        with st.expander(label=''):
            for segment in segments:
                time_col, text_col = st.columns([2, 5])

                with time_col:
                    play_button = st.button(
                        label='▶️ {:.1f} - {:.1f}'.format(segment['start'], segment['end']),
                        use_container_width=True,
                    )
                    if play_button:
                        st.session_state.audio_play_time = int(segment['start'])
                        st.experimental_rerun()

                with text_col:
                    st.write('%s' % segment['text'])

# Quizzes
with quiz_col:
    st.write('### 📜 Result')
    # Display generated quizzes
    with st.expander(label='', expanded=True):
        if 'quizzes' in st.session_state:
            st.write(st.session_state.quizzes)
