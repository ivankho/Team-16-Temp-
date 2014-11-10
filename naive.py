pclick = 0
conditionalsclick = {}
conditionalsnoclick = {}

#assume each line is feature(ad id), clicks, impressions.

def train(data):
    totalclicks = 0
    totalimps = 0
    for line in data:
        instance = line.strip().split('\t')
        clicks = instance[1]
        imps = instance[2]
        totalclicks += clicks
        totalimps += imps

    pclick = totalclicks/totalimps

    for instance in data:
        feature = instance[0]
        clicks = instance[1]
        imps = instance[2]
        conditionalsclick[feature] = clicks/totalclicks
        conitionalsnoclick[feature] = (imps - clicks)/(totalimps - imps)


def predict(feature):
    click = conditionalsclick[feature] * pclick
    noclick = conditionalsnoclick[feature] * (1-pclick)

    if click > noclick:
        return 1
    else:
        return 0

