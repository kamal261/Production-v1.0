from agent.agent import SEOAgent


agent = SEOAgent()

result = agent.audit(
    "https://example.com"
)

print(result)

agent.close()