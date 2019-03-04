print(
    "Correct answers : \n Идентификатор объекта – это целое число\n Идентификаторы всех объектов уникальны\n  [1, 2, 3, 4] 123")

objects = [1, 2, 2, 3, 3, 3, 4,4,4,5,6,7,8,8,8,8,9,10,11,11,11,12,12,13,14,15,16,16,16,1,2,3,4,5,17]
print(objects)

j = 0
count = 1
ans = len(objects)
for obj in objects:  # доступная переменная objects
    for i in range(count, len(objects)):
        print('obj', end=' ')
        print(obj, end=' ')
        print('obj[i] ', end=' ')
        print(objects[i], end=' ')

        if id(obj) == id(objects[i]):
            ans -= 1
            print(ans)
            break
        #     print('True',end=' ')
        #     print(obj,end=' ')
        #     print(objects[i],end=' ')
        print('')
        #     j = i+1
    count = count + 1
print('')
print(ans)
# print(len(objects))
# result = (len(objects)-ans)
# print(result)
