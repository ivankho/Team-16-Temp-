import sys

FIELDS = ["click", "impression", "display_url", "ad_id", "advertiser_id",\
          "depth", "position", "query_id", "keyword_id", "title_id",\
          "description_id", "user_id"]

def parse_line(line):
    line = line.strip()
    fields = line.split('\t')
    field_dic = {}
    for i in range(0, len(FIELDS)):
        field_dic[FIELDS[i]] = fields[i]
    return field_dic

pclick = 0
conditionalsclick = {}
conditionalsnoclick = {}

#assume each line is feature(ad id), clicks, impressions.


def train(data):
    totalclicks = 0
    totalimps = 0
    instances = []
    global pclick
    
    #compute total clicks and total impressions, for P(Y)
    for line in data:
        instance = line.strip().split('\t')
        clicks = instance[1]
        imps = instance[2]
        totalclicks += int(clicks)
        totalimps += int(imps)
        instances.append(instance)
        

    #P(Y)
    pclick = float(totalclicks)/totalimps
    
    #compute conditional probabilities. P(X|Y), P(X|not Y)
    for instance in instances:
        feature = instance[0]
        clicks = int(instance[1])
        imps = int(instance[2])
        conditionalsclick[feature] = float(clicks)/totalclicks
        conditionalsnoclick[feature] = float((imps - clicks))/(totalimps - imps)


def predict(feature, plick):

    # max of P(X|Y)*P(Y)

    click = conditionalsclick[feature] * pclick
    noclick = conditionalsnoclick[feature] * (1-pclick)

    if click > noclick:
        return 1
    else:
        return 0

train(sys.stdin)

for k in conditionalsclick.keys():
    print 'feature: %s, prediction: %s' % (k, predict(k, pclick))
