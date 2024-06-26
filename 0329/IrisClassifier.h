#ifndef UUID2847378629216
#define UUID2847378629216

/**
  * DecisionTreeClassifier(ccp_alpha=0.0, class_name=DecisionTreeClassifier, class_weight=None, criterion=gini, max_depth=None, max_features=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, num_outputs=3, package_name=everywhereml.sklearn.tree, random_state=None, splitter=best, template_folder=everywhereml/sklearn/tree)
 */
class DecisionTreeClassifier {
    public:

        /**
         * Predict class from features
         */
        int predict(float *x) {
            int predictedValue = 0;
            size_t startedAt = micros();

            
                    
            
            if (x[2] < 2.449999988079071) {
                
                    
            predictedValue = 0;

                
            }
            else {
                
                    
            if (x[3] < 1.75) {
                
                    
            if (x[2] < 4.950000047683716) {
                
                    
            if (x[3] < 1.6500000357627869) {
                
                    
            predictedValue = 1;

                
            }
            else {
                
                    
            predictedValue = 2;

                
            }

                
            }
            else {
                
                    
            if (x[3] < 1.550000011920929) {
                
                    
            predictedValue = 2;

                
            }
            else {
                
                    
            if (x[2] < 5.450000047683716) {
                
                    
            predictedValue = 1;

                
            }
            else {
                
                    
            predictedValue = 2;

                
            }

                
            }

                
            }

                
            }
            else {
                
                    
            if (x[2] < 4.8500001430511475) {
                
                    
            if (x[1] < 3.100000023841858) {
                
                    
            predictedValue = 2;

                
            }
            else {
                
                    
            predictedValue = 1;

                
            }

                
            }
            else {
                
                    
            predictedValue = 2;

                
            }

                
            }

                
            }


                    

            latency = micros() - startedAt;

            return (lastPrediction = predictedValue);
        }

        
            
            /**
             * Get latency in micros
             */
            uint32_t latencyInMicros() {
                return latency;
            }

            /**
             * Get latency in millis
             */
            uint16_t latencyInMillis() {
                return latency / 1000;
            }
            

    protected:
        float latency = 0;
        int lastPrediction = 0;

        
            
            
};



static DecisionTreeClassifier irisClassifier;


#endif
