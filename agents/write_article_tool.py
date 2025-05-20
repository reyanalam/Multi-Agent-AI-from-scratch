



# These are tools

from .agent import AgentBase

class WriteArticle(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="WriteArticle",max_retries=max_retries,verbose=verbose)

    def execute(self, topic):
        
        system_message = "You are an expert academic writer"
        user_content = f"Write a research article on the following topic: \nTopic: {topic} \n\n"

        user_content+=f"Article:\n"

        messages = [
            {'role':'system','content':system_message},
            {'role':'user','content':user_content}
        ]


        article = self.call_openai(messages,max_tokens=1000)
        return article
