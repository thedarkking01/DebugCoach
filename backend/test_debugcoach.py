from ai_service import generate_hint


code = """numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i + 1])
"""

error = "IndexError: list index out of range"

result = generate_hint(
    language="python",
    code=code,
    error=error,
    hint_level=1
)

print("\n==============================")
print("DEBUGCOACH HINT")
print("==============================")
print(result)