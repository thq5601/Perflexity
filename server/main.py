import asyncio
from fastapi import FastAPI, WebSocket

from pydantic_models.chat_body import ChatBody
from services.gemini_service import GeminiService
from services.sort_source_service import SortSourceService
from services.search_service import SearchService

app = FastAPI()

# check if the server is running
# @app.get("/")
# def hello_world():
#     return "Hello World"

search_service = SearchService()
sort_source_service = SortSourceService()
gemini_service = GeminiService()


#chat websocket
@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        await asyncio.sleep(0.1)
        data = await websocket.receive_json()
        query = data.get("query")       
        search_results = search_service.web_search(query)       
        sorted_results = sort_source_service.sort_sources(query, search_results)
        await asyncio.sleep(0.1)
        await websocket.send_json({
            "type": "search_result", 
            "data": sorted_results
            })   
        for chunk in gemini_service.generate_response(query, sorted_results):
            await asyncio.sleep(0.1)
            await websocket.send_json({
                "type": "content", 
                "data": chunk
                })

    except:
        print("Error occured")
        
    finally:
        await websocket.close()

#chat
@app.post("/chat")
def chat_endpoint(body: ChatBody):
    # Step 1: search the web and fint appropriate sources
    search_results = search_service.web_search(body.query)
    # Step 2: sort the sources
    sorted_results = sort_source_service.sort_sources(body.query, search_results)
    # Step 3: generate the response using LLM
    response = gemini_service.generate_response(body.query, sorted_results)
    
    return response
