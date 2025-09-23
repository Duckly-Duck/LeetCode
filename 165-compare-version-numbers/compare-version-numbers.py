class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #shitty one

        # v1=version1.split(".")
        # v1=[int(v1[i]) for i in range(len(v1))]

        # v2=version2.split(".")
        # v2=[int(v2[i]) for i in range(len(v2))]

        # m=max(len(v1),len(v2))

        # for i in range(m):
        #     if i>=len(v1):
        #         v1.extend([0 for i in range(abs(len(v1)-len(v2)))])
        #     elif i>=len(v2):
        #         v2.extend([0 for i in range(abs(len(v1)-len(v2)))])
            
        #     if v1[i]==v2[i]:
        #         continue
                
        #     elif v1[i]<v2[i]:
        #         return -1
                
        #     return 1

        # return 0

        vs1, vs2 = version1.split("."), version2.split(".")
        m, n = len(vs1), len(vs2)

        for i in range(max(m, n)):
            v1 = int(vs1[i]) if i < m else 0
            v2 = int(vs2[i]) if i < n else 0

            if v1 < v2:
                return -1

            if v1 > v2:
                return 1

        return 0
        
