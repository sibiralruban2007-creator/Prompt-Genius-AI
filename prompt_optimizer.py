
def optimize_prompt(original_prompt, technique="Detailed"):
    original_prompt = original_prompt.strip()

    if not original_prompt:
        return "Please enter a prompt to optimize."

    if technique == "Zero-Shot":
        return f"""
Answer the following request directly and accurately.

User Request:
{original_prompt}

Instructions:
- Give a clear, relevant answer.
- Use simple language.
- Avoid unnecessary information.
"""

    elif technique == "One-Shot":
        return f"""
Follow the example below to understand the expected style.

Example:
Request: Explain Python.
Response: Python is a programming language used to build applications.

Now respond to this request in a similar clear style:
{original_prompt}
"""

    elif technique == "Few-Shot":
        return f"""
Follow these examples.

Example 1:
Request: Define AI.
Response: AI enables machines to perform tasks that usually require human intelligence.

Example 2:
Request: Define ML.
Response: Machine learning allows computers to learn patterns from data.

Now answer this request using a similar concise style:
{original_prompt}
"""

    elif technique == "Role-Based":
        return f"""
Act as a knowledgeable subject expert and helpful teacher.

Task:
{original_prompt}

Instructions:
- Explain accurately.
- Organize the response with headings or bullet points when useful.
- Use examples where appropriate.
- Keep the answer easy to understand.
"""

    else:
        return f"""
Improve the response to this request by following clear instructions.

Original Request:
{original_prompt}

Instructions:
1. Understand the main objective.
2. Provide a relevant, accurate answer.
3. Organize information logically.
4. Include examples when useful.
5. Use clear and simple language.
"""