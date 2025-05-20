

# These are tools

from .agent import AgentBase

class Summarize(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="Summarize",max_retries=max_retries,verbose=verbose)

    def execute(self, text):
        
        messages = [
            {'role':'system','content':"You are a AI assistant that summarizes texts."},
            {'role':'user','content':(
                "Please provide a consice summaray of the following texts: \n\n"
                f"{text}\n\nSummary: "
            )}
        ]

        summary = self.call_openai(messages,max_tokens=300)
        return summary
