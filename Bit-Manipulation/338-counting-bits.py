"""
https://leetcode.com/problems/counting-bits

đếm số lượng bit 1 của 1 binary representation của 1 số

vd C1
5
1 0 1
0 0 1  -> số 1 là 000...0001 -> clear mọi bit khác trừ bit cuối
0 0 1
"""
def countBits(n):
    # C1: &1
    # AND 1 sẽ loại bỏ mọi bit khác (vì AND 0 = 0) trừ bit cuối thì depend nó là 0 hay 1.
    # result = []
    # for i in range(n+1):
    #     count = 0
    #     while i:
    #         count += i & 1
    #         i >>= 1
    #     result.append(count)
    # return result

    # C2: multiple in different hệ số
    # - Mọi số nguyên đều là 2N (chẵn) hoặc 2N + 1 (lẻ)
    # - Trong binary, nhân 2 thêm số 0 vào cuối (tương tự decimal nhân 10 thêm số 0 vào cuối). Trong hệ x, nhân x thêm số 0 vào cuối.
    # → Vì * 2 thêm mỗi số 0 nên x và 2x có cùng số set bit, còn 2x +1 sẽ nhiều hơn 1 set bit.
    result = [0]  # bắt đầu từ số 0 có 0 set bit, cùng set bit với số 2, 4, 6, 8, v.v
    for i in range(1, n + 1):
        # cái này chia 2, thay vì // 2 thì shift right 1 bit cũng đc
        # vì trong binary, x2 thêm 1 số 0, nên mình cứ bỏ đi 1 số 0 là chia 2
        # result.append(result[i // 2] + i % 2)
        result.append(result[i >> 1] + i % 2)  # nếu là số lẻ (i % 2) thì nhiều hơn 1 set bit
    return result

if __name__ == '__main__':
    print(countBits(5))