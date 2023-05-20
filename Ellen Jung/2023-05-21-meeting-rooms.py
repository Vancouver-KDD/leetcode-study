class Solution(object):
    def can_attend_meetings(self, meetings):
        meetings = sorted(meetings, key=lambda x: x[0])
        for i in range(0, len(meetings) - 1):
            if meetings[i][1] > meetings[i+1][0]:
                return False

        return True


def main():
    so = Solution()
    print(so.can_attend_meetings([[0, 30], [5,10], [15,20]]))
    print(so.can_attend_meetings([[7, 10], [2, 4]]))


if __name__ == '__main__':
    main()
