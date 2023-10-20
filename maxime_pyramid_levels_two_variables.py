

def beeramid(bonus, price):

    beer_cans_available = (bonus / price).__floor__()
    level = 0

    while beer_cans_available >= (level + 1) ** 2:
        level += 1
        beer_cans_available -= level ** 2

    return level

print(beeramid(5000, 3))

# beeramid(1500, 2); // should === 12
# beeramid(5000, 3); // should === 16

