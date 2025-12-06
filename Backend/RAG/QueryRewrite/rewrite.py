from LLM.factory import LLMProviderFactory
import re

client = LLMProviderFactory()


def normalizeQuery(query: str) -> str:
    query = query.lower().strip()
    query = re.sub(r'\s+', ' ', query)
    return query



async def rewriteQuery(query: str) -> str:
    normalizedQuery = normalizeQuery(query)
    response = await client.query_rewrite(normalizedQuery)
    return response


print(normalizeQuery("   What is the capital of France? sdjfsd"))