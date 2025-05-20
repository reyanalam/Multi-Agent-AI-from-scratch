


# These are tools

from .agent import AgentBase

class SummarizeValidator(AgentBase):
    def __init__(self,max_retries=2,verbose=True):
        super().__init__(name="SummarizeValidator",max_retries=max_retries,verbose=verbose)

    def execute(self, text, summary):

        system_message = "You are an AI assistant that validates summaries of texts."
        user_content = (
            "Given the original text and its summary, assess whether the summary accurately and concisely captures the key points of the original text.\n"
            "Provide a brief analysis and rate the summary on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Original Text:\n{text}\n\n"
            f"Summary:\n{summary}\n\n"
            "Validation:"
        )
        
        messages = [
            {'role':'system','content':system_message},
            {'role':'user','content':user_content}
        ]

        validation = self.call_openai(messages,max_tokens=300)
        return validation
