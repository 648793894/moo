# def checkio(data):
#     # data_list = list(data)
#     # flag_num = False
#     # flag_lower = False
#     # flag_upper = False
#     # flag_char = False
#     # if len(data_list) < 10:
#     #     return False
#     # else:
#     #     for i in data_list:
#     #         if i.isdigit():
#     #             flag_num = True
#     #
#     #         if i.isalpha():
#     #             if i == i.lower():
#     #                 flag_lower = True
#     #             if i == i.upper():
#     #                 flag_upper = True
#     #             flag_char = True
#     # #replace this for solution
#     # if flag_num and flag_lower and flag_upper and flag_char:
#     #     return True
#     # else:
#     #     return False
#     return not (data.isalpha() or  data.isupper() or  data.islower() or len(data)<10 or  data.isdigit())
# #Some hints
# #Just check all conditions
#
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio('A1213pokl') == False, "1st example"
#     assert checkio('bAse730onE4') == True, "2nd example"
#     assert checkio('asasasasasasasaas') == False, "3rd example"
#     assert checkio('QWERTYqwerty') == False, "4th example"
#     assert checkio('123456123456') == False, "5th example"
#     assert checkio('QwErTy911poqqqq') == True, "6th example"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# def count_words(text, words):
#     count = 0
#     text = text.lower()
#     import re
#     for i in words:
#         if re.search(i,text):
#             count +=1
#     return count
#
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
#     assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
#     assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
#                        {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")




def checkio(game_result):
    row=[]
    for result in game_result:
        row.append(result)
    if (row[0])[0] == (row[1])[0] and (row[0])[0]==(row[2])[0]:
        if (row[0])[0] !='.':
            return (row[0])[0]
    if (row[0])[1] == (row[1])[1] and (row[0])[1]==(row[2])[1]:
        if (row[0])[1] != '.':
            return (row[0])[1]
    if (row[0])[2] == (row[1])[2] and (row[0])[2]==(row[2])[2]:
        if (row[0])[2] !='.':
            return (row[0])[2]
    if (row[0])[0] == (row[0])[1] and (row[0])[0]==(row[0])[2]:
        if (row[0])[0] !='.':
            return (row[0])[0]
    if (row[1])[0] == (row[1])[1] and (row[1])[0]==(row[1])[2]:
        if (row[1])[0] !='.':
            return (row[1])[0]
    if (row[2])[0] == (row[2])[1] and (row[2])[0]==(row[2])[2]:
        if (row[2])[0] !='.':
            return (row[2])[0]
    if (row[0])[0] == (row[1])[1] and (row[0])[0]==(row[2])[2]:
        if (row[0])[0] !='.':
            return (row[0])[0]
    if (row[0])[2] == (row[1])[1] and (row[0])[2]==(row[2])[0]:
        if (row[0])[2] !='.':
            return (row[0])[2]
    return 'D'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


