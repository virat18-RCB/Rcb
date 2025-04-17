def is_balanced(s):
    stack=[]
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return "unbalanced"
            if (char==")" and stack[-1]!="(")or \
               (char=="}" and stack[-1]!="{")or \
               (char=="]" and stack[-1]!="["):
                return "unbalanced"
            stack.pop()
    if not stack:
        return "balanced"
    else:
        return "unbalanced"
a=input("enter")
print(is_balanced(a))
