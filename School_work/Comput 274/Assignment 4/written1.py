def push_with_priority(stack, priority, element):

    temp_stack = []

    if(len(stack) != 0):
        while stack:
            if len(stack) == 1: #special case, if length of stack is 1 then simply append the stack to the temp_stack
                temp_stack.append(stack[0])
                stack.pop(0)

            else:
                if(stack[0][0] >= stack[1][0]): #comparison between priorities in stack (between first and second)
                    temp_stack.append(stack[0])
                    stack.pop(0) # pop stack after adding element ot temp_stack
                else:
                    temp_stack.append(stack[1])
                    stack.pop(1)

        count = 0
        for i in range(len(temp_stack)): #since the temp stack is already sorted, simply find how many element is priority ahead
            if priority <= temp_stack[i][0]:
                count += 1

        if count <= len(temp_stack): #insert priority element
            temp_stack.insert(count, (priority, element))
        else:
            temp_stack.append((priority, element))

    else: #base case, when stack is empty (just append element)
        stack.append((priority, element))

    for n in temp_stack:
        stack.append(n)


stack = []
push_with_priority(stack, 3, "A")
push_with_priority(stack, 1, "B")
push_with_priority(stack, 2, "C")
print(stack)