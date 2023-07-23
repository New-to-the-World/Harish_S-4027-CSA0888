class Solution(object):
    def plusOne(self, digits):
        string =""
        result =[]
        for d in digits:
            string += str(d)
        i = int(string) + 1
        for w in str(i):
            result.append(w)
        return result
