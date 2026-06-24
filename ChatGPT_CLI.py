"""
1. Functionality: A simple CLI to interact with the ChatGPT API.
2. Data: Just the user prompt in the form of a string. JSON response from the API.
no need to store anything locally.
3. Operations: User Input, HTTP GET, Parse JSON, Print Response.
4. Flow: Get user input, fetch data, print response.
"""

from openai import OpenAI
client = OpenAI()

def get_input():
    return input("Enter a prompt: ")

def fetch_data(prompt):
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )
    return response

def print_response(response):
    print(response.output_text)

def main():
    while True:
        prompt = get_input()
        response = fetch_data(prompt)
        print_response(response)
        if input("Do you want to continue? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()


# I'm adding a comment here to test a commit and PR.
# another comment for testing