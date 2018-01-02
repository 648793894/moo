#! -*-coding:utf-8 -*-
# 第一步都换成小写
# 第二步计算每个字母对应出现的个数
# 第三步取出最大的values
# 循环找出相等的key存到list中排序。

def checkio(text):
    text = text.lower()
    text_l = list(text)
    map={}
    count_times = []
    for i in text_l:
        if i.isalpha():
            if i not in map.keys():
                map[i] = text_l.count(i)

    m = max(map.values())
    for (key,value) in map.items():
         if value == m:
             count_times.append(key)
    count_times.sort()

    return count_times[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")