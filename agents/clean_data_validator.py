


# These are tools

from .agent import AgentBase

class CleanDataValidator(AgentBase):
    def __init__(self,max_retries=2,verbose=True):
        super().__init__(name="CleanDataValidator",max_retries=max_retries,verbose=verbose)

    def execute(self, text, cleaned_data):
        
        system_message = "You are an AI assistant that validates the sanitization of text by checking for the removal of Protected Health Information (PHI)."
        user_content = (
            "Given the original data and the sanitized data, verify that all PHI has been removed.\n"
            "List any remaining PHI in the sanitized data and rate the sanitization process on a scale of 1 to 5, where 5 indicates complete sanitization.\n\n"
            f"Original Data:\n{text}\n\n"
            f"Sanitized Data:\n{cleaned_data}\n\n"
            "Validation:"
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]

        validation = self.call_openai(messages,max_tokens=300)
        return validation
