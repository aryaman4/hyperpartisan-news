from xml2panda import *
from afinn import Afinn
import matplotlib.pyplot as plt
af = Afinn()
data = xml_panda('articles-training-byarticle-20181122.xml')
scores = [af.score(t) for t in data['title']]
gt = xml_panda_gt('ground-truth-training-byarticle-20181122.xml')
truths = [h for h in gt['hyperpartisan']]
vals = [0 if h == 'false' else 1 for h in truths]
pairs = [(scores[i], vals[i]) for i in range(len(scores))]
print(pairs)
plt.plot(scores, vals, 'ro')
plt.ylabel('truths')
plt.xlabel('sentiment scores')
plt.show()
