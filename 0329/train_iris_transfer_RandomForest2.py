import os
from micromlgen import port
from sklearn.datasets import load_iris
from everywhereml.sklearn.ensemble import RandomForestClassifier
iris = load_iris()

# Model (can also use single decision tree)
#from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=3)

# Train
model.fit(iris.data, iris.target)
#print(port(model))
print(model.to_arduino(instance_name='irisClassifier'))

# Extract single tree
#estimator = model.estimators_[5]

from sklearn.tree import export_graphviz
# Export as dot file
for idx, estimator in enumerate(model.estimators_):
    export_graphviz(estimator, out_file='tree{}.dot'.format(idx), 
                    feature_names = iris.feature_names,
                    class_names = iris.target_names,
                    rounded = True, proportion = False, 
                    precision = 2, filled = True)
    os.system('dot -Tpng tree{}.dot -o tree{}.png'.format(idx, idx))
'''

# Convert to png using system command (requires Graphviz)
from subprocess import call
call(['dot', '-Tpng', 'tree1.dot', '-o', 'tree1.png', '-Gdpi=600'])

# Display in jupyter notebook
from IPython.display import Image
Image(filename = 'tree1.png')
'''