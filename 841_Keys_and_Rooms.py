from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=set()
        stack.add(0)
        rooms={i:j for i,j in enumerate(rooms)}
        while stack:
            room=stack.pop()
            if room in rooms:
                stack.update(rooms[room])
                rooms.pop(room)
        if rooms: return False
        else: return True

if __name__=="__main__":
    rooms = [[1],[2],[3],[]]
    print(Solution().canVisitAllRooms(rooms=rooms))