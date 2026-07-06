from agent.agent import SEOAgent


def test_agent():

    agent = SEOAgent()

    result = agent.audit("https://pooyamachine.com")

    assert "execution" in result