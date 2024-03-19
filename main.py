from anthropic import Anthropic
from anthropic.types import MessageParam

client = Anthropic(api_key="api-key-here")


def estimate_tokens(prompt):
    count = client.count_tokens(prompt)
    return count


def submit_prompt(prompt, system_prompt):
    with client.messages.stream(
            model='claude-2.1',
            system=system_prompt,
            max_tokens=1024,
            messages=[
                MessageParam(role="user", content=prompt)
            ]
    ) as stream:
        try:
            for text in stream.text_stream:
                print(text, end="", flush=True)
        except Exception as e:
            print(e)
            raise e


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    system_prompt = """You are a customer service agent tasked with classifying emails by type. Please output your 
    answer and then justify your classification. The classification categories are: (A) Pre-sale question (B) Broken 
    or defective item (C) Billing question (D) Other, please"""
    print(f"Tokens for this request: {estimate_tokens(prompt)}")
    submit_prompt(prompt, system_prompt=system_prompt)
