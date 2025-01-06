class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        full_boxes=[i for i,x in enumerate(boxes) if x=="1"]
        ans=[0]*len(boxes)
        for i,x in enumerate(boxes):
             for full_box in full_boxes:
                 if i != full_box:
                    ans[i]+=abs(i-full_box)
        return ans