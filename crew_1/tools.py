import os
from exa_py import Exa
from langchain.agents import tool

class ExaSearchToolset():
    @tool
    def search(self, query: str):
        """Search for a webpage based on the query."""
        return ExaSearchToolset._exa().search(f"{query}", use_autoprompt=True, num_results=3)

    @tool
    def find_similar(self,url: str):
        """Search for webpages similar to the given URL.
        The url passed in should be a URL returned from 'search'.
        """
        return ExaSearchToolset._exa().find_similar(url, num_results=3)

    @tool
    def get_contents(self, ids: str):
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list of ids returned from 'search'.
        """
        ids=eval(ids)

        contents = str(ExaSearchToolset._exa().get_contents(ids))
        contents = contents.split("URL:")
        contents = [contents[:1000] for content in contents]
        return "\n\n".join(contents)

    def tools(self):
        return [
            ExaSearchToolset.search,
            ExaSearchToolset.find_similar,
            ExaSearchToolset.get_contents,
        ]
    def _exa(self):
        return Exa(api_key=os.environ.get("EXA_API_KEY"))
