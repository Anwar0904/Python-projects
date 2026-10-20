from routing import route_message

# message = "there is an error in my code"
message = "my app is crashing"

result = route_message(message)

print(result)


# exercises

# 1. add crashing to the technical keywords,implemented above
# 2. Decide how mixed billing/technical messages should behave.
# Ans:If a message contain billign and technical keywords then the funciton defined first will be returned means that in our case the billing will be returned cuz its statemnt is declared first and the program wil stop there
# 3. add a sales category : ok, implemented in router.py


# 4.Ans: this is a rule based system not an ML in ML the model learn patterns and design rules by itsef not follow the rules. but in this case our program work on defined rules if this than this vice versa
