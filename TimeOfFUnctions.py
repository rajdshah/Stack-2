# Time Complexity : O(n)
# Space Complexity :O(n)
class Solution(object):
    def exclusiveTime(self, n, logs):

        st = []
        res = [0 for _ in range(n)]
        prev = 0
        for i in range(len(logs)):
            strArr = logs[i].split(':')
            curr = int(strArr[2])


            if(strArr[1]=="start"):
                if(len(st)!=0):
                    res[st[-1]]+=curr - prev
                prev = curr
                st.append(int(strArr[0]))
            else:
                res[st.pop()]+=curr-prev+1
                prev = curr+1

        return res 
