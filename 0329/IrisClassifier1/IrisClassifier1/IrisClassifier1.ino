#include "IrisClassifier.h"  //DecisionTree
//#include "IrisClassifier2.h"  //RandomForest
//#include "IrisClassifier3.h"  //DecisionTree

// IrisClassifier.h creates a irisClassifier object
// that you can use to classify a feature vector
// no setup is required

void setup() {
    Serial.begin(115200);
}

void loop() {
    // replace with your actual feature vector
    float input[4] = {6.2, 2.8, 4.8, 1.8};//{5.1, 3.5, 1.4, 0.2};

    Serial.print("Predicted label (you should see '2': ");
    Serial.println(irisClassifier.predict(input));
    //Serial.println(irisClassifier3.predict(input));
    //Serial.println(RandomForest.predict(input));
    delay(1000);
}