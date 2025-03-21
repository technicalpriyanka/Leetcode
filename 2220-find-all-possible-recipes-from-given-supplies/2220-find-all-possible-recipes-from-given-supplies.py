class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        cur, ingredients = {*supplies}, [*map(set,ingredients)]
        for _ in recipes:
            for rcp,ingr in zip(recipes,ingredients):
                ingr<=cur and cur.add(rcp)
                
        return [*cur-{*supplies}]