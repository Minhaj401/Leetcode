class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n=len(plants)
        i=0
        j=n-1
        refil=0
        awater=capacityA
        bwater=capacityB

        while i<=j:
            if i == j:
                if plants[i] > awater and plants[i] > bwater:
                    refil += 1
                break
            if plants[i]>awater:
                refil+=1
                awater=capacityA
            if plants[j]>bwater:
                refil+=1
                bwater=capacityB
            awater-=plants[i]
            bwater-=plants[j]

            i=i+1
            j=j-1
        return refil
            


