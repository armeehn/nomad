#/bin/zsh

# A script for reproducing results in literature

echo 'Starting batch testing...\n'

for PROB_NUM in {19..21}
do
    for NUM_EVALS in {2,3}00 #{1,2,3}00 #{10..10}
    do
        echo "Doing problem number ${PROB_NUM}...with ${NUM_EVALS} bb evaluations."

        DATA_PATH="data/raw/problem-${PROB_NUM}/${NUM_EVALS}evals.txt"

        # Get the nomad data, but we have to create some temporary stuff first
        # first because its the quickest despite it being not the nicest
        PARAM_FILE="param-${PROB_NUM}.txt"
        # This needs to be saved, otherwise we'll lose it next invoke

        # 30 
        for i in {1..30}
        do

            SEED=$RANDOM
            SEED_PARAM_FILE="seed(${SEED})-${PARAM_FILE}"

            # Append the seed paran
            cp $PARAM_FILE $SEED_PARAM_FILE
            echo "SEED  ${SEED}" >> $SEED_PARAM_FILE
            echo "MAX_BB_EVAL ${NUM_EVALS}" >> $SEED_PARAM_FILE

            nomad $SEED_PARAM_FILE  | grep "best feasible"  \
                                    | tr -s ' '             \
                                    | cut -d ' ' -f5-       \
                                    | tee -a $DATA_PATH

            # We can redirect output with > to raw-data.txt
            # It can be cleaned up using the regex : "\(.*\) h=0 "

            rm $SEED_PARAM_FILE

        done
        echo "-------------"
    done
done

echo "Batching testing complete."
