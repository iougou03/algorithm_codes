formula = input()

idx = 0
bracket_close = True
num_queue = [] ; num = ""

while(idx < len(formula)):
    if formula[idx] == "-":
        num_queue.append(str(int(num)))
        num = ""
        if not bracket_close: 
            num_queue.append(")")
            num_queue.append(formula[idx])
            num_queue.append("(")
        else: 
            num_queue.append(formula[idx])
            num_queue.append("(")
        bracket_close = False
    elif formula[idx] == "+":
        num_queue.append(str(int(num)))
        num_queue.append(formula[idx])
        num = ""
    else: num += formula[idx]

    idx += 1

if num: num_queue.append(str(int(num)))
if not bracket_close: num_queue.append(")")

num_queue = "".join(num_queue)
print(eval(num_queue))