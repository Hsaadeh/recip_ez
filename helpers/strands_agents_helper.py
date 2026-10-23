from strands import Agent
from strands.models import BedrockModel
from app.settings import AWS_MODEL_ID, AWS_REGION
from .internal_agent_tools.default_tools import abilities
from .internal_agent_tools.recipe_tools import get_recipes



def create_agent(system_prompt: str, temperature: int, max_tokens: int) -> Agent:
    """Uses strands to configure a bedrock model and returns an instance of an Agent"""
    bedrock_model = BedrockModel(
        model_id=AWS_MODEL_ID,
        region_name=AWS_REGION,
        temperature=temperature,
        max_tokens=max_tokens,
        use_native_token_count=True,
    )

    agent = Agent(
        model=bedrock_model,
        system_prompt=system_prompt,
        callback_handler=None,
        tools=[abilities, get_recipes],
    )
    return agent
