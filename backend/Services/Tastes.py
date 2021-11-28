import data_treatment.dataframe_functions_use as dataframe

ingredients = dataframe.get_empty_ingredient_dict()
please_dont=[]
# list of all the most heaviest ingredient
# this array SHOULD ALWAYS BE SORTED by weight asc order
heaviest =[("",0),("",0),("",0),("",0),("",0),("",0),("",0),("",0),("",0),("",0)]

def find_heavier(dictionnary):
    for key in dictionnary:
        find_and_eject((key,dictionnary[key]))
    print("this is supposed to be the eavyest :")
    print(heaviest)

# compare the weight to every weight in the array
# if this one is bigger thant any one of them, it replace the less heavy ( i forgot the word lol ) of them
# as the array is always sorted , we only need to check for the first element of it
def find_and_eject(tuple):
    BoolQuiChamboule=False
    if(tuple[1]>heaviest[0][1]):
        BoolQuiChamboule=True
    if BoolQuiChamboule:
        heaviest[0] = tuple
        heaviest.sort(key=lambda y: y[1])



"""
fetch the appropriate recipe (eg the one wich match the most with the user)
"""
def fetch_tastefull_recipe(dont):
    find_heavier(ingredients)
    recipes = {}
    best_recipe=[("",0),("",0),("",0),("",0),("",0),("",0),("",0),("",0)]
    for key in ingredients:
        tab =dataframe.recipe_selection(key)
        for recipe in tab:
            if  recipe  not in dont:
                print(recipe+" is not in ",dont)
                if recipe in recipes.keys():
                    recipes[recipe]+=ingredients[key]
                else:
                    recipes[recipe]=ingredients[key]
                if recipes[recipe]>best_recipe[0][1]:
                    best_recipe[0]=(recipe,ingredients[key])
                    best_recipe.sort(key=lambda y: y[1])
            else:
                recipes[recipe]=1
    print(best_recipe)
    return best_recipe

"""
recipe : the name of the recipe
score : the rating of this recipe
take the score and modify the weight of each ingredients
"""
def rate_ingredient(recipe_name,grade):
    list_ingredients = dataframe.fetch_ingredient_per_recipe(recipe_name)
    for i in list_ingredients:
        ingredients[i]+=int(grade)
        print(ingredients)


"""""
compute the feedback from the user
 feedback have this formalism : "name_recipe:grade
"""""
def compute_feedback(array):
    aaa=[]
    print(array)
    for i in array:
        recipe_name=i.split(":")[0]
        aaa.append(recipe_name)
        grade=i.split(":")[1]
        print("this is the recipe :"+recipe_name)
        print("this is the grade :"+grade)
        rate_ingredient(recipe_name,grade)
    return aaa
"""
driver function that launch the ia thinking.
It take the body of the request ( see main.py) as arguement, wich is an array of string, and return another array of string
"""
def launch_ia(request_body):
    #first we adjust the weight of each ingredient
    dont =compute_feedback(request_body)
    #then we ask the ia for new recipes :
    best_recipe= fetch_tastefull_recipe(dont)
    print("BLIP BLOP those are the recipes that fit the best :",best_recipe)
    return best_recipe



