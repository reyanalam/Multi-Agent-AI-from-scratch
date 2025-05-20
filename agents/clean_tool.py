

# These are tools

from .agent import AgentBase

class CleanDataTool(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="CleanDataTool",max_retries=max_retries,verbose=verbose)

    def execute(self, text):
        
        messages = [
            {'role':'system','content':"You are a AI assistant that cleans data by removing protected information."},
            {'role':'user','content':(
                "Remove all protected information from the data: \n\n"
                f"{text}\n\nCleaned Data: "
            )}
        ]

        clean_data = self.call_openai(messages,max_tokens=300)
        return clean_data
