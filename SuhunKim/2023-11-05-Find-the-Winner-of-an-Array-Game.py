class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr)*2:
            return max(arr)
        winner = {}
        
        player1 = arr.pop(0)
        player2 = arr.pop(0)
        
        while True:
            if player1 > player2:
                arr.append(player2)
                if player1 not in winner:
                    winner[player1] = 1
                else:
                    winner[player1] += 1
            else:
                arr.append(player1)
                if player2 not in winner:
                    winner[player2] = 1
                else:
                    winner[player2] += 1
                player1 = player2
            
            if winner[player1] == k:
                break
            player2 = arr.pop(0)
        return player1