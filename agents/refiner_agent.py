


# These are tools

from .agent import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic):
        messages = [
            {
                'role':'system',
                'content':[
                    {'type':'text',
                    'text':'You are an expert editor who refines and enhances articles for clarity, choerance and acedemic quality.'}
                ]
            },
            {
                'role':'user',
                'content':[
                    {
                        
                        'type': 'text',
                        'text':("Please refine the following article to improve its language, coherence, and overall quantity:\n\n"
                                f"{topic}\n\nRefinedArticle:")
                
                    }
                ]
            }
        ]

        refiner = self.call_openai(messages, temperature=0.5, max_tokens=1000)
        return refiner
