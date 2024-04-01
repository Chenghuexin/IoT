import pandas as pd
from micromlgen import port
#from sklearn.tree import DecisionTreeClassifier, export_graphviz
from everywhereml.sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz

iris_df = pd.read_csv('iris.csv')
label = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2, 'OtherSpecies': 3}
iris_df['variety'] = iris_df['variety'].map(label)
X = iris_df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = iris_df['variety'].values
clf = DecisionTreeClassifier()
clf.fit(X, y)
print(clf.to_arduino(instance_name='irisClassifier')) # 將clf轉成Arduino標頭檔
#print(port(clf))

dot = export_graphviz(clf, out_file=None, feature_names=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'], class_names=['Setosa', 'Versicolor', 'Virginica', 'OtherSpecies'], filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot)
graph.format = 'png'
graph.render('iris', view=True)


'''
import pandas as pd
from micromlgen import port
from sklearn.tree import DecisionTreeClassifier
import graphviz

iris_df = pd.read_csv('./iris.csv')
#print(type(iris_df))
label = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2, 'OtherSpecies': 3}
iris_df['variety'] = iris_df['variety'].map(label)
X = iris_df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = iris_df['variety'].values
clf = DecisionTreeClassifier()
clf.fit(X, y)
print(port(clf))

dot = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot)
graph.format = 'png'
graph.render('iris', view=True)
'''