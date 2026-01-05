import logging
from fastapi import APIRouter, Request, Response, HTTPException,Path
from typing import Optional,Annotated
from schemas.sector_schemas import SectorEnum
from core.session import get_or_create_session, SESSION_EXPIRY
from core.rate_limiter import is_rate_limited,is_ip_rate_limited
from services.trade_llm import chat_with_openai
from schemas.sector_schemas import SectorRequest
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("API-Routes")

router = APIRouter()

@router.get("/trade/analyze/{sector}")
async def sectore_analyze(sector : SectorEnum,request:Request,response:Response
):
    try:
        # STEP 1: guest auth Authentication with session id with rate limiting
        session_id = request.cookies.get("session_id")
        session_id = get_or_create_session(session_id)

        if is_rate_limited(session_id):
            logger.warning(f"Rate limit exceeded for session: {session_id}")
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Try again later."
            )
        logger.info(f"Session ID: {session_id} for sector analysis: {sector}")
        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=True,
            max_age=SESSION_EXPIRY
        )

        # STEP 2 : create LLM prompt for send llm
        chat_with_openai(sector.value) # This function call LLM and create md file report
        logger.info(f"LLM response received for sector with MD file: {sector}")
        file_name = f'Trade_report_{sector.value}.md'

        return {"message":"File created successfully",'file_name':file_name}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )