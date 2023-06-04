from fastapi.responses import JSONResponse

from fastapi import APIRouter

from .schemas import ServiceInfo
from .service import get_llm_service, get_quiz_prompt_generator
from .utils import strip_response

router = APIRouter()


@router.post('/quizzes')
def generate_quizzes(
    content: str, service_info: ServiceInfo, quiz_type: str, quiz_config: dict
) -> JSONResponse:
    """
    The function call LLM service and return the generated quiz.
    """
    llm_service = get_llm_service(service_info.service)
    quiz_prompt_generator = get_quiz_prompt_generator(quiz_type)

    try:
        prompt = quiz_prompt_generator.generate_prompt(**quiz_config)
    except Exception:
        return JSONResponse(content={'message': 'prompt generation error'})
    prompt = f'{prompt}\n{content}'

    try:
        response = llm_service.call_service(service_info.service_key, prompt)
    except Exception:
        return JSONResponse(content={'message': 'LLM service call error'})

    response = strip_response(response)

    return JSONResponse(
        content={
            'message': 'success',
            'generated_quiz': response,
        }
    )
