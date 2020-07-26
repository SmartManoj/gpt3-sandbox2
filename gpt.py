"""Creates the Example and GPT classes for a user to interface with the OpenAI API."""

import openai


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

class Example():
    """Stores an input, output pair and formats it to prime the model."""

    def __init__(self, inp, out):
        self.input = inp
        self.output = out

    def get_input(self):
        """Returns the input of the example."""
        return self.input

    def get_output(self):
        """Returns the intended output of the example."""
        return self.output

    def format(self):
        """Formats the input, output pair."""
        return f"input: {self.input}\noutput: {self.output}\n"


class GPT:
    """The main class for a user to interface with the OpenAI API.
    A user can add examples and set parameters of the API request."""

    def __init__(self, engine='davinci',
                 temperature=0.5,
                 max_tokens=100,
                 context=''):
        self.examples = []
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.prompt = context +'\n'

    def add_examples(self, ex):
        """Adds example to the prompt"""
        for i,j in ex.items():
        	self.examples.append(Example(i,j).format())
        self.prompt= '\n'.join(self.examples) + '\n'

 

    def get_engine(self):
        """Returns the engine specified for the API."""
        return self.engine

    def get_temperature(self):
        """Returns the temperature specified for the API."""
        return self.temperature

    def get_max_tokens(self):
        """Returns the max tokens specified for the API."""
        return self.max_tokens

    def craft_query(self, prompt):
        """Creates the query for the API request."""
        return self.prompt + "input: " + prompt + "\n"

    def submit_request(self, prompt):
        """Calls the OpenAI API with the specified parameters."""
        response = openai.Completion.create(engine=self.get_engine(),
                                            prompt=self.craft_query(prompt),
                                            max_tokens=self.get_max_tokens(),
                                            temperature=self.get_temperature(),
                                            top_p=1,
                                            n=1,
                                            stream=False,
                                            stop="\ninput:")
        return response

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        try:
	        response = self.submit_request(prompt)
	        output = response['choices'][0]['text']
	        self.prompt +=f"\noutput: {output}\n"
	        return output
        except Exception as e:
        	return 'Error' + response
        
