# 5: Create list of things you would like to take on the empty island
# ● Write this list to the tab-delimited file, so that each element is on a different line and lines are
# numbered
# ● Example
# 1 casserole
# 2 book
# 3 knife
# 4 water bottle
# 5 fishing rod
# ● Hint: you can use print with additional parameters

things = ["knife", "blanket", "metal pot", "needle", "string"]

with open("items.txt", "w", encoding="utf-8") as f:
    for i, item in enumerate(things):
        f.write(str(i + 1) + "\t" + item + "\n")
