from .clean_tool import CleanDataTool
from .clean_data_validator import CleanDataValidator
from .summarize_tools import Summarize
from .summarize_tool_validator import SummarizeValidator
from .write_article_tool import WriteArticle
from .write_article_validator import WriteArticleValidator
from .refiner_agent import RefinerAgent

class AgentManager:
    def __init__(self,max_retries=2,verbose=True):

        self.agent = {
        "summarize": Summarize(max_retries=max_retries, verbose=verbose),
        "write_article": WriteArticle(max_retries=max_retries, verbose=verbose),
        "clean_data": CleanDataTool(max_retries=max_retries, verbose=verbose),
        "summarize_validator": SummarizeValidator(max_retries=max_retries, verbose=verbose),
        "write_article_validator": WriteArticleValidator(max_retries=max_retries, verbose=verbose),
        "clean_data_validator": CleanDataValidator(max_retries=max_retries, verbose=verbose),
        "refiner": RefinerAgent(max_retries=max_retries, verbose=verbose)
        
        }

    def get_agent(self,agent_name):
        agent = self.agent.get(agent_name)
        if not agent:
            raise ValueError(f"Agent '{agent_name}' not found.")
        return agent