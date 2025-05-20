



# These are tools

from .agent import AgentBase

class WriteArticleValidator(AgentBase):
    def __init__(self,max_retries=2,verbose=True):
        super().__init__(name="WriteArticleValidator",max_retries=max_retries,verbose=verbose)

    def execute(self, topic, article):
        
        system_message = "You are an expert ai assistant that validates articles."
        user_content = (
            'Given a topic and an article, asses wheather the article comprehensively covers the topic, follows a logical structure, and maintain academic standard.\n'
            'Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality.\n\n'
            f'Topic:{topic}\n\n'
            f'Article:\n{article}\n\n'
            'Validation:'
        )

        messages = [
            {'role':'system','content':system_message},
            {'role':'user','content':user_content}
        ]


        validation = self.call_openai(messages,max_tokens=500)
        return validation
