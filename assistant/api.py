import json
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helpers.strands_agents_helper import create_agent



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_agent_prompt(request):
    if request.method == "POST":
        data = request.data
        user_prompt = data.get("prompt", "")
        if len(user_prompt) > 0:
            agent_system_prompt = "You are a helpful agent. You assist users with managing recipes and shopping lists."
            agent = create_agent(
                system_prompt=agent_system_prompt,
                temperature=0.7,
                max_tokens=1000,
            )
            agent_message = agent(prompt=user_prompt).message
            data = {
                "message": json.dumps(agent_message)
            }
            return Response(data=data, status=status.HTTP_200_OK)
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
