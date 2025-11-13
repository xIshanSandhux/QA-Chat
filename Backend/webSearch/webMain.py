# this will be the entry point for the web search queries
from ddgs import DDGS

results = DDGS().text("Where is canada located", max_results=5)
print(results)