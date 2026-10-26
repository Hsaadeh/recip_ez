import json
from rest_framework import status
from helpers.strands_agents_helper import create_agent
from django.http.response import StreamingHttpResponse, JsonResponse


async def api_agent_prompt(request):
    """Endpoint to prompt the agent"""
    user = await request.auser()
    if user.is_authenticated != True:
        data = {
            "message": "Unauthorized"
        }
        return JsonResponse(data=data, status=status.HTTP_401_UNAUTHORIZED)

    async def generate_stream_response(prompt):
        """Generates the asynchronous stream response for the agent"""
        agent_system_prompt = "You are a helpful agent. You assist users with managing recipes and shopping lists."
        agent = create_agent(
            system_prompt=agent_system_prompt,
            temperature=0.7,
            max_tokens=1000,
        )
        try:
            async for event in agent.stream_async(prompt=user_prompt):
                if "data" in event:
                    yield event["data"]
        except Exception as e:
            yield f"Error: {str(e)}"

    if request.method == "POST":
        data = json.loads(request.body)
        user_prompt = data.get("prompt", "")
        if len(user_prompt) > 0:
            response = StreamingHttpResponse(generate_stream_response(user_prompt), status=status.HTTP_200_OK, content_type="text/plain")
            return response
        else:
            data = {
                "message": "Bad request, message is empty"
            }
            return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = {
            "message": "This method is not allowed",
        }
        return JsonResponse(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
