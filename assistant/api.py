import json
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helpers.strands_agents_helper import create_agent
from django.http.response import StreamingHttpResponse


async def api_agent_prompt(request):
    """Endpoint to prompt the agent"""
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
                "message": "Invalid request"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = {
            "message": "This method is not allowed",
        }
        return Response(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
