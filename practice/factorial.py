
def factor(num):
    results = [1]
    max_num = 10000

    for current_num in range(2, num + 1):
        remaing = 0

        for index in range(0, len(results)):
            each_num = results[index]
            tmp_result = each_num * current_num + remaing
            results[index] = tmp_result % max_num
            remaing = tmp_result / max_num

        if remaing > 0:
            results.append(remaing)

    results.reverse()
    result_str = "%s" % results[0]
    for each_num in results[1:]:
        result_str += "%04d" % each_num

    return result_str

def factor2(num):
    result = 1L

    for i in range(2, num + 1):
        result *= i

    return result

print factor(10)
print factor2(10)

