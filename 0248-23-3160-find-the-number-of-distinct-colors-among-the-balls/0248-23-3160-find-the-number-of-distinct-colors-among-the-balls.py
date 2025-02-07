class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = dict()
        colors = dict()
        n = len(queries)
        result = []

        for ball, color in queries:
            if ball in balls:
                prevColor = balls[ball]
                
                colors[prevColor] -= 1
                if colors[prevColor] == 0:
                    colors.pop(prevColor)

            colors[color] = colors.get(color, 0) + 1
            balls[ball] = color
            result.append(len(colors.items()))

        return result


                

        return result