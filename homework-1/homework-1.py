import json
from ollama import chat, ChatResponse
from typing import List, Dict, Any

# Function Implementations
def count_square(input: int):
    """Counts square of a number"""
    return input*input

# Define tools for Ollama (mixed format as shown in original)
tools = [
    count_square,  # Direct function reference
]

# Available functions for calling
available_functions = {
    "count_square": count_square,
}

class OllamaReactAgent:
    """A ReAct (Reason and Act) agent using Ollama."""
    
    def __init__(self, model: str = "mistral:7b-instruct-v0.3-q5_0"):
        self.model = model
        self.max_iterations = 10
        
    def run(self, messages: List[Dict[str, Any]]) -> str:
        """
        Run the ReAct loop until we get a final answer.
        """
        iteration = 0
        
        while iteration < self.max_iterations:
            iteration += 1
            print(f"\n--- Iteration {iteration} ---")
            
            # Call the LLM
            response: ChatResponse = chat(
                self.model,
                messages=messages,
                tools=tools,
            )
            
            print(f"LLM Response: {response.message}")
            
            # Check if there are tool calls
            if response.message.tool_calls:
                # Add the assistant's message to history
                messages.append(response.message)
                
                # Process ALL tool calls (there can be more than one!)
                for tool_call in response.message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = tool_call.function.arguments
                    
                    print(f"Executing tool: {function_name}({function_args})")
                    
                    # Call the function
                    function_to_call = available_functions[function_name]
                    function_response = function_to_call(**function_args)
                    
                    print(f"Tool result: {function_response}")
                    
                    # Add tool response to messages
                    messages.append({
                        "role": "tool",
                        "name": function_name,
                        "content": json.dumps(function_response),
                    })
                
                # Continue the loop to get the next response
                continue
                
            else:
                # No tool calls - we have our final answer
                final_content = response.message.content
                
                # Add the final assistant message to history
                messages.append(response.message)
                
                print(f"\nFinal answer: {final_content}")
                return final_content
        
        # If we hit max iterations, return an error
        return "Error: Maximum iterations reached without getting a final answer."


def main():
    # Create a ReAct agent
    agent = OllamaReactAgent()
    
    # Example 1: Simple query (single tool call)
    print("=== Example 1: Single Tool Call ===")
    messages1 = [
        {"role": "user", "content": "What is the value of 25^2?"}
    ]
    
    result1 = agent.run(messages1.copy())
    print(f"\nResult: {result1}")
    


if __name__ == "__main__":
    main()
