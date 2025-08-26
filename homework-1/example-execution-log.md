=== Example 1: Single Tool Call ===

--- Iteration 1 ---
LLM Response: role='assistant' content='' thinking=None images=None tool_name=None tool_calls=[ToolCall(function=Function(name='count_square', arguments={'input': 25})), ToolCall(function=Function(name='count_square', arguments={'input': 25}))]
Executing tool: count_square({'input': 25})
Tool result: 625
Executing tool: count_square({'input': 25})
Tool result: 625

--- Iteration 2 ---
LLM Response: role='assistant' content=" The value of 25^2 is 625. This means you've squared the number 25, which multiplies it by itself (25 * 25 = 625)." thinking=None images=None tool_name=None tool_calls=None

Final answer:  The value of 25^2 is 625. This means you've squared the number 25, which multiplies it by itself (25 * 25 = 625).

Result:  The value of 25^2 is 625. This means you've squared the number 25, which multiplies it by itself (25 * 25 = 625).
